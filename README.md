# SSD Editorial — MVP

Sistema de Soporte a Decisiones con Aprendizaje Automático para predicción de
demanda bibliográfica. MVP funcional construido sobre los datos reales de
`input_locales/` (ver `Tesis_v2.3.md` y `Capstone Project Sistemas-v3.md` para
el contexto académico completo).

## Instalación

```
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pip install -e .
```

## Ejecutar el pipeline de datos/modelos por separado

```
.venv\Scripts\python.exe -m ssd_aa.pipeline
```

Imprime la comparación de los 3 modelos (Regresión Lineal, Random Forest,
XGBoost) y las métricas PRE (método empírico) vs POST (modelo ganador).

## Pruebas

```
.venv\Scripts\python.exe -m pytest -q
```

## Levantar la app (Streamlit — versión original)

```
.venv\Scripts\python.exe -m streamlit run app/Home.py
```

Credenciales de demo: usuario `editor`, contraseña `ambar2026` (configurables
en `.streamlit/secrets.toml`, ver `secrets.toml.example`).

## Levantar la app (Next.js + FastAPI — UI en migración)

La UI se está migrando a Next.js + Tailwind + shadcn/ui (fidelidad visual real
al mockup de `input_locales/prototipos/`), consumiendo una API FastAPI que
envuelve el mismo `ssd_aa.pipeline`. La app Streamlit de arriba sigue
funcionando en paralelo sin cambios, como referencia/fallback.

Dos procesos, en dos terminales:

```
# Terminal 1 — API (desde la raíz del repo)
.venv\Scripts\python.exe -m pip install -r requirements-api.txt
.venv\Scripts\python.exe -m uvicorn api.main:app --reload --port 8000 --workers 1

# Terminal 2 — Web
cd web
npm install
npm run dev   # http://localhost:3000
```

Copiar `web/.env.local.example` a `web/.env.local` antes del primer arranque.
Credenciales de demo: usuario `editor`, contraseña `ambar2026` (variables
`SSD_AUTH_USER`/`SSD_AUTH_PASSWORD` en `.env.local`).

Pruebas: `.venv\Scripts\python.exe -m pytest api/tests -q` (API) y
`cd web && npm run lint && npm run build` (tipos). Hay además un smoke test
con Playwright en `web/scripts/` (`node scripts/verify-login.mjs` y
`node scripts/verify-data.mjs`, requieren la API y la web corriendo).

**Progreso de la migración** (Fase 1 del plan):
- ✅ Login, shell de navegación (sidebar/topbar), Dashboard, Catálogo de
  Libros (búsqueda + paginación), Detalle del libro (5 tabs), Predicciones —
  conectados a datos reales vía la API.
- ⏳ Fase 2, aún solo en Streamlit: Alertas, Modelos IA, Simulador, Reportes
  y Configuración.

## Alcance y supuestos de este MVP

- No hay columna de inventario real: "stock actual" es un proxy (tiraje
  estimado del período anterior), no un dato de almacén.
- No hay columna con el tiraje que el editor decidió históricamente: el
  método "empírico" (PRE) se reconstruye como media móvil de 3 meses.
- El simulador usa ajustes de tendencia/estacionalidad en vez de las
  variables ilustrativas del mockup original (campaña escolar, publicidad,
  precio, competencia), que no existen en los datos.
- Fuera de esta iteración: LSTM (requiere TensorFlow), autenticación
  multiusuario real, base de datos gestionada, reentrenamiento programado.
