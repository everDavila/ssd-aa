"""Vista de detalle de un título, reutilizada desde Catálogo (drill-down) y
desde Predicciones (selector directo) — tabs Resumen/Predicción/Factores/
Historial/Recomendación, igual en espíritu al mockup (pantallas 4-6)."""

import pandas as pd
import streamlit as st

from ssd_aa.explain import compute_feature_importance
from ssd_aa.features import FEATURE_COLUMNS
from ssd_aa.pipeline import PipelineResult
from ssd_aa.ui.components import forecast_chart, risk_badge, shap_bar_chart


def _fila_catalogo(resultado: PipelineResult, titulo: str) -> pd.Series:
    fila = resultado.resumen_titulos[resultado.resumen_titulos["titulo"] == titulo].iloc[0]
    return fila


def render_book_detail(resultado: PipelineResult, titulo: str) -> None:
    fila = _fila_catalogo(resultado, titulo)

    st.markdown(f"## {titulo}")
    autor = fila.get("autor") or "—"
    genero = fila.get("genero") or "—"
    st.caption(f"{autor} · {genero}")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Stock actual (estimado)", f"{fila['stock_actual_estimado']:,.0f} unidades")
    c2.metric("Demanda prevista", f"{fila['demanda_prevista']:,.0f} unidades")
    c3.metric("Tiraje recomendado", f"{fila['tiraje_recomendado']:,.0f} unidades")
    with c4:
        st.caption("Riesgo")
        risk_badge(fila["riesgo"])

    tab_resumen, tab_prediccion, tab_factores, tab_historial, tab_recomendacion = st.tabs(
        ["Resumen", "Predicción", "Factores", "Historial", "Recomendación"]
    )

    with tab_resumen:
        st.markdown("**Información general**")
        info = {
            "Formato": str(fila.get("formato", "—")),
            "N.° páginas": str(fila.get("n_paginas", "—")),
            "PVP mayor (S/.)": str(fila.get("pvp", "—")),
            "Género": str(genero),
            "Autor/a": str(autor),
        }
        st.table(pd.Series(info, name="Valor"))

    with tab_prediccion:
        historial = resultado.df_features[
            (resultado.df_features["titulo"] == titulo) & resultado.df_features["ventas"].notna()
        ][["fecha", "ventas"]]
        st.plotly_chart(forecast_chart(historial, titulo), width="stretch")
        st.markdown("**Resumen de predicción**")
        st.write(
            f"Demanda esperada (próximo mes): **{fila['demanda_prevista']:,.0f} unidades**  \n"
            f"Tiraje recomendado: **{fila['tiraje_recomendado']:,.0f} unidades** "
            f"(colchón de seguridad sobre el pronóstico)  \n"
            f"Confianza del modelo: **{fila['confianza_modelo']:.0f}%** "
            "(heurística: 100 − MAPE de prueba del modelo activo, no una probabilidad calibrada)"
        )

    with tab_factores:
        fila_features = resultado.df_features[
            (resultado.df_features["titulo"] == titulo) & resultado.df_features[list(FEATURE_COLUMNS)].notna().all(axis=1)
            & resultado.df_features["ventas"].isna()
        ]
        if fila_features.empty:
            st.info("No hay suficiente historial continuo para explicar esta predicción.")
        else:
            importancia = compute_feature_importance(resultado.modelo_activo, fila_features[list(FEATURE_COLUMNS)])
            st.plotly_chart(shap_bar_chart(importancia), width="stretch")
            st.caption(
                "Los factores reflejan las variables que el modelo realmente usa "
                "(ventas recientes, tendencia, estacionalidad, perfil del título). "
                "El mockup original mostraba variables ilustrativas (campaña "
                "escolar, publicidad, competencia) que no existen en los datos."
            )

    with tab_historial:
        st.dataframe(
            historial.rename(columns={"fecha": "Mes", "ventas": "Ventas reales"}),
            hide_index=True, width="stretch",
        )

    with tab_recomendacion:
        st.write(f"Se recomienda imprimir **{fila['tiraje_recomendado']:,.0f} ejemplares** para el próximo período.")
        csv = fila.to_frame().T.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Generar orden de impresión (CSV)", data=csv,
            file_name=f"orden_impresion_{titulo.replace(' ', '_')}.csv", mime="text/csv",
        )
