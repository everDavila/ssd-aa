# CLAUDE.md

<!-- bitacora-doble-salida -->
## Cuando diga "para bitácora"

Haz DOS cosas, en este orden. No publiques nada en Sanity ni hagas deploy.

### 1. Bitácora técnica del proyecto (BITACORA.md en la raíz; créalo si no existe)
Agrega una entrada con la fecha de hoy: qué cambió, por qué, decisiones tomadas, lo que quedó pendiente y lo que NO se probó. Aquí sí van los detalles técnicos (archivos, commits, umbrales). Revisa el `git log` del día para no olvidar nada. Nunca incluyas tokens, claves ni correos personales.

### 2. Borrador para la bitácora pública de mi sitio (davila.uno)
Entrégamelo como texto para copiar y pasar a otra IA. La bitácora es un viaje: quien la ve debe notar todo por lo que paso, y quien la lee debe poder aprender de ella. Por eso importan el porqué, los tropiezos y lo que aprendí, más que el "cómo lo conecté".

**Voz**
- Primera persona, con mi voz. Como un tipo contándole a un colega, con un café en la mano, qué acaba de resolver y por qué importa. Lenguaje de trinchera, no de terminal: nada de "F1 terminada y pusheada" ni de commit message con puntos.
- Humor seco y autocrítico, sarcasmo suave. Los chistes salen de una imagen concreta, no de una exclamación, y suelen apuntar también hacia mí. Nada de comunicado corporativo.
- Sé honesto sobre lo que falta o no se probó. Termina con una línea corta que resuma o pinche.
- Groserías: con cuentagotas. Un "carajo" de vez en cuando cae bien, pero solo si tú lo dices por mí; nunca las agregues por tu cuenta y nunca contra una persona (van contra la situación, el bug o contra mí mismo).

**Ritmo y aire (que se lea de un bocado, no como muro de texto)**
- Oraciones cortas y remates claros, pero sin volver todo staccato: mezcla una frase que explica con otra corta que pincha.
- Una línea en blanco entre párrafos cada vez que cambie la idea (por ejemplo, de la decisión de fondo al dolor técnico). Párrafos de 1 a 3 frases.
- Texto plano (sin negritas, listas ni código). Que se entienda sin saber programar. Sin rutas, commits, IDs ni cifras, salvo una pincelada si hace falta.

**Qué merece entrada y cuántas**
- Una idea por entrada, cortas (unas 120 palabras como guía blanda). Si el trabajo tuvo varias cosas o varias iteraciones de algo, divídelo en varias entradas, una por momento. Nunca metas todo en una sola.
- NO hay tope de entradas por día: a veces trabajo varios días seguidos y pasan muchas cosas. El volumen lo decide el trabajo real. Lo que sí filtra son los microcambios.
- No documentes microcambios (un color, un margen, un typo, renombrar algo) salvo que sean parte de una historia más grande. Piensa en momentos de 2 o 3 horas de trabajo, no en minutos. Si algo cambió una decisión, enseñó algo, rompió o arregló algo que importaba, o cambió de cara para quien lo use, merece entrada. Si varias cosas chicas van juntas, agrúpalas en una sola.

**Qué entregarme por cada entrada**
- Proyecto, fecha y hora aproximada, dimensión sugerida (Idea, Producto, Interfaz, Implementación, Infraestructura, Aprendizaje, Hito, Investigación, Testing, Contenido, Datos, Diseño de sistema, Accesibilidad, Proceso, Cierre del día), tag sugerido (Hipótesis, Decisión, Exploración, Avance, Completado, Lección, Hito, Fallo, Pivote, Insight, Duda, Pausa, Validación) y el texto.
- Si algo no tiene su porqué, hazme UNA pregunta corta antes de escribir.
- Las capturas de cada entrada (regla "Capturas para la bitácora", siempre activa, más abajo): archivo y pie en español e inglés. Si falta alguna, dilo y explica qué tendría que mostrar.

**Si te dicto lo que hice hablando:** el dictado trae muletillas, repeticiones y frases a medias. Límpialo, pero conserva mi vocabulario, mis imágenes y mis chistes. No agregues bromas tuyas ni un registro más elegante que el mío.

Muestras de mi voz escrita:
- "Nimbus llegó a una versión que por fin puedo llamar estable. No porque esté terminado, sino porque ya puedo tocar algo sin preguntarme qué otra cosa acabo de romper."
- "Podría conectar un LLM desde ahora y hacer que genere comentarios infinitos. Suena bonito hasta que Firebase, APIs y compañía empiezan a enviar facturas con vocación de alquiler."
- "Nimbus no debería ser una app a la que entras solo para revisar si mañana llueve. Para eso ya existen bastantes aplicaciones. Y, siendo sinceros, varias lo hacen bastante bien."
- "No estoy cambiando de plataforma. Estoy cambiando de libertad."
<!-- /bitacora-doble-salida -->

<!-- bitacora-capturas -->
## Capturas para la bitácora (siempre activo)

Esta regla corre siempre, aunque nadie haya dicho "para bitácora". La captura se toma al probar, no al escribir la bitácora: días después, reproducir una pantalla cuesta más que la captura misma.

- Capturar en el momento en que algo se prueba y funciona, o cuando se rompe de forma visible. Arreglo visible: antes y después con el mismo encuadre (guarda el "antes" ANTES de tocar el código).
- No capturar microcambios ni migraciones o scripts sin efecto en pantalla. No inventar una pantalla para un hito invisible.
- Si puedes abrir la app (navegador, Playwright), la tomas tú al terminar la prueba, en el estado real que probaste: escritorio a 1440 px y celular a 390 px si el cambio es responsive; claro y oscuro solo si toca el tema. Si hace falta una sesión, un dispositivo real o una persona, pídele la captura a Ever en ese momento y dile exactamente qué mostrar (Win+Shift+S captura; Win+Shift+R video).
- Guardar en `bitacora-capturas/AAAA-MM-DD/NN-que-muestra.png` en la raíz del checkout principal, nunca dentro de un worktree (se borra). Antes y después: `03a-...-antes.png` y `03b-...-despues.png`. Recorridos o animaciones: video corto (MP4/WebM) o 3 a 5 capturas numeradas.
- La carpeta va en `.gitignore` (comprueba que lo esté): las imágenes se quedan en la PC. El script que toma las capturas va DENTRO del repo y sí se versiona; no lo dejes fuera del proyecto.
- Difumina correos, nombres de personas reales, tokens, IDs de sesión y ubicaciones exactas antes de guardar.
- Registro: en `BITACORA.md`, al final de la entrada técnica, una línea `Capturas:` con los archivos. Hito probado sin captura: `Captura pendiente: <qué mostrar>` en esa entrada y avísale a Ever; no lo omitas en silencio.
- En el borrador público, cada entrada visual lleva archivo + pie en español e inglés. Como la carpeta no se sube a git, para publicar hay que cargarlas en el campo "Imágenes y videos" de la entrada en Sanity.
- Nunca des por hecho un cambio visual que no hayas visto.
<!-- /bitacora-capturas -->
