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

await page.waitForSelector("text=MAPE actual");
console.log("Dashboard MAPE:", await page.locator("text=/\\d+\\.\\d+%/").first().innerText());
await page.screenshot({ path: `${SHOT_DIR}/10_dashboard_real.png`, fullPage: true });

await page.goto(`${BASE_URL}/catalogo`);
await page.waitForSelector("text=títulos · página");
console.log("Catalogo footer:", await page.locator("text=títulos · página").innerText());
await page.screenshot({ path: `${SHOT_DIR}/11_catalogo.png`, fullPage: true });

// Buscar por autor
await page.fill('input[name="q"]', "Cárdich");
await page.click('button:has-text("Buscar")');
await page.waitForLoadState("networkidle");
console.log("Búsqueda Cárdich:", await page.locator("text=títulos · página").innerText());
await page.screenshot({ path: `${SHOT_DIR}/12_catalogo_buscado.png`, fullPage: true });

// Detalle de un libro con historial
await page.goto(`${BASE_URL}/catalogo/TIT-010`);
await page.waitForSelector("text=Tiraje recomendado");
console.log("Detalle TIT-010 cargó tabs:", await page.locator('[data-slot="tabs-trigger"]').count());
await page.click("text=Factores");
await page.waitForTimeout(300);
await page.screenshot({ path: `${SHOT_DIR}/13_detalle_factores.png`, fullPage: true });

// Detalle de un libro SIN historial
await page.goto(`${BASE_URL}/catalogo/TIT-005`);
await page.waitForSelector("text=no tiene historial");
console.log("TIT-005 (sin historial) muestra aviso correctamente");

// Predicciones (selector + mismo componente)
await page.goto(`${BASE_URL}/predicciones`);
await page.waitForSelector("text=Tiraje recomendado");
console.log("Predicciones cargó con título por defecto");
await page.screenshot({ path: `${SHOT_DIR}/14_predicciones.png`, fullPage: true });

await browser.close();
console.log(hadErrors ? "FALLO: hubo errores de consola/página" : "OK: verificación de datos reales completa");
process.exit(hadErrors ? 1 : 0);
