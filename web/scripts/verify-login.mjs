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
  if (msg.type() === "error") {
    hadErrors = true;
    console.log("CONSOLE ERROR:", msg.text());
  }
});

await page.goto(BASE_URL);
await page.waitForURL("**/login");
await page.screenshot({ path: `${SHOT_DIR}/01_login.png` });
console.log("Login visible:", await page.locator("text=SSD Editorial").isVisible());

await page.fill("#usuario", "malo");
await page.fill("#contrasena", "malo");
await page.click('button[type="submit"]');
await page.waitForSelector('[role="alert"]');
console.log("Error de credenciales:", await page.locator('[role="alert"]').innerText());
await page.screenshot({ path: `${SHOT_DIR}/02_login_error.png` });

await page.fill("#usuario", "editor");
await page.fill("#contrasena", "ambar2026");
await page.click('button[type="submit"]');
await page.waitForURL("**/dashboard");
console.log("Redirigido a:", page.url());
await page.waitForTimeout(500);
await page.screenshot({ path: `${SHOT_DIR}/03_dashboard.png`, fullPage: true });

const rutas = ["/catalogo", "/predicciones", "/alertas", "/modelos", "/simulador", "/reportes"];
for (const ruta of rutas) {
  await page.goto(`${BASE_URL}${ruta}`);
  await page.waitForLoadState("networkidle");
  console.log(`${ruta} -> ${page.url().endsWith(ruta) ? "OK" : "REDIRIGIDO:" + page.url()}`);
}
await page.screenshot({ path: `${SHOT_DIR}/04_catalogo.png`, fullPage: true });

await page.goto(`${BASE_URL}/dashboard`);
await page.click('[data-slot="dropdown-menu-trigger"]');
await page.click("text=Cerrar sesión");
await page.waitForURL("**/login");
console.log("Tras logout, URL:", page.url());

await browser.close();
console.log(hadErrors ? "FALLO: hubo errores de consola/página" : "OK: verificación completa sin errores");
process.exit(hadErrors ? 1 : 0);
