from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_dashboard_shape():
    r = client.get("/api/dashboard")
    assert r.status_code == 200
    data = r.json()
    assert set(data.keys()) == {"kpis", "top_riesgo", "chart_demanda", "totales"}
    assert data["totales"]["total_catalogo"] == 55
    assert data["totales"]["titulos_activos"] == 21


def test_catalogo_lista_pagina_por_defecto():
    r = client.get("/api/catalogo")
    assert r.status_code == 200
    data = r.json()
    assert data["total"] == 55
    assert len(data["items"]) == 20  # page_size por defecto


def test_catalogo_busqueda_por_autor():
    r = client.get("/api/catalogo", params={"q": "cárdich"})
    assert r.status_code == 200
    data = r.json()
    assert data["total"] > 0
    assert all("cárdich" in item["autor"].lower() for item in data["items"])


def test_catalogo_detalle_titulo_con_historial():
    r = client.get("/api/catalogo/TIT-010")  # Beto el Espantapájaros (override de catálogo)
    assert r.status_code == 200
    data = r.json()
    assert data["tiene_historial"] is True
    assert data["resumen"] is not None
    assert data["historial"]


def test_catalogo_detalle_titulo_sin_historial():
    r = client.get("/api/catalogo/TIT-005")  # TIPO B real, sin historial
    assert r.status_code == 200
    data = r.json()
    assert data["tiene_historial"] is False
    assert data["resumen"] is None


def test_catalogo_detalle_titulo_inexistente():
    r = client.get("/api/catalogo/TIT-999")
    assert r.status_code == 404


def test_alertas_conteos_suman_el_total():
    r = client.get("/api/alertas")
    assert r.status_code == 200
    data = r.json()
    assert data["conteos"]["Todas"] == 21
    assert (
        data["conteos"]["Alto"] + data["conteos"]["Medio"] + data["conteos"]["Bajo"]
        == data["conteos"]["Todas"]
    )
    assert len(data["items"]) == 21


def test_alertas_filtro_por_riesgo():
    r = client.get("/api/alertas", params={"riesgo": "Alto"})
    assert r.status_code == 200
    data = r.json()
    assert all(item["riesgo"] == "Alto" for item in data["items"])
    assert len(data["items"]) == data["conteos"]["Alto"]


def test_modelos_incluye_lstm_proximamente_y_modelo_activo():
    r = client.get("/api/modelos")
    assert r.status_code == 200
    data = r.json()
    nombres = [f["modelo"] for f in data["filas"]]
    assert "LSTM" in nombres
    lstm = next(f for f in data["filas"] if f["modelo"] == "LSTM")
    assert lstm["estado"] == "Próximamente"
    assert lstm["mape"] is None
    activo = next(f for f in data["filas"] if f["modelo"] == data["modelo_activo"])
    assert activo["estado"] == "Activo"


def test_simulador_titulo_con_historial():
    r = client.post("/api/simulador", json={"id_titulo": "TIT-010", "ajuste_tendencia": 0, "ajuste_estacionalidad": 0})
    assert r.status_code == 200
    data = r.json()
    assert data["demanda_proyectada"] > 0
    assert 0 <= data["prob_quiebre"] <= 100
    assert 0 <= data["prob_sobrestock"] <= 100


def test_simulador_ajuste_estacionalidad_positivo_aumenta_demanda():
    base = client.post(
        "/api/simulador", json={"id_titulo": "TIT-010", "ajuste_tendencia": 0, "ajuste_estacionalidad": 0}
    ).json()
    subida = client.post(
        "/api/simulador", json={"id_titulo": "TIT-010", "ajuste_tendencia": 0, "ajuste_estacionalidad": 20}
    ).json()
    assert subida["demanda_proyectada"] > base["demanda_proyectada"]


def test_simulador_titulo_sin_historial_da_422():
    r = client.post("/api/simulador", json={"id_titulo": "TIT-005"})
    assert r.status_code == 422


def test_configuracion_expone_parametros_activos():
    r = client.get("/api/configuracion")
    assert r.status_code == 200
    data = r.json()
    assert 0 < data["print_run_safety_buffer"] < 1
    assert data["modelo_activo"]


def test_recomendaciones_csv_y_xlsx_descargan():
    r_csv = client.get("/api/reportes/recomendaciones.csv")
    assert r_csv.status_code == 200
    assert r_csv.headers["content-type"].startswith("text/csv")
    assert b"id_titulo" in r_csv.content

    r_xlsx = client.get("/api/reportes/recomendaciones.xlsx")
    assert r_xlsx.status_code == 200
    assert "spreadsheetml" in r_xlsx.headers["content-type"]
