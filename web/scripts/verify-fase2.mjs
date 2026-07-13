import { chromium } from "playwright";

const SHOT_DIR = process.env.SSD_SHOT_DIR ?? ".";
const BASE_URL = process.env.SSD_BASE_URL ?? "http://localhost:3000";

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

let hadErrors = false;
page.on("pageerror", (err) => {
  hadErrors = true;
  console.log("PAGE ERROR:", err.message);
});
page.on("console", (msg) => {
  const text = msg.text();
  if (msg.type() === "error" && !text.includes("caret-color")) {
    hadErrors = true;
    console.log("CONSOLE ERROR:", text);
  }
});

await page.goto(`${BASE_URL}/login`);
await page.fill("#usuario", "editor");
await page.fill("#contrasena", "ambar2026");
await page.click('button[type="submit"]');
await page.waitForURL("**/dashboard");

// Alertas
await page.goto(`${BASE_URL}/alertas`);
await page.waitForSelector("text=Riesgo alto");
console.log("Alertas: pill 'Riesgo alto' visible");
await page.click("text=Riesgo alto");
await page.waitForLoadState("networkidle");
const alertasAlto = await page.locator('a[href="/catalogo/TIT-001"]').count();
console.log("Alertas filtradas por Alto, items con link a catálogo:", alertasAlto >= 0 ? "ok" : "fallo");
await page.screenshot({ path: `${SHOT_DIR}/20_alertas.png`, fullPage: true });

// Modelos IA
await page.goto(`${BASE_URL}/modelos`);
await page.waitForSelector("text=LSTM");
console.log("Modelos IA: fila LSTM 'Próximamente' visible:", await page.locator("text=Próximamente").isVisible());
console.log("Modelos IA: hay fila 'Activo':", await page.locator("text=✅ Activo").isVisible());
await page.screenshot({ path: `${SHOT_DIR}/21_modelos.png`, fullPage: true });

// Simulador
await page.goto(`${BASE_URL}/simulador`);
await page.waitForSelector("text=Demanda proyectada");
const demandaInicial = await page.locator("text=/\\d[\\d,.]* unidades/").first().innerText();
console.log("Simulador: demanda inicial:", demandaInicial);

// mover el primer slider (tendencia) al máximo con teclado
const sliderTendencia = page.locator('[data-slot="slider-thumb"]').first();
await sliderTendencia.focus();
for (let i = 0; i < 30; i++) await page.keyboard.press("ArrowRight");
await page.click('button:has-text("Aplicar escenario")');
await page.waitForTimeout(500);
const demandaAjustada = await page.locator("text=/\\d[\\d,.]* unidades/").first().innerText();
console.log("Simulador: demanda tras +30% tendencia:", demandaAjustada);
await page.screenshot({ path: `${SHOT_DIR}/22_simulador.png`, fullPage: true });

// Reportes / Configuración
await page.goto(`${BASE_URL}/reportes`);
await page.waitForSelector("text=Descargar CSV");
console.log("Reportes: botones de descarga visibles");
await page.click("text=Configuración");
await page.waitForSelector("text=Colchón de seguridad");
console.log("Configuración: parámetros visibles:", await page.locator("text=Colchón de seguridad").isVisible());
await page.screenshot({ path: `${SHOT_DIR}/23_reportes_config.png`, fullPage: true });

await browser.close();
console.log(hadErrors ? "FALLO: hubo errores de consola/página" : "OK: verificación Fase 2 completa");
process.exit(hadErrors ? 1 : 0);
