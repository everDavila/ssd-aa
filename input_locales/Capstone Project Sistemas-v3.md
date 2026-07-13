## **FACULTAD DE INGENIERÍA** 

# **CARRERA DE INGENIERÍA DE SISTEMAS COMPUTACIONALES** 

## **INFORME DE PROYECTO FINAL** 

TÍTULO: IMPLEMENTACIÓN DE UN SISTEMA DE SOPORTE A DECISIONES CON APRENDIZAJE AUTOMÁTICO PARA MEJORAR LA PREDICCIÓN DE LA DEMANDA BIBLIOGRÁFICA 

**Autores:** BRICEÑO PORTILLO, Erik Antony DAVILA ATOCHE, Ever Antonio HUAMAN SARABIA, Jimena SANCHEZ MARIN, Sebastian Saul 

**Curso:** 

Capstone Project Sistemas 

**Docente del Curso:** GERARDO SARMIENTO QUISTAN 

Lima  – Perú 2026-1 

_Sistema de Soporte de Decisiones_ 

## **Contenido** 

|**Contenido**|**Contenido**|
|---|---|
|I.<br>RESUMEN. .............................................................................................................. 6||
|II.<br>INTRODUCCIÓN .................................................................................................... 7||
|2.1.|Motivación del proyecto ................................................................................... 8|
|2.2.|Hallazgos .......................................................................................................... 8|
|III.<br>ANÁLISIS DEL PROBLEMA ............................................................................ 9||
|3.1.|Antecedentes ..................................................................................................... 9|
|3.2.|Identificación y formulación del problema .................................................... 11|
|3.3.|Definición de variables ................................................................................... 12|
|3.4.|Definición de objetivos ................................................................................... 12|
|3.4.1.|Objetivo general ......................................................................................... 12|
|3.4.2.|Objetivos específicos .................................................................................. 12|
|3.5.|Población ........................................................................................................ 13|
|3.6.|Muestra ........................................................................................................... 13|
|3.7.|Matriz de dimensiones e indicadores.............................................................. 14|
|3.8.|Matriz de consistencia .................................................................................... 17|
|3.9.|Técnicas e instrumentos de recolección de datos ........................................... 19|
|3.10.|Validación y confiabilidad de datos ........................................................... 19|
|IV.<br>HERRAMIENTAS DE INGENIERÍA .............................................................. 21||
|4.1.|Comparación de metodologías o marcos de trabajo y estándares de ingeniería|
||21|
|4.2.|Selección de herramientas de hardware y software ........................................ 21|
|4.3.|Uso correcto de herramientas ......................................................................... 24|
|4.4.|Requisitos de usuario final y servidor ............................................................ 24|
|V.<br>GENERACIÓN DE SOLUCIONES ...................................................................... 25||
|5.1.|Alternativas de solución ................................................................................. 25|
|5.2.|Identificación y descripción de todas las restricciones realistas, criterios,|
|riesgos y limitaciones. ................................................................................................ 27|riesgos y limitaciones. ................................................................................................ 27|
|5.3.|Generación y análisis de múltiples soluciones ............................................... 29|
|5.4.|Análisis de los Contextos y su impacto .......................................................... 30|
|5.5.|Social .............................................................................................................. 30|
|5.6.|Cultural ........................................................................................................... 31|
|5.7.|Económico ...................................................................................................... 31|
|5.8.|Político ............................................................................................................ 32|
|5.9.|Legal ............................................................................................................... 32|



pág. 2 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

|5.10.|Medio Ambiente ......................................................................................... 32|
|---|---|
|5.11.|Seguridad .................................................................................................... 33|
|5.12.|Matriz comparativa de los impactos de las soluciones ............................... 33|
|5.13.|Importancia del impacto del proyecto ........................................................ 33|
|5.13.1.|Arquitectura del sistema ............................................................................. 34|
|5.13.2.|Modelo de datos ......................................................................................... 34|
|5.13.3.|Flujo de decisión del usuario ...................................................................... 35|
|5.13.4.|Prototipos .................................................................................................... 35|
|5.14.|Diseño de la alternativa seleccionada ......................................................... 35|
|5.15.|Business Case ............................................................................................. 35|
|5.16.|Cronograma del proyecto y EDT del proyecto ........................................... 36|
|5.17.|Plan de Gestión de Riesgos ........................................................................ 37|
|5.17.1.|Roles y Responsabilidades ......................................................................... 37|
|5.17.2.|Presupuesto ................................................................................................. 37|
|5.17.3.|Matriz de riegos .......................................................................................... 38|
|5.18.|Plan de Gestión de Interesados ................................................................... 39|
|5.18.1.|Registro de interesados ............................................................................... 39|
|5.18.2.|Alcance e impacto del proyecto sobre los interesados ............................... 40|
|5.19.|Presupuesto del proyecto ............................................................................ 42|
|5.20.|Plan de seguridad ........................................................................................ 42|
|5.21.|Plan de Calidad de software ....................................................................... 42|
|VI.<br>METODOLOGÍA DE DESARROLLO A UTILIZAR...................................... 42||
|6.1.|Desarrollo de la metodología .......................................................................... 42|
|6.2.|Pruebas de Calidad ......................................................................................... 43|
|6.2.1.|Pruebas unitarias ......................................................................................... 43|
|6.2.2.|Pruebas de aceptación ................................................................................. 43|
|6.3.|Despliegue ...................................................................................................... 45|
|6.4.|Resultados de medición de variable independiente ........................................ 46|
|VII.<br>RESULTADOS: EVALUACIÓN OPERATIVA Y ECONÓMICA ................. 47||
|7.1.|Análisis de Viabilidad técnica y tecnológica .................................................. 47|
|7.2.|Análisis de la viabilidad (de diferente tipo) y/o beneficio económico ........... 47|
|7.3.|Uso de indicadores y ratios ............................................................................. 48|
|7.4.|Análisis de la sostenibilidad ........................................................................... 48|
|7.5.|Discusión de resultados .................................................................................. 48|
|7.6.|Resultados en base a los objetivos del proyecto ............................................. 49|
|7.6.1.|Resultados del Objetivo específico 01........................................................ 49|



pág. 3 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

**==> picture [425 x 351] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||
|---|---|
|7.6.2.|Resultados del Objetivo específico 02........................................................ 49|
|7.6.3.|Resultados del Objetivo específico 03........................................................ 49|
|7.6.4.|Resultados del Objetivo específico 04........................................................ 49|
|7.6.5.|Resultados del Objetivo General ................................................................ 50|
|VIII.|RECOMENDACIONES FINALES ................................................................... 50|
|8.1.|Conclusiones ................................................................................................... 50|
|8.2.|Recomendaciones respaldadas por información y análisis............................. 51|
|IX.|COMPROMISO ÉTICO EN EL EJERCICIO PROFESIONAL ....................... 51|
|9.1.|Compromiso ético personal ............................................................................ 51|
|9.2.|Importancia del ejercicio ético a nivel profesional ......................................... 52|
|X.|REFERENCIAS O BIBLIOGRAFÍA .................................................................... 52|
|XI.|ANEXOS ............................................................................................................ 53|
|11.1.|Anexo 01:  Ficha de Registro ..................................................................... 53|
|11.2.|Anexo 02:  Instrumento validado por experto 01 ....................................... 54|
|11.3.|Anexo 03: Instrumento alidado por experto 02 .......................................... 54|
|11.4.|Anexo 04: Instrumento validado por experto 03 ........................................ 54|
|11.5.|Anexo 05: Matriz de Consistencia.............................................................. 55|
|11.6.|Anexo 06: Matriz de Variables (Operacionales) ........................................ 59|
|11.7.|Anexo 07: Prototipos .................................................................................. 66|

**----- End of picture text -----**<br>


**INDICE DE TABLAS** Tabla 1 : Análisis de Diagrama de Pareto ...................................................................... 11 Tabla 2:  Formulación de problema ................................................................................ 11 Tabla 3. Matriz de Dimensiones e indicadores............................................................... 14 Tabla 4  Matriz de Consistencia ..................................................................................... 17 Tabla 5.  Campos utilizados ........................................................................................... 19 Tabla 6.  Confiabilidad ................................................................................................... 19 Tabla 7  Stack de software y versiones utilizadas .......................................................... 21 Tabla 8  Requisitos de hardware del entorno de desarrollo y despliegue....................... 23 Tabla 9.  Matriz comparativa de requisitos versus alternativas de solución .................. 25 Tabla 10  Análisis comparativo de soluciones según restricciones contextuales ........... 29 Tabla 11  Síntesis de impactos del proyecto por contexto ............................................. 33 Tabla 12  Cronograma del proyecto ............................................................................... 36 Tabla 13  Roles y responsabilidades en la gestión de riesgos ........................................ 37 Tabla 14  Resumen de Costos por Tipo de Recurso ....................................................... 37 Tabla 15  Registro de interesados del proyecto .............................................................. 39 Tabla 16  Alcance e impacto del proyecto sobre los interesados ................................... 41 Tabla 17 Aplicación de Scrum durante el desarrollo del SSD (alineada al EDT y cronograma ..................................................................................................................... 43 Tabla 18  Casos de prueba unitaria ................................................................................. 43 Tabla 19  Casos de prueba de aceptación ....................................................................... 44 

pág. 4 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

Tabla 20  Medición de los indicadores de la variable independiente ............................. 46 Tabla 21  Resumen de viabilidad económica (valores referenciales anuales, en soles) . 47 Tabla 22 Indicadores y ratios PRE/POST implementación............................................ 48 

## **INDICE DE FIGURAS** 

Figura 1 : EDT del proyecto ........................................................................................... 36 Figura 2 Prototipo validado por el usuario ..................................................................... 44 Figura 3 Alertas del sistema ........................................................................................... 45 Figura 4 Predicciones  y recomendaciones del Sistema ................................................. 46 

**INDICE DE ANEXOS** Anexo 1 Ficha de Registro ............................................................................................. 53 Anexo 2 Instrumento validado por experto 01 ............................................................... 54 Anexo 3 Instrumento validado por experto 01 ............................................................... 54 Anexo 4 Instrumento validado por experto 01 ............................................................... 54 Anexo 5 Matriz de consistencia ..................................................................................... 58 Anexo 6 Matriz de variables ........................................................................................... 65 Anexo 7 Prototipos ......................................................................................................... 66 

pág. 5 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **I. RESUMEN.** 

Las editoriales tienen dificultades para saber cuántos libros producir: si imprimen de más, el stock se acumula sin venderse; si imprimen de menos, los títulos exitosos se agotan antes de tiempo. Esta investigación propone un sistema inteligente basado en Aprendizaje Automático que analiza el historial de ventas de una editorial limeña para predecir cuántos libros de narrativa infantil y juvenil se venderán, ayudando así a tomar mejores decisiones de producción. El estudio analizó 1 280 registros de ventas del período 2022-2025, correspondientes al segmento de lectores de 9 a 17 años, comparando los resultados obtenidos antes y después de implementar el sistema. Los resultados mostraron que el sistema reduce significativamente el margen de error en las predicciones y disminuye tanto el exceso como la falta de stock, lo que representa un beneficio directo para la planificación editorial. La investigación demuestra que incorporar herramientas de análisis de datos en la gestión editorial no solo mejora la eficiencia operativa, sino que también contribuye a que los libros adecuados estén disponibles en el momento oportuno para los lectores. 

Palabras clave: sistema de soporte a las decisiones; aprendizaje automático; predicción de demanda; gestión de inventarios; industria editorial. 

pág. 6 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **II. INTRODUCCIÓN** 

La industria editorial atraviesa una etapa de transición crítica, marcada por la convergencia entre la consolidación de los formatos digitales y la persistente relevancia del libro impreso. A pesar del auge de los libros electrónicos y el incremento del consumo de contenidos en dispositivos digitales, el libro físico se mantiene como un soporte fundamental de conexión sensorial y cognitiva, particularmente durante las etapas formativas del hábito lector. En este escenario, la supervivencia y competitividad de las organizaciones editoriales depende en gran medida de su capacidad para integrar tecnologías de la información que permitan una gestión inteligente de la producción física. 

La presente investigación se centra en el diseño e implementación de un Sistema de Soporte a las Decisiones (SSD) basado en técnicas de Aprendizaje Automático, orientado específicamente a la predicción de la demanda bibliográfica en Lima Metropolitana. El problema central que motiva este estudio es la ineficiencia en la gestión de inventarios, manifestada en un desequilibrio persistente entre el sobrestock de títulos de baja rotación y el quiebre de stock de aquellos con alta demanda. Esta situación se ve agravada por una toma de decisiones basada predominantemente en la experiencia empírica y en herramientas de análisis rudimentarias, lo que limita la capacidad de respuesta ante un mercado juvenil —segmento de 9 a 17 años— cada vez más volátil y competitivo. 

A través de la aplicación de algoritmos predictivos, esta tesis busca transformar los datos históricos y las tendencias de consumo en conocimiento accionable. No se pretende únicamente optimizar los recursos financieros de la editorial, sino también proporcionar una base científica para la creación de contenidos que logren conectar eficazmente con las nuevas generaciones de lectores, fomentando el libro físico como un objeto de valor pedagógico y cultural en la era digital. 

Adicionalmente, la organización carece de una base de datos integrada que consolide información histórica de ventas, preferencias del lector y patrones de estacionalidad, lo que restringe el uso de herramientas analíticas avanzadas. La ausencia de un sistema automatizado de predicción obliga a mantener decisiones reactivas y empíricas, reduciendo la capacidad de la editorial para diseñar estrategias orientadas tanto a la rentabilidad como al fomento progresivo del hábito lector. 

pág. 7 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

De persistir esta situación, la editorial podría enfrentar un incremento sostenido del sobrestock, una disminución de su competitividad en el mercado y una menor capacidad para desarrollar propuestas editoriales que conecten eficazmente con los intereses del público infantil y juvenil. 

## **2.1. Motivación del proyecto** 

La motivación central de esta investigación surge de la observación directa de una problemática operativa recurrente en una editorial familiar limeña especializada en literatura infantil y juvenil para el segmento de 9 a 17 años. Durante el período 2022– 2025, la organización sustentaba sus decisiones de producción e inventario en criterios empíricos y registros fragmentados en hojas de cálculo, sin contar con ningún sistema automatizado de análisis predictivo. Esta situación generaba de manera sistemática dos efectos contrapuestos e igualmente costosos: el sobrestock de títulos de baja rotación y el quiebre de stock de aquellos con alta demanda. La constatación de que esta brecha tecnológica podía abordarse mediante técnicas de Aprendizaje Automático disponibles en el ecosistema de código abierto motivó el diseño de un Sistema de Soporte a las Decisiones (SSD) como solución técnica, replicable y fundamentada científicamente. 

## **2.2. Hallazgos** 

Los resultados obtenidos validan la pertinencia de la intervención. La implementación del SSD produjo una reducción del error porcentual absoluto medio (MAPE) de 21.07% a 3.48%, una disminución del sobrestock de 23.57% a 7.64%, y una reducción del quiebre de stock de 19.15% a 6.24%. Estas mejoras fueron estadísticamente significativas (t = 115.23, p < .001), confirmadas además mediante la prueba no paramétrica de Wilcoxon y el análisis ANOVA para la comparación entre los tres algoritmos evaluados. En conjunto, los hallazgos demuestran que la integración de modelos predictivos en la gestión editorial no solo mejora la precisión del pronóstico de demanda, sino que reduce de forma cuantificable los costos operativos asociados a una gestión de inventarios deficiente. A continuación, se presenta el análisis detallado de la realidad problemática que dio origen a esta investigación. 

pág. 8 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **III. ANÁLISIS DEL PROBLEMA** 

## **3.1. Antecedentes** 

Huber y Stuckenschmidt (2020), Alemania, en su investigación titulada “Daily retail demand forecasting using machine learning with emphasis on calendric special days”, tuvieron como objetivo mejorar la precisión del pronóstico de demanda diaria incorporando días especiales del calendario como variables predictoras. La metodología adoptada fue cuantitativa y aplicada, con un diseño comparativo-experimental que utilizó series temporales de ventas diarias; aplicaron modelos de Aprendizaje Automático bajo el flujo CRISP-DM. Los resultados evidenciaron que dicho enfoque permite abordar patrones atípicos y generar pronósticos útiles para la planificación de la producción. Los autores concluyen que la incorporación del componente calendárico resulta determinante para el pronóstico operativo en el comercio minorista. 

Saha et al. (2022), Estados Unidos, en “Demand Forecasting of a Multinational Retail Company using Deep Learning Frameworks”, propusieron modelos basados en LSTM y LightGBM bajo arquitectura CRISP-DM para predecir la demanda estacional y apoyar decisiones de compras y control de inventario. Los resultados confirman que los enfoques de Deep Learning y de boosting son eficaces para el pronóstico en contextos minoristas de alta variabilidad. 

Punia y Shankar (2022), India, en “Predictive analytics for demand forecasting: A deep learning-based decision support system”, propusieron un modelo de analítica predictiva para generar pronósticos de demanda a corto, mediano y largo plazo, estructurado como un pipeline de DSS con Deep Learning dentro de un flujo CRISP-DM. Los autores concluyen que un DSS basado en Deep Learning fortalece significativamente la gestión de la demanda en organizaciones con grandes volúmenes de información histórica. Islek y Gunduz Oguducu (2017), Turquía, en “A Decision Support System for Demand Forecasting based on Classifier Ensemble”, construyeron un esquema de pronóstico de demanda mediante combinación de clasificadores (MLP, Bayesian Network, SVM) y técnicas de ensamble como stacking. Los resultados reportan un MAPE de 12.7% en la mejor configuración evaluada, concluyendo que la combinación de modelos incrementa de manera consistente la precisión del pronóstico. 

pág. 9 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

Park, Lee y Doo (2020), Corea del Sur, en “A Study of the Demand Forecasting Model for Publishing Business using Business Analysis”, identificaron los factores que inciden en la venta y devolución de libros, construyendo un modelo de pronóstico de demanda para una editorial a partir de cinco años de datos históricos (2012-2016) combinados con señales de portales digitales y redes sociales, mediante Gaussian Process Regression. Los autores concluyen que el pronóstico automatizado mejora significativamente las decisiones de tiraje e inventario en el contexto editorial. Wang et al. (2019), Estados Unidos, en “Success in books: predicting book sales before publication”, aplicaron el enfoque “Learning to Place” basado en Aprendizaje Automático para predecir ventas de libros antes de su publicación. Los resultados demuestran que la casa editorial emerge como un factor altamente influyente en el desempeño comercial, y concluyen que es posible anticipar dicho desempeño mediante modelos predictivos antes del lanzamiento al mercado. 

Nithin et al. (2022), India, en “Retail Demand Forecasting using CNN-LSTM Model”, propusieron un modelo híbrido que integra CNN para la extracción de patrones espaciales y LSTM para la dependencia temporal, dentro de un flujo CRISP-DM. Los resultados evidencian la utilidad de los enfoques híbridos para capturar patrones complejos en series de demanda. 

Bandara et al. (2019), Estados Unidos, en “Sales Demand Forecast in E-commerce using a Long Short-Term Memory Neural Network Methodology”, entrenaron una LSTM global con estrategias de agrupamiento de productos para mejorar los pronósticos en comercio electrónico. Los autores concluyen que el aprendizaje profundo global puede superar los enfoques univariados tradicionales en precisión y generalización. 

Theodoridis y Tsadiras (2025), Grecia, en “Retail Demand Forecasting: A Comparative Analysis of Deep Neural Networks and the Proposal of LSTMixer”, compararon modelos profundos multivariados y propusieron el modelo LSTMixer. Los resultados indican que el modelo propuesto alcanza un mejor desempeño que los enfoques estadísticos y de ML tradicionales, concluyendo que el pronóstico en retail debe migrar hacia arquitecturas profundas multivariadas. 

Rinaldi et al. (2025), Europa, en “DSS4EX: A Decision Support System framework to explore AI pipelines for time series forecasting”, propusieron un framework DSS para explorar, configurar y evaluar modelos de IA aplicados al pronóstico de series 

pág. 10 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

temporales. Los resultados evidencian que el framework facilita a usuarios no expertos la configuración de modelos y el análisis interactivo de resultados, concluyendo que los sistemas DSS orientados al forecasting promueven la adopción práctica del Aprendizaje Automático en organizaciones. Del conjunto de antecedentes revisados se desprenden tres vacíos que la presente investigación busca atender. Primero, la mayoría de los estudios se desarrollan en contextos de retail masivo o comercio electrónico con grandes volúmenes de datos; ninguno aborda específicamente el sector editorial de narrativa infantil-juvenil en economías emergentes de América Latina, donde la escala de producción es reducida y los datos históricos son limitados y heterogéneos. Segundo, si bien Park et al. (2020) constituyen el antecedente más próximo al contexto editorial, su modelo no incorpora un SSD con interfaz de decisión accesible para usuarios no técnicos ni contempla la comparación estadística PRE/POST mediante prueba t de Student. Tercero, ninguno de los estudios identificados aborda simultáneamente la limpieza de datos desde fuentes no estructuradas (hojas de cálculo) y la trazabilidad completa del proceso de predicción mediante metadatos de control de sesgo. La presente tesis responde a estos tres vacíos en el contexto específico de una editorial limeña con catálogo de ficción infantil-juvenil. 

## **3.2. Identificación y formulación del problema** 

## **Análisis con Diagrama de Pareto** 

Las causas principales del problema de predicción de demanda bibliográfica, ordenadas por frecuencia/impacto acumulado, son: 

_Tabla 1 : Análisis de Diagrama de Pareto_ 

|N°|Causa|Frecuencia<br>relativa|%<br>Acumulado|
|---|---|---|---|
|1|Toma de decisiones basada en criterio empírico del editor|35%|35%|
|2|Datos históricos dispersos sin estructura normalizada|25%|60%|
|3|Campos nulos,duplicados e inconsistencias en los registros|20%|80%|
|4|Ausencia de sistema de información o modelo analítico<br>formal|12%|92%|
|5|Meses sin registropor ausencia de reporte|8%|100%|



_Tabla 2: Formulación de problema_ 

Tipo Formulación 

pág. 11 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

|Problema<br>General|¿En qué medida la implementación de un Sistema de Soporte a Decisiones con<br>Aprendizaje Automático mejora la predicción de la demanda bibliográfica en Lima<br>Metropolitana, 2026?|
|---|---|
|PE1|¿En qué medida los modelos de Aprendizaje Automático incrementan la exactitud de<br>los pronósticos de demanda en comparación con los métodos convencionales de la<br>editorial?|
|PE2|¿En qué medida el SSD basado en datos históricos contribuye a la reducción del<br>sobrestock de títulos bibliográficos?|
|PE3|¿En qué medida la predicción mediante Aprendizaje Automático disminuye la<br>incidencia dequiebre de stock en la editorial?|
|PE4|¿En qué medida la integración del SSD reduce el tiempo de planificación de tirajes y<br>aumenta elporcentaje de decisiones editoriales respaldadaspor datos?|



## **3.3. Definición de variables** 

Variable Independiente: Sistema de Soporte a Decisiones con Aprendizaje Automático Conjunto integrado de herramientas tecnológicas, algoritmos de aprendizaje automático (LSTM, XGBoost, Random Forest) y bases de datos históricas que procesan información de demanda bibliográfica para generar predicciones precisas y apoyar la toma de decisiones editoriales. Se operacionaliza a través de sus dimensiones: algoritmos de AA, calidad de datos, registro y trazabilidad, y monitoreo del sistema. 

Variable Dependiente: Predicción de la Demanda Bibliográfica 

Proceso mediante el cual el sistema estima con anticipación la cantidad de unidades bibliográficas que serán demandadas en un período futuro, a través del análisis de patrones históricos de ventas e inventarios (2022–2025). Se operacionaliza mediante métricas de exactitud (MAE, RMSE, MAPE), eficiencia, optimización de inventario y apoyo a la toma de decisiones, evaluadas en escenarios PRE y POST intervención. 

## **3.4. Definición de objetivos** 

## **3.4.1. Objetivo general** 

Determinar en qué medida la implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático mejora la predicción de la demanda bibliográfica en Lima Metropolitana, 2026. 

## **3.4.2. Objetivos específicos** 

- .1.1. OE1: Determinar en qué medida los modelos de Aprendizaje Automático incrementan la exactitud de los pronósticos de demanda respecto a los métodos convencionales. 

pág. 12 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

- .1.2. OE2: Evaluar en qué medida el SSD basado en datos históricos reduce el sobrestock de títulos bibliográficos en la editorial. 

- .1.3. OE3: Determinar en qué medida la predicción mediante Aprendizaje Automático disminuye la incidencia de quiebre de stock. 

- .1.4. OE4: Evaluar en qué medida la integración del SSD reduce el tiempo de planificación de tirajes y aumenta el porcentaje de decisiones editoriales respaldadas por datos. 

## **3.5. Población** 

La población está constituida por la totalidad de los registros históricos de ventas e inventarios de títulos bibliográficos administrados por la editorial ubicada en Lima Metropolitana, correspondientes al período 2022–2025, los cuales ascienden a aproximadamente 3 250 registros. 

## **3.6. Muestra** 

La muestra está conformada por 1 280 registros históricos de ventas e inventarios correspondientes a títulos bibliográficos dirigidos al segmento de lectores de 9 a 17 años, extraídos del período 2022–2025. El tipo de muestreo es no probabilístico intencional, justificado por la importancia estratégica de dicho segmento para la editorial y la necesidad de contar con información representativa para el entrenamiento y validación de los modelos predictivos (21 títulos seleccionados por criterio editorial) 

pág. 13 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## **3.7. Matriz de dimensiones e indicadores** 

_Tabla 3. Matriz de Dimensiones e indicadores_ 

|**Variable**|**Dimensión**|**Indicador**|**Escala**|
|---|---|---|---|
|**V. Independiente Sistema de Soporte a**|Algoritmos de Aprendizaje Automático|Tipo de modelo implementado (LSTM,|Nominal|
|**Decisiones con AA**||XGBoost, Random Forest)||
|||Número de variables predictoras utilizadas|Discreta|
|||División entrenamiento / prueba (%)|Razón|
||Calidad de los Datos|% de registros completos sin valores nulos|Razón|
|||% de registros sin duplicados|Razón|
|||Rango temporal cubierto por datos históricos|Razón|
|||(años)||
||Registro y Trazabilidad|Fuente del dato (base histórica, ERP, registro|Nominal|
|||manual)||



|UNIVERSIDAD||||
|---|---|---|---|
|PRIVADA<br>DEL NORTE|_Sistema de Soporte de Decisiones_|||
|||Estado del sistema al momento de la|Ordinal|
|||predicción||
|||Versión del modelo de ML utilizado|Nominal|
|||% de predicciones registradas en el sistema|Razón|
||Monitoreo del Sistema|Frecuencia de reentrenamiento del modelo|Razón|
|||(veces/mes)||
|||N° de alertas generadas por degradación del|Discreta|
|||modelo||
|||Tiempo promedio de respuesta del sistema|Razón|
|||(segundos)||
|**V. Dependiente Predicción de la**|Exactitud de la Predicción|Error Absoluto Medio — MAE|Razón|
|**Demanda Bibliográfica**||||
|||Raíz del Error Cuadrático Medio — RMSE|Razón|



pág. 15 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

||Error Porcentual Absoluto Medio — MAPE|Razón|
|---|---|---|
||(%)||
|Eficiencia de la Predicción|Tiempo de procesamiento por predicción|Razón|
||(segundos)||
||Reducción del error vs. método convencional|Razón|
||(%)||
||N° de títulos procesados por ejecución|Discreta|
|Optimización del Inventario|Reducción del nivel de sobrestock (%)|Razón|
||Reducción del nivel de quiebre de stock (%)|Razón|
||Variación en la rotación de títulos|Índice|
||bibliográficos||



pág. 16 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

Apoyo a la Toma de Decisiones 

N° de decisiones editoriales respaldadas por el Discreta sistema 

## **3.8. Matriz de consistencia** 

_Tabla 4_ 

_Matriz de Consistencia_ 

## **Matriz de Consistencia** 

**“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en Lima Metropolitana, 2026”** 

|**Metropolitana, 2026”politana, 2026”olitana, 2026”, 2026” 2026”**|||||
|---|---|---|---|---|
|**PROBLEMA**|OBJETIVOS|HIPÓTESIS|VARIABLES|METODOLOGÍA|
|**1. Problema General**|1. Objetivo General|1. Hipótesis General|Variable 1:|1. Tipo de Investigación:|
|**¿En qué medida la**|Determinar en qué medida la|La implementación de un|VARIABLE INDEPENDIENTE:|Aplicada|
|**implementación de un**|implementación de un|Sistema de Soporte a Decisiones|Sistema de Soporte a Decisiones||
|**Sistema de Soporte a**|Sistema de Soporte a|con Aprendizaje Automático|con Aprendizaje Automático||
|**Decisiones con**|Decisiones con Aprendizaje|mejora significativamente la|||
|**Aprendizaje Automático**|Automático mejora la|predicción de la demanda|||
|**mejora la predicción de la**|predicción de la demanda|bibliográfica en Lima|||
|**demanda bibliográfica en**|bibliográfica en Lima|Metropolitana, 2026.|||
|**Lima Metropolitana, 2026?**|Metropolitana,2026.||||
|**2. Problemas Específicos**|2. Objetivos Específicos|2. Hipótesis Específicas:|Variable 2:|2. Nivel de la Investigación:|
|**PE1: ¿En qué medida los**|OE1: Determinar en qué|HE1: Los modelos de|VARIABLE DEPENDIENTE:|Correlacional-comparativo|
|**modelos de Aprendizaje**|medida los modelos de|Aprendizaje Automático|Predicción de la Demanda||
|**Automático incrementan la**|Aprendizaje Automático|presentan mayor exactitud en los|Bibliográfica||
|**exactitud de los**|incrementan la exactitud de|pronósticos que los métodos|||
|**pronósticos de demanda en**|los pronósticos de demanda|convencionales utilizados por la|||
|**comparación con los**|respecto a los métodos|editorial.|||
||convencionales.||||



pág. 17 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **métodos convencionales de** 

|**métodos convencionales de**||||
|---|---|---|---|
|**la editorial?**||||
|**PE2: ¿En qué medida el**|OE2: Evaluar en qué medida|HE2: El SSD reduce|3. Diseño de la Investigación:|
|**SSD basado en datos**|el SSD basado en datos|significativamente los niveles de|Preexperimental|
|**históricos contribuye a la**|históricos reduce el|sobrestock de títulos||
|**reducción del sobrestock**|sobrestock de títulos|bibliográficos en la editorial.||
|**de títulos bibliográficos?**|bibliográficos en la editorial.|||
|**PE3: ¿En qué medida la**|OE3: Determinar en qué|HE3: La predicción mediante|4. Método:|
|**predicción mediante**|medida la predicción|Aprendizaje Automático|Hipotético-deductivo|
|**Aprendizaje Automático**|mediante Aprendizaje|disminuye significativamente la||
|**disminuye la incidencia de**|Automático disminuye la|incidencia de quiebre de stock.||
|**quiebre de stock en la**|incidencia de quiebre de|||
|**editorial?**|stock.|||
|**PE4: ¿En qué medida la**|OE4: Evaluar en qué medida|HE4: La integración del SSD|5. Población:|
|**integración del SSD reduce**|la integración del SSD|con Aprendizaje Automático|~3 250 registros históricos de|
|**el tiempo de planificación**|reduce el tiempo de|reduce significativamente el|ventas e inventarios (2022–|
|**de tirajes y aumenta el**|planificación de tirajes y|tiempo de planificación de|2025)|
|**porcentaje de decisiones**|aumenta el porcentaje de|tirajes y aumenta el porcentaje||
|**editoriales respaldadas por**|decisiones editoriales|de decisiones editoriales||
|**datos en la editorial?**|respaldadas por datos.|respaldadas por datos en la||
|||editorial.||
||||6. Muestra:|
||||1 280 registros (segmento 9–17|
||||años)|
||||7. Tipo de Muestreo:|
||||Noprobabilístico intencional|
||||8. Técnica de Recolección:|
||||Análisis documental|
||||9. Instrumento de Recolección:|
||||Ficha de registro estructurada|
||||(28 campos)|



pág. 18 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## **3.9. Técnicas e instrumentos de recolección de datos** 

Técnica: Análisis documental, mediante revisión sistemática de las bases de datos internas de la editorial, registros históricos de ventas, informes de inventario e información generada por el sistema implementado. 

Instrumento: Ficha de registro estructurada (BD_FICHA_REGISTRO) con 28 campos agrupados en cuatro bloques funcionales: 

_Tabla 5. Campos utilizados_ 

|**Bloque**|**Campos incluidos**|
|---|---|
|**(a) Identificacióny calidad**|Título bibliográfico, período de análisis,ventas reales|
|**(b) Parámetros del algoritmo**|Tipo de modelo (LSTM/XGBoost/RF), división|
|**de AA**|entrenamiento/prueba,tiempo deprocesamiento|
|**(c) Métricas PRE/POST**|Predicciones de demanda, MAE, RMSE, MAPE, % sobrestock, %|
||quiebre de stock|
|**(d) Metadatos de trazabilidad**|Fuente del dato,estado del sistema,versión del modelo|



Los campos incluyen codificación numérica directa compatible con Python (Pandas, Scikit-learn, TensorFlow/Keras). 

## **3.10. Validación y confiabilidad de datos** 

**Validación:** El instrumento fue sometido a juicio de expertos — tres especialistas con grado de Magíster en Ingeniería de Sistemas y Gestión de TI — quienes evaluaron la pertinencia, relevancia y claridad de los 28 campos de la ficha de registro respecto a las dimensiones e indicadores de la matriz de operacionalización. 

**Confiabilidad:** Se evaluó mediante el método de **estabilidad temporal (test-retest)** sobre una muestra piloto de 30 registros históricos, analizando dos indicadores clave: 

_Tabla 6. Confiabilidad_ 

|**Indicador**|**Variable**|**Normalidad**|**Estadístico**|**Resultado**|
|---|---|---|---|---|
|||**(Shapiro-Wilk)**|||
|**Tiempo de**|Independiente|No normal (p <|Rho de Spearman =|Confiabilidad|
|**Procesamiento(s)**||.05)|.998(p< .001)|muyalta|
|**POST MAPE (%)**|Dependiente|Normal (p > .05)|Pearson r = .999 (p|Confiabilidad|
||||< .001)|muyalta|



_Sistema de Soporte de Decisiones_ 

Ambos resultados evidencian una **muy alta estabilidad temporal** del instrumento, garantizando que la extracción automatizada desde los logs del sistema produce mediciones consistentes y replicables. 

pág. 20 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **IV. HERRAMIENTAS DE INGENIERÍA** 

## **4.1. Comparación de metodologías o marcos de trabajo y estándares de ingeniería** 

Para el desarrollo del Sistema de Soporte a Decisiones (SSD), se evaluó el uso de metodologías de desarrollo de software tradicionales frente a marcos de trabajo orientados a datos. Se seleccionó la metodología **CRISP-DM** (Cross-Industry Standard Process for Data Mining). La elección se justifica porque CRISP-DM es el estándar de la industria estructurado en seis fases específicamente diseñadas para proyectos de minería de datos y aprendizaje automático. Esto permite contar con un pipeline documentado, auditable y replicable, lo cual es ideal para abordar la variabilidad de los datos históricos de la editorial. 

## **4.2. Selección de herramientas de hardware y software** 

La selección tecnológica se fundamentó en la necesidad de ofrecer una solución de bajo costo, adaptable al nicho editorial y sin dependencia de infraestructura de nube compleja. A continuación se especifican los componentes de software con sus versiones, garantizando la trazabilidad y replicabilidad del entorno de desarrollo. 

_Tabla 7_ 

_Stack de software y versiones utilizadas_ 

|**Componente**|**Herramienta**|**Versión**|**Función en el**|
|---|---|---|---|
||||**sistema**|
|**Lenguaje**|Python|3.11.9|Núcleo de|
|**base**|||desarrollo del|
||||SSD y del|
||||pipeline|
||||analítico|
|**Manipulación**|Pandas|2.2.3|Limpieza,|
|**de datos**|||transformación|
||||y|
||||estructuración|
||||de registros|
|**Cálculo**|NumPy|1.26.4|Operaciones|
|**numérico**|||vectoriales y|



pág. 21 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

||||soporte de|
|---|---|---|---|
||||arrays|
|**Cómputo**|SciPy|1.14.1|Funciones|
|**científico**|||estadísticas y|
||||soporte de|
||||scikit-learn|
|**Machine**|Scikit-learn|1.5.2|Random|
|**Learning**|||Forest,|
|**clásico**|||partición de|
||||datos y|
||||métricas|
|**Gradient**|XGBoost|2.1.3|Algoritmo de|
|**Boosting**|||ensamble para|
||||forecasting|
|**Deep**|TensorFlow /|2.17.0|Arquitectura|
|**Learning**|Keras|(Keras|LSTM para|
|||3.x)|series|
||||temporales|
|**Persistencia**|Joblib|1.4.2|Serialización|
|**de modelos**|||de modelos|
||||entrenados|
|**Interfaz /**|Streamlit|1.39.0|Frontend web|
|**Dashboard**|||interactivo para|
||||usuarios no|
||||técnicos|
|**Visualización**|Plotly|5.24.1|Gráficos de|
||||pronóstico e|
||||indicadores|
|**Visualización**|Matplotlib|3.9.2|Gráficos|
||||estadísticos|
||||(histogramas,|
||||boxplots)|
|**Lectura**|openpyxl /|3.1.5 /|Ingesta de los|
|**Excel/ODS**|odfpy|1.4.1|registros|
||||históricos|



pág. 22 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

|**Análisis**|IBM SPSS|26|Pruebas de|
|---|---|---|---|
|**estadístico**|Statistics||normalidad,|
||||Wilcoxon y|
||||ANOVA|
|**Control de**|Git|2.45+|Trazabilidad|
|**versiones**|||del código|
||||fuente|
|**Entorno de**|Visual Studio|1.95+|Editor de|
|**desarrollo**|Code||código|
|**Gestión de**|pip / venv|integrado|Aislamiento|
|**dependencias**||en|del entorno de|
|||Python|ejecución|
|||3.11||



_**Nota**_ . Las versiones fueron fijadas en un archivo _requirements.txt_ para asegurar la reproducibilidad del entorno. 

_Tabla 8_ 

_Requisitos de hardware del entorno de desarrollo y despliegue_ 

|**Recurso**||**Especificación**|**Especificación**|
|---|---|---|---|
|||**mínima**|**recomendada**|
|**Procesador (CPU)**||Intel Core i5 (10.ª gen)|Intel Core i7 / AMD|
|||/ AMD Ryzen 5|Ryzen 7|
|**Memoria RAM**||8 GB|16 GB|
|**Almacenamiento**||20 GB libres en disco|SSD NVMe|
|||SSD||
|**Tarjeta**|**gráfica**|No requerida|Opcional (no aporta|
|**(GPU)**|||mejora significativa)|
|**Sistema operativo**||Windows 10 / Ubuntu|Windows 11 / Ubuntu|
|||22.04 LTS|24.04 LTS|



_**Nota**_ . Dado el tamaño reducido del conjunto de datos (1 280 registros), el entrenamiento de los modelos —incluida la red LSTM— se ejecuta en tiempos operativos sobre CPU, sin requerir aceleración por GPU. Esta característica refuerza la viabilidad económica de la solución para una Pyme editorial, al no exigir hardware especializado. 

pág. 23 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **4.3. Uso correcto de herramientas** 

- **Recolección de datos:** La ingesta inicial de información se realizó a partir de archivos en formato **Excel / ODS** , extrayendo 1 280 registros históricos de ventas e inventarios correspondientes al período 2022-2025. 

- **Procesamiento y limpieza de datos:** Mediante el pipeline de datos en Python, se consolidó la información aplicando protocolos automatizados para la detección y corrección de valores nulos, registros duplicados e inconsistencias de nomenclatura originadas por el registro manual previo. 

- **Análisis de datos:** El motor predictivo evalúa los datos limpios generando pronósticos de demanda. Las herramientas analíticas calculan automáticamente métricas de error precisas para comparar escenarios PRE y POST implementación, tales como el MAPE (Error Porcentual Absoluto Medio), el MAE y el RMSE. 

## **4.4. Requisitos de usuario final y servidor** 

- **Requisitos del Usuario Final:** El sistema está enfocado en usuarios de negocio (editor jefe, responsable de inventario y gerencia editorial) que no poseen conocimientos técnicos en Machine Learning. Por ello, la herramienta final es un _dashboard_ editorial interactivo que visualiza pronósticos por título, genera alertas automáticas de sobrestock y quiebre de stock, y brinda recomendaciones claras de reposición para facilitar decisiones basadas en datos. 

- **Requisitos del Servidor/Infraestructura:** Para garantizar la viabilidad económica en una pyme editorial, el sistema está diseñado para un **despliegue en entorno local** . Esto permite el entrenamiento de los modelos y el funcionamiento operativo sin requerir licencias de software propietario de alto costo y sin una dependencia de conectividad permanente a servicios en la nube. 

pág. 24 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **V. GENERACIÓN DE SOLUCIONES** 

## **5.1. Alternativas de solución** 

Con la finalidad de seleccionar la solución tecnológica más adecuada para resolver la problemática de predicción de demanda bibliográfica identificada en la editorial, se procedió a realizar un análisis comparativo entre la propuesta desarrollada en la presente investigación y dos soluciones existentes en el mercado con funcionalidades afines: SAP Integrated Business Planning (SAP IBP) y Microsoft Azure Machine Learning (Azure ML). Ambas alternativas fueron seleccionadas por ser referentes reconocidos en la industria para tareas de forecasting y soporte a decisiones. 

La comparación se estructuró mediante una Matriz de Requisitos vs. Soluciones, en la que cada requisito funcional y no funcional fue derivado directamente de las dimensiones e indicadores operacionalizados en la presente investigación. La nomenclatura empleada es: ✔ cumple el requisito de forma nativa o completa; ◑ cumple parcialmente o con configuración avanzada; ✘ no cumple o no aplica en el contexto de la editorial. 

_Tabla 9._ 

_Matriz comparativa de requisitos versus alternativas de solución_ 

|Cód.|Requisito|Descripción del<br>requisito|SSD con<br>AA<br>_(propuesta)_|SAP IBP<br>_(solución_<br>_1)_|Azure<br>ML<br>_(solución_<br>_2)_|
|---|---|---|---|---|---|
|RE01|Procesamiento<br>de datos<br>históricos en<br>formato<br>Excel/ODS|Ingesta directa<br>desde hojas de<br>cálculo sin<br>infraestructura<br>ERP previa|✔|✘|◑|
|RE02|Entrenamiento<br>de múltiples<br>algoritmos ML<br>(LSTM,<br>XGBoost,RF)|Comparación y<br>selección del<br>modelo con<br>menor error<br>predictivo|✔|✘|✔|



pág. 25 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

|RE03|Cálculo<br>automático de<br>MAPE, MAE y<br>RMSE|Evaluación<br>cuantitativa del<br>error de<br>pronóstico post-<br>implementación|✔|◑|✔|
|---|---|---|---|---|---|
|RE04|Reducción del<br>sobrestock de<br>títulos<br>bibliográficos|Optimización del<br>nivel de<br>inventario según<br>predicción de<br>demanda|✔|✔|◑|
|RE05|Reducción del<br>quiebre de stock|Garantía de<br>disponibilidad de<br>títulos ante picos<br>de demanda|✔|✔|◑|
|RE06|Dashboard<br>interactivo para<br>usuarios no<br>técnicos|Visualización de<br>pronósticos<br>accesible para el<br>planificador<br>editorial|✔|◑|◑|
|RE07|Reducción del<br>tiempo de<br>planificación de<br>tirajes|Automatización<br>del proceso<br>decisional frente<br>al método<br>empírico|✔|◑|◑|
|RE08|Adaptabilidad al<br>segmento<br>editorial<br>infantil-juvenil<br>(9–17 años)|Configuración del<br>modelo para<br>catálogos de<br>nicho con<br>estacionalidad<br>específica|✔|✘|◑|
|RE09|Operación sin<br>licencias de<br>software<br>propietario de<br>alto costo|Viabilidad<br>económica para<br>una Pyme<br>editorial en Lima<br>Metropolitana|✔|✘|◑|
|RE10|Anonimización<br>de datos<br>comerciales<br>sensibles|Protección del<br>secreto comercial<br>de la editorial<br>colaboradora|✔|◑|✔|
|RE11|Trazabilidad y<br>log de versiones<br>del modelo|Registro de cada<br>ejecución<br>predictiva para<br>auditoría y<br>reentrenamiento|✔|◑|✔|
|RE12|Despliegue en<br>entorno local sin<br>dependencia de<br>nube|Funcionamiento<br>sin requerir<br>conectividad<br>permanente a<br>internet|✔|✘|✘|



pág. 26 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

|RE13|Validación<br>estadística<br>PRE/POST<br>mediante prueba<br>de Wilcoxon|Contraste<br>inferencial del<br>impacto de la<br>solución con<br>datos reales|✔|✘|✘|
|---|---|---|---|---|---|
|RE14|Pipeline CRISP-<br>DM<br>documentado y<br>replicable|Metodología de<br>desarrollo<br>estándar, auditada<br>y reproducible|✔|◑|◑|
|TOTAL<br>✔|||14/14|3/14|5/14|



_Nota._ SSD con AA: Sistema de Soporte de Decisiones son Aprendizaje Automatico 

Del análisis comparativo se desprende que las soluciones comerciales existentes —SAP IBP y Azure ML— si bien ofrecen capacidades predictivas de alto rendimiento en entornos corporativos con infraestructura robusta, no satisfacen los requisitos críticos del contexto específico de la presente investigación: operación sobre datos en formato Excel sin ERP, bajo costo de implementación para una Pyme, adaptabilidad al nicho editorial infantil-juvenil peruano y despliegue local sin dependencia de servicios en la nube. En contraste, el SSD con Aprendizaje Automático desarrollado en Python con interfaz Streamlit cumple la totalidad de los requisitos identificados, justificando su selección como solución óptima y convalidando metodológicamente la decisión de construir una solución propia en lugar de adoptar un producto comercial estándar. 

## **5.2. Identificación y descripción de todas las restricciones realistas, criterios, riesgos y limitaciones.** 

Durante el desarrollo del proyecto se presentarion limitaciones concretas durante su diseño, implementación y análisis, las cuales se detallan a continuación con el propósito de transparentar el alcance real de los hallazgos y orientar futuras investigaciones en la misma línea. 

Limitación 1 — Calidad inconsistente de la data histórica inicial. 

La base de datos proporcionada por la editorial presentó registros con valores nulos, formatos heterogéneos y duplicidades originadas en el registro manual previo a la implementación del sistema. Esta condición obligó a ejecutar procesos de imputación, normalización y filtrado metodológico no previstos en el cronograma inicial, 

pág. 27 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

incrementando los tiempos de preprocesamiento tecnológico y exigiendo decisiones técnicas adicionales por parte del investigador. 

Limitación 2 — Alcance geográfico y sectorial restringido. 

El estudio se circunscribe a una única editorial familiar de Lima Metropolitana, especializada en literatura narrativa para el segmento de 9 a 17 años. En consecuencia, los resultados y los modelos entrenados no pueden generalizarse directamente a otras editoriales de distinto tamaño, ubicación geográfica o catálogo temático, sin antes realizar un proceso de reentrenamiento y validación con datos propios de cada organización. 

Limitación 3 — Periodo temporal acotado del conjunto de datos. La muestra analizada abarcó registros históricos comprendidos entre 2022 y 2025 (N = 1,280). Si bien este volumen resultó suficiente para el entrenamiento y validación estadística de los algoritmos, el horizonte temporal no captura ciclos económicos de largo plazo ni disrupciones extraordinarias del mercado editorial (como crisis de papel, cambios arancelarios o eventos pandémicos), lo que puede limitar la robustez del modelo ante escenarios atípicos futuros. 

Limitación 4 — Diseño pre-experimental de grupo único. 

Al emplearse un diseño pre-experimental (G: O₁ → X → O₂) con un solo grupo de estudio, no se contó con un grupo control paralelo que permitiera aislar con total precisión el efecto exclusivo del sistema respecto a otras variables contextuales (como estacionalidad del mercado o cambios de política interna de la editorial) que pudieran haber influido simultáneamente en los indicadores post-test. 

Limitación 5 — Anonimización de variables comerciales sensibles. Con el fin de resguardar el secreto comercial de la editorial colaboradora, los títulos literarios y algunos indicadores de ventas fueron enmascarados en la ficha de registro. Si bien esta medida no afectó la integridad del análisis cuantitativo, impide la replicación exacta del estudio con los datos originales por parte de investigadores externos. 

pág. 28 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

Limitación 6 — Dependencia del entorno tecnológico seleccionado. 

El sistema fue desarrollado íntegramente en Python (Pandas, Scikit-learn, TensorFlow/Keras) y desplegado mediante Streamlit. La sostenibilidad operativa del SSD a largo plazo está condicionada a que la editorial mantenga el entorno tecnológico compatible, cuente con personal capacitado para su administración y garantice la actualización periódica de los modelos conforme los patrones de demanda evolucionen. 

Limitación 7 — Ausencia de grupo de control humano comparable. El indicador de tiempo de planificación y toma de decisiones (Dimensión 4) se midió comparando el proceso manual previo frente al uso del dashboard. Sin embargo, no fue posible estandarizar las condiciones cognitivas o de carga laboral del planificador en ambos momentos, por lo que los tiempos pre-test podrían estar influenciados por factores individuales no controlados. 

## **5.3. Generación y análisis de múltiples soluciones** 

Para determinar la solución tecnológica más viable frente a la problemática de predicción de demanda bibliográfica identificada, se evaluaron tres alternativas: el SSD con Aprendizaje Automático desarrollado a medida (propuesta de la presente investigación), SAP Integrated Business Planning (SAP IBP) y Microsoft Azure Machine Learning (Azure ML). Mientras que la matriz de requisitos de la sección 5.1 evaluó la cobertura funcional de cada alternativa, el presente análisis se centra en las restricciones contextuales reales del entorno de la editorial familiar objeto de estudio, organizadas en diez dimensiones. 

La escala empleada es: **favorable** o sin restricción relevante; ◑ restricción parcial o superable con esfuerzo adicional; **restricción crítica** que inviabiliza o limita severamente la solución en este contexto. 

_Tabla 10_ 

_Análisis comparativo de soluciones según restricciones contextuales_ 

|**RC01**<br>**RC02**<br>**RC03**|Presupuesto acotado de Pyme editorial<br>✔<br>✘<br>◑<br>Ausencia de infraestructura de nube o ERP<br>previo<br>✔<br>✘<br>✘<br>Datos de origen en Excel/ODS con calidad<br>inconsistente<br>✔<br>✘<br>◑|
|---|---|



pág. 29 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

|**RC04**|Sin equipo técnico de ciencia de datos dedicado|✔|✘|◑|
|---|---|---|---|---|
|**RC05**|Plazo corto de implementación (capstone|✔|✘|◑|
||académico)||||
|**RC06**|Adaptabilidad al nicho infantil-juvenil (9-17|✔|✘|◑|
||años)||||
|**RC07**|Usuarios finales no técnicos (editores,|✔|◑|◑|
||inventario)||||
|**RC08**|Protección del secreto comercial de la editorial|✔|◑|✔|
|**RC09**|Mantenibilidad por personal no especializado|✔|✘|◑|
|**RC10**|Escalabilidad futura del catálogo editorial|◑|✔|✔|



## _**Nota** : SSD con AA = Sistema de Soporte a Decisiones con Aprendizaje Automático. Elaboración propia._ 

Del análisis se desprende que las soluciones comerciales, pese a su robustez en entornos corporativos, presentan restricciones críticas en las dimensiones económica (RC01), de infraestructura (RC02) y de datos (RC03), que son precisamente las condiciones dominantes del contexto de la editorial. La única dimensión donde la propuesta muestra una restricción parcial es la escalabilidad futura (RC10): Streamlit y el despliegue local imponen un techo de crecimiento que, no obstante, resulta holgado para el volumen actual del catálogo (21 títulos, 1 280 registros). Este _trade-off_ es deliberado y coherente con el principio de simplicidad inteligente: se prioriza una solución ajustada al problema real por sobre una arquitectura sobredimensionada. En consecuencia, el SSD con Aprendizaje Automático se confirma como la alternativa optima para el contexto específico de la investigación. 

## **5.4. Análisis de los Contextos y su impacto** 

A continuación se describe el contexto actual asociado al proyecto en siete dimensiones y, para cada una, el impacto que genera la implementación del Sistema de Soporte a Decisiones. El análisis conecta las restricciones y beneficios ya identificados con el entorno social, cultural, económico, político, legal, medioambiental y de seguridad de la editorial. 

## **5.5. Social** 

## **Análisis del contexto** 

El hábito lector en el segmento infantil-juvenil (0 a 17 años) se encuentra en competencia directa con el consumo de contenidos digitales. El libro fisico conserva un rol formativo, pero su disponibilidad depende de decisiones de producción que, en la editorial estudiada, se tomaban de forma empírica, provocando que títulos demandados 

pág. 30 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

por los lectores se agotaran (quiebre de stock) y otros permanecieran inaccesibles por sobreproducción mal colocada. 

## **Impacto en el contexto** 

Al mejorar la precisión del pronóstico, el sistema aumenta la probabilidad de que los títulos correctos esten disponibles cuando el lector los requiere (quiebre de stock reducido de 19.15 % a 6.24 %). Esto favorece indirectamente el acceso sostenido a literatura infantil-juvenil y fortalece la continuidad del hábito lector en el segmento objetivo. 

## **5.6. Cultural** 

## **Análisis del contexto** 

La editorial produce narrativa infantil-juvenil de catálogo propio, un activo cultural cuya sostenibilidad económica condiciona la diversidad de la oferta editorial peruana. Las decisiones de tiraje empiricas ponian en riesgo la continuidad de títulos culturalmente valiosos pero de rotación irregular. 

## **Impacto en el contexto** 

El sistema permite distinguir cuantitativamente entre baja rotación coyuntural y baja demanda estructural, protegiendo la permanencia de títulos de valor cultural en el catálogo. Al cuantificar la demanda real, la decisión editorial deja de castigar por defecto a los títulos de nicho, preservando la diversidad de la producción narrativa. 

## **5.7. Económico** 

## **Análisis del contexto** 

La editorial es una Pyme familiar con márgenes ajustados. El sobrestock inmoviliza capital y genera costos de bodegaje; el quiebre de stock representa ventas no capturadas. Ambos efectos erosionaban directamente la rentabilidad, sin que existiera un instrumento para cuantificarlos ni anticiparlos. 

## **Impacto en el contexto** 

La reducción del sobrestock de 23.57 % a 7.64 % libera capital inmovilizado y disminuye costos de almacenamiento, mientras que la reducción del quiebre de stock recupera ingresos antes perdidos. El impacto económico se detalla y cuantifica en el Business Case y el análisis de viabilidad económica (Capítulo VII). 

pág. 31 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **5.8. Político** 

## **Análisis del contexto** 

El Estado peruano promueve el fomento del libro y la lectura a través de la Ley de Democratización del Libro y Fomento de la Lectura y de programas del Ministerio de Educación. Sin embargo, la digitalización tecnológica del sector editorial de menor escala continúa siendo limitada. 

## **Impacto en el contexto** 

El proyecto se alinea con las políticas de fomento del libro al hacer económicamente sostenible la producción de literatura infantil-juvenil. Además, demuestra que la adopción de analítica avanzada es viable en Pymes editoriales, aportando un caso replicable de digitalización del sector cultural. 

## **5.9. Legal** 

## **Análisis del contexto** 

El tratamiento de datos comerciales de la editorial está sujeto a la Ley N.o 29733 de Protección de Datos Personales y a la normativa de propiedad intelectual. Los registros contienen información sensible cuyo uso indebido podría afectar la competitividad de la organización. 

## **Impacto en el contexto** 

El sistema incorpora la anonimización de títulos e indicadores comerciales sensibles en la ficha de registro, y limita el uso de los datos a fines de la investigación. Las fuentes bibliográficas se citaron conforme a la normativa APA. Estas medidas aseguran el cumplimiento legal y resguardan el secreto comercial de la editorial colaboradora. 

## **5.10. Medio Ambiente** 

## **Análisis del contexto** 

La producción editorial fisica consume papel y energía. El sobrestock representa, en términos ambientales, recursos consumidos en ejemplares que no se venden y que eventualmente se convierten en merma o residuo, ampliando innecesariamente la huella ambiental del proceso productivo. 

## **Impacto en el contexto** 

Al reducir la sobreproducción en aproximadamente 16 puntos porcentuales, el sistema disminuye el consumo de papel y energía asociado a ejemplares no demandados. De 

pág. 32 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

este modo, la mejora en la precisión del pronóstico se traduce en un impacto ambiental positivo, alineando eficiencia económica y sostenibilidad. 

## **5.11. Seguridad** 

## **Análisis del contexto** 

Los registros históricos constituyen información crítica para la editorial. Su pérdida, alteración o filtración comprometería tanto la operación como la ventaja competitiva de la organización. El manejo previo en hojas de cálculo dispersas carecía de controles de respaldo e integridad. 

## **Impacto en el contexto** 

El despliegue local del sistema mantiene los datos dentro de la infraestructura de la editorial, reduciendo la superficie de exposición frente a un modelo en la nube. El Plan de Seguridad define controles de acceso, respaldo e integridad de datos que protegen la información a lo largo del ciclo de vida del sistema. 

## **5.12. Matriz comparativa de los impactos de las soluciones** 

La  Tabla 11 sintetiza el impacto del proyecto en cada contexto analizado, permitiendo una lectura integral de su contribución más allá de la dimensión estrictamente técnica. 

_Tabla 11_ 

_Síntesis de impactos del proyecto por contexto_ 

|**Contexto**|**Impacto del proyecto**|
|---|---|
|**Social**|Mayor disponibilidad de títulos demandados; refuerzo del hábito lector (quiebre de stock|
||de 19.15 % a 6.24 %).|
|**Cultural**|Preservación de títulos de valor cultural mediante decisiones de tiraje basadas en demanda|
||real.|
|**Económico**|Liberación de capital inmovilizado y recuperación de ventas; mejora directa de la|
||rentabilidad.|
|**Político**|Alineación con políticas de fomento del libro; caso replicable de digitalización de Pymes|
||editoriales.|
|**Legal**|Cumplimiento de la Ley N.o 29733 y de propiedad intelectual mediante anonimización y|
||uso restringido de datos.|
|**Medio**|Reducción del consumo de papel y energía por menor sobreproducción (sobrestock de|
|**Ambiente**|23.57 % a 7.64 %).|
|**Seguridad**|Resguardo de datos críticos mediante despliegue local y controles de acceso, respaldo e|
||integridad.|



## **5.13. Importancia del impacto del proyecto** 

El proyecto aborda un problema complejo de ingeniería en el sentido estricto del término: integra requisitos en conflicto (precisión predictiva frente a interpretabilidad para usuarios no técnicos), opera bajo restricciones reales múltiples (económicas, de 

pág. 33 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

datos, de infraestructura) y no admite una solución estándar de catálogo, como evidenció el análisis comparativo frente a SAP IBP y Azure ML. 

La importancia del impacto se sustenta en tres planos convergentes. En el plano operativo, el sistema transforma un proceso de decisión empírico y no trazable en uno cuantificable, auditable y reproducible. En el plano económico, convierte reducciones porcentuales de error en ahorros concretos de capital de trabajo y en recuperación de ingresos. En el plano metodológico, demuestra que técnicas de Aprendizaje Automático de código abierto, aplicadas con rigor bajo un pipeline CRISP-DM, resuelven problemas reales de una Pyme sin requerir la infraestructura de una gran corporación. Esta triple contribución es la que justifica el proyecto como una solución de ingeniería de valor real y no como una demostración académica aislada. 

## **5.13.1. Arquitectura del sistema** 

El sistema se organiza en cuatro capas lógicas. La capa de datos ingesta y consolida los registros históricos desde archivos Excel/ODS. La capa de procesamiento ejecuta la limpieza, transformación y validación mediante Python y Pandas. La capa de modelado entrena y compara los algoritmos Random Forest, XGBoost y LSTM, seleccionando el de menor error. La capa de presentación, construida en Streamlit, expone pronósticos, alertas y recomendaciones a los usuarios no técnicos. 

|**Capa**|**Responsabilidad**|**Tecnología**|**Fase CRISP-DM**|
|---|---|---|---|
|**Datos**|Ingesta y consolidación de registros|Excel/ODS, openpyxl,|Comprensión de|
||históricos|odfpy|los datos|
|**Procesamiento**|Limpieza, imputación, normalización|Python, Pandas, NumPy|Preparación de los|
||yfeatures||datos|
|**Modelado**|Entrenamiento y comparación de|Scikit-learn, XGBoost,|Modelado y|
||modelospredictivos|TensorFlow/Keras|Evaluación|
|**Presentación**|Dashboard, alertas y|Streamlit, Plotly|Despliegue|
||recomendaciones de tiraje|||



_**Nota.** La correspondencia con CRISP-DM asegura que cada componente técnico responde a una fase metodológica documentada._ 

## **5.13.2. Modelo de datos** 

El núcleo de datos es la ficha de registro estructurada (BD_FICHA_REGISTRO) de 28 campos, agrupados en cuatro bloques: identificación y calidad, parámetros del algoritmo, métricas PRE/POST y metadatos de trazabilidad. Esta estructura tabular única es suficiente para el volumen del proyecto y evita la complejidad de un modelo 

pág. 34 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

relacional multi-tabla que no aportaría valor a 1 280 registros de una fuente única. Cada fila representa la predicción de un titulo en un periodo, con su algoritmo, sus métricas de error y sus metadatos de control. 

## **5.13.3. Flujo de decisión del usuario** 

El flujo operativo para el usuario no técnico consta de cuatro pasos: (1) carga del archivo histórico; (2) ejecución del pipeline que limpia los datos y genera el pronóstico; (3) visualización del tiraje recomendado por titulo, acompañado de alertas de sobrestock o quiebre; y (4) exportación de la recomendación. El diseño minimiza la carga cognitiva: el usuario no interactúa con parámetros de modelos, sino con recomendaciones accionables expresadas en unidades de negocio (ejemplares a imprimir). 

## **5.13.4. Prototipos** 

El diseño de interfaz se materializó en prototipos que priorizan claridad y confianza sobre densidad visual. Las pantallas principales son: panel de carga y estado del procesamiento, tablero de pronóstico por titulo con semáforo de riesgo (sobrestock/quiebre), y vista de detalle por titulo con el histórico y el intervalo de la predicción. Los prototipos completos se presentan en el Anexo 

## **5.14. Diseño de la alternativa seleccionada** 

La alternativa seleccionada es un Sistema de Soporte a Decisiones estructurado sobre una arquitectura en capas que refleja las fases del pipeline CRISP-DM. El diseño separa explícitamente la gestión de datos, el modelado predictivo y la presentación al usuario, favoreciendo la mantenibilidad y la trazabilidad exigidas por el contexto editorial. 

## **5.15. Business Case** 

El detalle completo de este apartado se desarrolla en el documento Business Case adjunto como entregable independiente de este informe. 

Ob1_BusinessCase. docx 

pág. 35 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **5.16. Cronograma del proyecto y EDT del proyecto** 

_Figura 1 : EDT del proyecto_ 

_Tabla 12_ 

_Cronograma del proyecto_ 

|**EDT**|**Paquete de trabajo **|**Duración(días)**|**Cronograma(día)**|
|---|---|---|---|
|**1.0**|InicioyPlanificación|18|1 – 18|
|**1.1**|VisiónyBusiness Case|6|1 – 6|
|**1.2**|Product Backlog|5|7 – 11|
|**1.3**|Arquitectura Base|7|12 – 18|
|**2.0**|Desarrollo Iterativo|54|19 – 72|
|**2.1**|Sprint 1: Pipeline ETL|16|19 – 34|
|**2.2**|Sprint 2: Motor Predictivo|22|35 – 56|
|**2.3**|Sprint 3: Dashboard Web|16|57 – 72|
|**3.0**|PruebasyDespliegue|21|73 – 93|
|**3.1**|Pruebas de Aceptación|9|73 – 81|
|**3.2**|Pase a Producción|6|82 – 87|
|**3.3**|Capacitación de Usuarios|6|88 – 93|
|**4.0**|Cierre del Proyecto|10|94 – 103|
|**4.1**|Documentación Técnica|5|94 – 98|
|**4.2**|Retrospectiva Ágil|3|99 – 101|
|**4.3**|Acta de Cierre|2|102 – 103|



pág. 36 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

TOTAL 103 

1 – 103 

## **5.17. Plan de Gestión de Riesgos** 

## **5.17.1. Roles y Responsabilidades** 

La gestión de riesgos distribuye responsabilidades entre los integrantes del equipo según los roles de Liderar (L), Ejecutar (E) y Apoyar (A). 

_Tabla 13_ 

_Roles y responsabilidades en la gestión de riesgos_ 

|**Integrante**|**Rol en elproyecto**|**Responsabilidad en riesgos**|
|---|---|---|
|**Davila Atoche, Ever**|Líder técnico / Ciencia de|L - Identificación y respuesta a|
|**Antonio**|datos|riesgos técnicos|
|**Briceno Portillo, Erik**|Desarrollo / Integración|E - Ejecución de mitigaciones|
|**Antony**||técnicas|
|**Huaman Sarabia, Jimena**|Análisis de datos /QA|E - Monitoreo de calidad de datos|
|**Sanchez Marin, Sebastian**|Documentación / Interesados|A - Soporte y comunicación de|
|**Saul**||riesgos|



_**Nota.** El cronograma se ejecuta en el periodo académico 2026-1. Las semanas son_ 

_referenciales y se ajustan al calendario del curso._ 

## **5.17.2. Presupuesto** 

El presupuesto del proyecto se estructura en costos directos, costos indirectos y una reserva de gestión. Los costos directos ascienden a S/ 35,810.00 y comprenden el personal, los materiales o consumibles y las máquinas o bienes no consumibles. Sobre estos se aplican costos indirectos y gastos administrativos equivalentes a aproximadamente el 18 %. Finalmente, se incorpora una reserva de gestión de S/ 10,544.00, dimensionada según la tolerancia establecida en el Business Case para absorber la materialización de riesgos —principalmente el retrabajo asociado a la calidad de los datos—, con lo que el presupuesto total asciende a S/ 52,800.00. 

_Tabla 14_ 

_Resumen de Costos por Tipo de Recurso_ 

|**Rubro**|**Monto (S/)**|
|---|---|
|**Personal**|25,320.00|
|**Materiales / Consumibles**|5,630.00|
|**Máquinas / No Consumibles**|4,860.00|
|**Subtotal directo**|**35,810.00**|
|**Costos indirectos y gastos administrativos (≈ 18 %)**|6,446.00|



pág. 37 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

|UNIVERSIDAD||
|---|---|
|UNIVERSIDAD<br>PRIVADA<br>NORTE|_Sistema de Soporte de Decisiones_|
|**Reserva de gestión (según tolerancia BC)**|10,544.00|
|**PRESUPUESTO TOTAL**|**52,800.00**|



El desglose detallado de partidas y el sustento de cada estimación se presentan en el documento **Costeo de Proyecto** , adjunto como entregable independiente de este informe. 

Ob2_CosteoProyect o.docx 

## **5.17.3. Matriz de riegos** 

Los riesgos se evalúan por probabilidad e impacto, priorizando aquellos de nivel alto para su mitigación activa. 

El detalle completo de este apartado se desarrolla en el documento “Plan de Gestion de Riesgos” adjunto como entregable independiente de este informe. 

Ob3_PlanGestionRi esgos.docx 

pág. 38 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## **5.18. Plan de Gestión de Interesados** 

## **5.18.1. Registro de interesados** 

El registro de interesados se deriva de la matriz de involucramiento del proyecto SSD-AA y documenta, para cada interesado, su rol, expectativas, fase de mayor interés, postura, influencia e interés respecto del proyecto. 

_Tabla 15_ 

_Registro de interesados del proyecto_ 

|**Nombre / Grupo**|**Puesto / Org. /**|**Rol en el proyecto**|**Requisitos / Expectativas**|**Fase de mayor**|**Postura**|**Influencia**|**Interés**|
|---|---|---|---|---|---|---|---|
||**Empresa**|||**interés**||||
|**Gerencia**|Patrocinador —|Patrocinador;|Recibir KPIs mensuales (MAPE,|Inicio y Cierre|Partidario|Alto|Alto|
|**General**|Editorial Ambar|autoriza presupuesto|sobrestock, quiebre) y respaldar|||||
|||y decisiones de|decisiones de inversión y reposición|||||
|||inversión|basadas enpronósticos.|||||
|**Gerencia**|Gerencia — Editorial|Cliente directo del|Sustituir la planificación intuitiva por|Pruebas y|Neutral|Alto|Alto|
|**Editorial**|Ambar|dashboard; aprueba|decisiones respaldadas en ≥80 % por el|Despliegue||||
|||tirajes|sistema y justificar tirajes ante Gerencia|||||
||||General.|||||
|**Editor Jefe**|Área Editorial —|Usuario funcional|Recibir pronósticos mensuales por título|Desarrollo y|Partidario|Alto|Alto|
||Editorial Ambar|clave del módulo de|y métricas MAPE/MAE/RMSE para|Despliegue||||
|||pronóstico|reducir la incertidumbre en la|||||
||||planificación.|||||
|**Responsable de**|Área de Inventario|Usuario operativo|Pasar de la revisión manual en Excel a|Pruebas y|Neutral|Medio|Alto|
|**Inventario**|— Editorial Ambar|de alertas de|operar alertas automáticas de sobrestock|Despliegue||||
|||inventario|y quiebre de stock.|||||
|**Equipo de Datos**|Equipo de proyecto|Responsable del|Garantizar la calidad del dataset (1 280|Desarrollo|Partidario|Alto|Alto|
||(Capstone)|dataset y del|registros / 21 títulos) y del pipeline ETL|Iterativo||||
|||pipeline ETL|que alimenta los modelos.|||||



|||_Sistema de Soporte de Decisiones_|_Sistema de Soporte de Decisiones_|||||
|---|---|---|---|---|---|---|---|
|**Equipo ML**|Equipo de proyecto|Entrena y selecciona|Entrenar y comparar LSTM, XGBoost y|Desarrollo|Partidario|Alto|Alto|
||(Capstone)|el modelo predictivo|Random Forest, controlando el riesgo de|Iterativo||||
||||overfitting y definiendo el modelo a|||||
||||desplegar.|||||
|**Usuarios Finales**|Personal Editorial —|Operadores del|Operar el dashboard Streamlit en lugar|Pruebas y|Reticente|Bajo|Medio|
||Editorial Ambar|dashboard|de hojas de Excel ad-hoc; requieren|Despliegue||||
||||capacitaciónpara su adopción.|||||
|**Revisor Experto**|Auditor|Audita modelos y|Auditar los modelos y validar la validez|Pruebas y|Neutral|Medio|Medio|
||metodológico|valida la|científica (Wilcoxon, ANOVA) y los|Despliegue||||
|||metodología|planes de contingencia.|||||
|**Mg. Ing. Nidia**|Asesora de tesis —|Acompañamiento|Aprobar los entregables T1, T2 y EF del|Transversal (todo|Partidario|Alto|Alto|
|**Solórzano**|UPN|académico del|sílabo y brindar respaldo metodológico a|el ciclo)||||
|||proyecto|la tesis fuente.|||||
|**Equipo del**|Capstone Grupo 8 —|Ejecutores de los|Ejecutar los paquetes del EDT en 103|Transversal|Partidario|Alto|Alto|
|**Proyecto**|Dávila, Najarro,|paquetes del EDT|días y responder por el éxito del proyecto|(ejecución)||||
||Sánchez, Briceño,||y la sustentación final.|||||
||Huamán|||||||
|**Docente del**|Docente Capstone —|Evaluador|Evaluar T1 (sem 5), T2 (sem 7) y EF|Cierre|Neutral|Alto|Alto|
|**curso**|UPN|académico|(sem 8), definiendo la calificación final|(evaluación)||||
||||delproyecto académico.|||||



Nota: El detalle completo de este apartado se desarrolla en el documento “Plan de Involucramiento de Interesados” adjunto como entregable independiente de este informe. 

Ob4_PlanInvolucra mientoInteresados.d 

## **5.18.2. Alcance e impacto del proyecto sobre los interesados** 

pág. 40 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

A partir del registro anterior, se documenta el impacto y los cambios que el proyecto significa para cada interesado. 

_Tabla 16_ 

_Alcance e impacto del proyecto sobre los interesados_ 

|**Nombre / Grupo / Interesado**|**Descripción del impactoque significa elproyecto**|
|---|---|
|**Gerencia General**|Alto. Transita de aprobar reportes anuales a decidir inversión y reposición sobre la base de pronósticos; respalda el presupuesto de|
||S/ 52 800yneutraliza la resistencia al cambio.|
|**Gerencia Editorial**|Alto. Cambia su proceso operativo y la forma de justificar los tirajes ante la Gerencia General, sustituyendo la planificación|
||intuitivapor decisiones respaldadaspor el sistema.|
|**Editor Jefe**|Alto. Reduce la incertidumbre en la planificación; se convierte en el usuario principal del módulo de pronóstico y entrega|
||validaciones al Responsable de Inventario.|
|**Responsable de Inventario**|Alto. Cambia su rutina diaria y sus indicadores de desempeño al pasar de la revisión manual a la operación de alertas automáticas;|
||requiere capacitación intensiva.|
|**Equipo de Datos**|Alto. Su trabajo condiciona el desempeño de los modelos,al ser responsable de la calidad del datasetydelpipeline ETL.|
|**Equipo ML**|Alto. Definequé modelo se despliegaycontrola el riesgo de overfitting,determinando elproducto analítico final.|
|**Usuarios Finales**|Medio. Enfrentan una curva de aprendizaje al migrar de hojas de Excel al dashboard; constituyen la mayor fuente de riesgo de|
||adopción,mitigada con capacitación.|
|**Revisor Experto**|Medio. Garantiza la validez científica del estudio(Wilcoxon, ANOVA) yaporta credibilidad ante la Gerencia General.|
|**Mg. Ing. Nidia Solórzano**|Alto. Aprueba los entregables académicos(T1,T2yEF) yconstituye el respaldo metodológico de la tesis fuente.|
|**Equipo del Proyecto**|Alto. Responsable directo del éxito delproyectoyde la sustentación final;ejecuta lospaquetes del EDT en 103 días.|
|**Docente del curso**|Alto. Define la calificación final delproyecto académicoyrecibe los entregables degestión.|



_**Nota.** Impactos derivados de la columna 'Impacto del Cambio para el Interesado' del Plan de Gestión de Interesados (SSD-AA, v1.0)._ 

pág. 41 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## **5.19. Presupuesto del proyecto** 

_Utilizar formato para un trabajo más ordenado_ 

## **5.20. Plan de seguridad** 

El detalle completo de este apartado se desarrolla en el documento **“Plan de Seguridad** 

**Integral”** adjunto como entregable independiente de este informe. 

Plan_de_Seguridad _Integral.docx 

## **5.21. Plan de Calidad de software** 

El detalle completo de este apartado se desarrolla en el documento “ **Plan de** 

**Aseguramiento de Calidad** ” adjunto como entregable independiente de este informe. 

Plan_de_Asegurami ento_de_Calidad.do 

## **VI. METODOLOGÍA DE DESARROLLO A UTILIZAR** 

## **6.1. Desarrollo de la metodología** 

El desarrollo del Sistema de Soporte a Decisiones combinó dos metodologías complementarias: Scrum para la gestión del proyecto de software y CRISP-DM para el desarrollo del componente analítico basado en aprendizaje automático. La selección de CRISP-DM se justifica por ser el estándar de la industria estructurado en seis fases específicamente diseñadas para proyectos de minería de datos, lo que provee un pipeline documentado, auditable y replicable, idóneo para abordar la variabilidad de los datos históricos de la editorial. 

Scrum organizó el trabajo en cuatro Sprints con entregables incrementales, mientras que CRISP-DM estructuró el ciclo de vida del modelo predictivo. La Tabla 8 detalla los Sprints ejecutados. 

_Sistema de Soporte de Decisiones_ 

_Tabla 17_ 

_Aplicación de Scrum durante el desarrollo del SSD (alineada al EDT y cronograma_ 

|**Sprint**|**Objetivo**|**Actividades principales**|**Entregable**|**Duración**|**Cronograma**|
|---|---|---|---|---|---|
|||||**(días)**|**(día)**|
|**Sprint 1:**|Preparar la|Recolección, limpieza y|Dataset|16|19 – 34|
|**Pipeline**|información|transformación de 1 280|consolidado y|||
|**ETL**||registros; construcción del|pipeline ETL|||
|||pipeline ETL|operativo|||
|**Sprint 2:**|Construir el|Entrenamiento y|Modelo|22|35 – 56|
|**Motor**|modelo|comparación de XGBoost,|predictivo|||
|**Predictivo**||Random Forest y LSTM;|seleccionado|||
|||evaluación con MAE,||||
|||RMSEyMAPE||||
|**Sprint 3:**|Integrar la|Desarrollo del dashboard|Dashboard web|16|57 – 72|
|**Dashboard**|interfaz de|Streamlit, integración del|integrado|||
|**Web**|decisión|modelo, alertas y||||
|||recomendaciones||||



_**Nota.** Los tres Sprints corresponden a la fase 2.0 Desarrollo Iterativo del EDT. La fase 1.0 (Inicio y Planificación: requisitos, arquitectura y backlog, días 1-18) precede a los Sprints, y las fases 3.0 (Pruebas y Despliegue, días 73-93) y 4.0 (Cierre, días 94-103) las suceden, gestionadas como paquetes de trabajo fuera del ciclo iterativo de Scrum._ 

## **6.2. Pruebas de Calidad** 

## **6.2.1. Pruebas unitarias** 

Se emplearon pruebas unitarias sobre las funciones críticas del pipeline de datos y de cálculo de métricas, utilizando el framework pytest. La Tabla 10 resume los casos de prueba diseñados. 

_Tabla 18_ 

_Casos de prueba unitaria_ 

|**ID**|**Función probada**|**Entrada / Condición**|**Resultado esperado**|**Estado**|
|---|---|---|---|---|
|**PU01**|Carga de archivo|Archivo con 1 280 registros|DataFrame con 1 280 filas|OK|
||Excel/ODS||||
|**PU02**|Detección de valores|Registro con campo vacío|Registro imputado o|OK|
||nulos||marcado||
|**PU03**|Eliminación de|Registros repetidos|Conjunto sin duplicados|OK|
||duplicados||||
|**PU04**|Cálculo de MAPE|Vectores real/predicho|MAPE correcto (referencia|OK|
|||conocidos|manual)||
|**PU05**|Predicción del modelo|Registro de entrada válido|Salida numérica no nula|OK|



## **6.2.2. Pruebas de aceptación** 

pág. 43 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

Las pruebas de aceptación verificaron que el sistema satisface las historias de usuario definidas con los usuarios de negocio (editor y responsable de inventario), validando la usabilidad del dashboard para perfiles no técnicos. 

_Tabla 19 Casos de prueba de aceptación_ 

|**ID**|**Criterio de aceptación**|**Estado**|
|---|---|---|
|**PA01**|El usuario carga el archivo histórico sin asistencia técnica|OK|
|**PA02**|El sistema muestra el tiraje recomendadopor título|OK|
|**PA03**|El dashboardgenera alertas de sobrestocky quiebre de stock|OK|
|**PA04**|El usuario exporta la recomendación de tiraje|OK|
|**PA05**|El tiempo de obtención delpronóstico es inferior alproceso manual|OK|



_Figura 2 Prototipo validado por el usuario_ 

pág. 44 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

_Figura 3 Alertas del sistema_ 

## **6.3. Despliegue** 

El despliegue se realizó en entorno local, coherente con la restricción de viabilidad económica de una Pyme editorial. El sistema se ejecuta mediante Streamlit sobre el entorno de Python reproducible definido en el archivo requirements.txt, sin dependencia de servicios en la nube ni licencias propietarias. 

El proceso de despliegue comprende: (1) preparación del entorno virtual e instalación de dependencias desde requirements.txt; (2) ubicación del modelo entrenado y del dataset consolidado; (3) ejecución del dashboard con el comando de Streamlit; y (4) acceso del usuario mediante navegador en la red local de la editorial. Esta configuración mantiene los datos dentro de la infraestructura de la organización, reforzando la seguridad. 

pág. 45 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

_Figura 4 Predicciones  y recomendaciones del Sistema_ 

## **6.4. Resultados de medición de variable independiente** 

Los indicadores de la variable independiente (Sistema de Soporte a Decisiones con Aprendizaje Automático) se midieron a partir de la configuración del sistema, las métricas de rendimiento de los logs y la trazabilidad del pipeline, conforme al instrumento validado. La Tabla 12 presenta los valores obtenidos por dimensión. 

_Tabla 20_ 

_Medición de los indicadores de la variable independiente_ 

|**Dimensión**|**Indicador**|**Valor medido**|
|---|---|---|
|**Algoritmos de AA**|Tipo de modelo implementado|LSTM, XGBoost,|
|||Random Forest|
|**Algoritmos de AA**|División entrenamiento/prueba|70/30, 75/25, 80/20|
|**Calidad de los datos**|% de registros completos sin nulos(post-limpieza)|100 %|
|**Calidad de los datos**|% de registros sin duplicados|100 %|
|**Calidad de los datos**|Rango temporal cubierto|4 años(2022-2025)|
|**Registro y**|Fuente del dato|Base histórica|
|**trazabilidad**||(Excel/ODS)|
|**Registro y**|Versión del modelo|v1.0|
|**trazabilidad**|||
|**Registro y**|% de predicciones registradas|100 %|
|**trazabilidad**|||
|**Monitoreo del sistema**|Tiempopromedio de respuesta|~1.7 sporpredicción|



pág. 46 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

_**Nota.** Los porcentajes de calidad corresponden al estado del dataset posterior al proceso de limpieza. Los valores de configuración deben ajustarse a los definitivos de la implementación final._ 

## **VII. RESULTADOS: EVALUACIÓN OPERATIVA Y ECONÓMICA** 

## **7.1. Análisis de Viabilidad técnica y tecnológica** 

La viabilidad técnica quedó demostrada por la implementación completa del pipeline CRISP-DM sobre un stack de código abierto (Python, Pandas, Scikit-learn, XGBoost, TensorFlow/Keras y Streamlit). El sistema procesó los 1 280 registros y entrenó los tres algoritmos en tiempos operativos sobre hardware convencional, sin requerir aceleración por GPU dada la escala del conjunto de datos. La arquitectura en capas y la reproducibilidad del entorno confirman que la solución es técnicamente sostenible en el contexto de una Pyme editorial. 

## **7.2. Análisis de la viabilidad (de diferente tipo) y/o beneficio económico** 

La viabilidad económica se sustenta en la relación beneficio/costo del proyecto. Bajo supuestos referenciales (volumen anual de 30 000 ejemplares, costo de impresión de S/ 10.00, precio de venta de S/ 30.00 y bodegaje de S/ 2.50 por ejemplar), la reducción del sobrestock y del quiebre de stock genera un beneficio anual estimado que supera ampliamente el costo de la solución. 

_Tabla 21_ 

_Resumen de viabilidad económica (valores referenciales anuales, en soles)_ 

|**Concepto**|**Monto (S/)**|
|---|---|
|**Costo total de la solución**|8 910|
|**Beneficio por menor sobrestock**|19 200|
|**Beneficio por menor quiebre de stock**|23 400|
|**Beneficio anual total**|42 600|
|**Beneficio neto (Año 1)**|33 690|
|**Relación beneficio/costo (B/C)**|4.78|



_**Nota.** Cifras referenciales; deben validarse con la información financiera real de la editorial. Una relación B/C mayor que 1 confirma la viabilidad económica de la inversión._ 

pág. 47 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **7.3. Uso de indicadores y ratios** 

Los principales indicadores operativos y financieros del proyecto se resumen en la  , 

Tabla 22 contrastando el escenario previo (método empírico) con el posterior (SSD). 

_Tabla 22_ 

_Indicadores y ratios PRE/POST implementación_ 

|**Indicador**|**PRE (empírico)**|**POST (SSD)**|**Variación**|
|---|---|---|---|
|**MAPE(exactitud delpronóstico)**|21.07 %|3.48 %|-83 %|
|**Nivel de sobrestock**|23.57 %|7.64 %|-68 %|
|**Nivel dequiebre de stock**|19.15 %|6.24 %|-67 %|
|**Tiempo por predicción**|Proceso manual|~1.7 s|Reducción drástica|
||(horas)|||
|**Relación beneficio/costo**|No cuantificado|4.78|Positiva|



## **7.4. Análisis de la sostenibilidad** 

La sostenibilidad de la solución se evalúa en tres planos. En el plano técnico, el uso exclusivo de software de código abierto y el despliegue local eliminan costos recurrentes de licencias y nube, aunque condicionan la sostenibilidad a que la editorial mantenga el entorno y reentrene los modelos periódicamente. En el plano económico, la relación beneficio/costo favorable asegura que los ahorros superan los costos de mantenimiento. En el plano ambiental, la reducción de la sobreproducción disminuye el consumo de papel y energía, alineando eficiencia económica y responsabilidad ambiental. 

## **7.5. Discusión de resultados** 

Los resultados evidenciaron una mejora significativa y transversal en la totalidad de los indicadores tras la intervención. El descenso del error predictivo y la optimización de los índices de inventario permiten afirmar que la automatización analítica superó ampliamente al método empírico. Este hallazgo coincide con Theodoridis y Tsadiras (2025), quienes hallaron que los modelos basados en redes neuronales reducen la varianza del error frente a métodos manuales, y con Wang et al. (2019), que demostraron la fiabilidad del modelado predictivo estructurado en la industria del libro. La reducción del MAPE de 21.07 % a 3.48 % confirma que una etapa rigurosa de preprocesamiento es tan determinante como la elección del algoritmo. La disminución del sobrestock y del quiebre de stock se explica desde la gestión de la cadena de suministro integrada por tecnología, donde la sincronización entre demanda proyectada e inventario preserva el nivel de servicio. Finalmente, la adopción del dashboard por usuarios no técnicos se interpreta a la luz del Modelo de Aceptación Tecnológica (TAM), en función de la utilidad percibida y la facilidad de uso. 

pág. 48 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **7.6. Resultados en base a los objetivos del proyecto** 

## **7.6.1. Resultados del Objetivo específico 01** 

_Objetivo: Determinar en qué medida los modelos de Aprendizaje Automático incrementan la exactitud de los pronósticos de demanda respecto a los métodos convencionales._ 

Respecto a la exactitud del pronóstico, el MAPE se redujo de 21.07 % a 3.48 %. La prueba de Wilcoxon arrojó Z = -30.978 (p < .001), rechazando la hipótesis nula. Adicionalmente, el ANOVA de un factor confirmó diferencias significativas entre los tres algoritmos evaluados. Se concluye que los modelos de Aprendizaje Automático incrementan significativamente la exactitud del pronóstico frente al método convencional. 

## **7.6.2. Resultados del Objetivo específico 02** 

_Objetivo: Evaluar en qué medida el SSD basado en datos históricos reduce el sobrestock de títulos bibliográficos en la editorial._ 

En cuanto a la reducción del sobrestock, el nivel descendió de 23.57 % a 7.64 %. La prueba de Wilcoxon reportó Z = -30.990 (p < .001), confirmando una reducción estadísticamente significativa del inventario inmovilizado y, con ello, de los costos de bodegaje asociados. 

## **7.6.3. Resultados del Objetivo específico 03** 

_Objetivo: Determinar en qué medida la predicción mediante Aprendizaje Automático disminuye la incidencia de quiebre de stock._ 

Respecto a la disminución del quiebre de stock, su incidencia se redujo de 19.15 % a 6.24 %, con un estadístico de Wilcoxon de Z = -30.990 (p < .001). Este resultado evidencia una mejora significativa en el nivel de servicio: los títulos de alta demanda permanecen disponibles de forma consistente. 

## **7.6.4. Resultados del Objetivo específico 04** 

_Objetivo: Evaluar en qué medida la integración del SSD reduce el tiempo de planificación de tirajes y aumenta el porcentaje de decisiones editoriales respaldadas por datos._ 

En relación con la reducción del tiempo de planificación, el tiempo de procesamiento por predicción se ubicó entre 0.64 y 3.42 segundos según el algoritmo, frente a un proceso de planificación manual que demandaba considerablemente más tiempo. Esta 

pág. 49 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

automatización libera al planificador de la extracción manual de datos hacia el análisis estratégico. Cabe precisar que el contraste formal PRE/POST del tiempo no formó parte del análisis de Wilcoxon de los cinco pares de indicadores, por lo que su evaluación se sustenta en la medición operativa del sistema; su formalización estadística se identifica como una línea de mejora 

## **7.6.5. Resultados del Objetivo General** 

_Objetivo: Determinar en qué medida la implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático mejora la predicción de la demanda bibliográfica en Lima Metropolitana, 2026._ 

La confluencia de los resultados anteriores, con significancia estadística p < .001 en todos los indicadores contrastados, permite aceptar la hipótesis general: la implementación del Sistema de Soporte a Decisiones con Aprendizaje Automático mejora significativamente la predicción de la demanda bibliográfica. El sistema se consolida como una solución tecnológica eficaz, capaz de transformar la incertidumbre del mercado editorial en decisiones de tiraje precisas 

## **VIII. RECOMENDACIONES FINALES** 

## **8.1. Conclusiones** 

En relación con el objetivo general, se concluye que el Sistema de Soporte a Decisiones con Aprendizaje Automático mejora de forma transversal y estadísticamente significativa la predicción de la demanda bibliográfica, superando al método empírico tradicional y transformando los datos históricos en proyecciones confiables. Respecto al primer objetivo específico, se concluye que los algoritmos automatizados redujeron drásticamente el MAPE (de 21.07 % a 3.48 %), demostrando la superioridad de la lógica computacional frente al cálculo manual en la detección de patrones de consumo. 

En cuanto al segundo objetivo específico, se concluye que el sistema redujo significativamente el sobrestock (de 23.57 % a 7.64 %), liberando capital inmovilizado y espacio de almacén y protegiendo la inversión de la editorial. 

Sobre el tercer objetivo específico, se concluye que la predicción algorítmica disminuyó la incidencia de quiebre de stock (de 19.15 % a 6.24 %), asegurando un nivel de servicio continuo para el segmento lector objetivo. 

pág. 50 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

Finalmente, respecto al cuarto objetivo específico, se concluye que la automatización de la extracción de indicadores redujo el tiempo de planificación, migrando la labor del recurso humano del cálculo operativo hacia el análisis estratégico del negocio. 

## **8.2. Recomendaciones respaldadas por información y análisis** 

- **Ampliar el dataset histórico** para incorporar progresivamente nuevos registros 

y capturar ciclos de mercado de mayor horizonte, robusteciendo el modelo ante escenarios atípicos. 

- **Establecer una cadencia de reentrenamiento** del modelo (por ejemplo, 

trimestral) para evitar la degradación de la precisión conforme evolucionan los patrones de demanda. 

- **Complementar el MAPE** con métricas complementarias (por ejemplo, MAE o 

WAPE) al reportar títulos de baja rotación, dado que el MAPE presenta 

inestabilidad cuando las ventas se aproximan a cero. 

- **Evaluar la migración desde Streamlit** hacia una arquitectura de mayor 

escalabilidad (por ejemplo, un backend con API y una base de datos 

gestionada) únicamente si el catálogo de la editorial crece de forma sostenida, evitando sobredimensionar la solución de forma prematura. 

- **Formalizar la transferencia tecnológica** mediante un plan de capacitación al 

   - personal, condición necesaria para la sostenibilidad operativa del sistema a 

largo plazo. 

- **Instrumentar el contraste PRE/POST** del indicador de tiempo de 

planificación para incluirlo en el análisis inferencial en futuras iteraciones, 

cerrando el vacío de medición del cuarto objetivo. 

## **IX. COMPROMISO ÉTICO EN EL EJERCICIO PROFESIONAL** 

## **9.1. Compromiso ético personal** 

El detalle completo de este apartado se desarrolla en el documento “Compromiso Etico Personal”  adjunto como entregable independiente de este informe. 

pág. 51 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

Ob5_Compromiso_ Etico_Personal_.docx 

## **9.2. Importancia del ejercicio ético a nivel profesional** 

El detalle completo de este apartado se desarrolla en el documento “ **Importancia del** 

**ejercicio ético a nivel profesional** ”  adjunto como entregable independiente de este 

informe. 

Ob6_Importancia_d el_ejercicio_etico_a_ 

## **X. REFERENCIAS O BIBLIOGRAFÍA** 

Albarracín Manrique, M. A. (2025). Predicting employee turnover using applied machine learning. Ingeniería Industrial, 49, 214-238. 

Arias, F. (2023). El proyecto de investigación: Introducción a la metodología científica (8.ª ed.). Episteme. 

- Bandara, K., Shi, P., Bergmeir, C., Hewamalage, H., Tran, Q., & Seaman, B. (2019). Sales demand forecast in e-commerce using a long short-term memory neural network methodology. En Proceedings of the International Joint Conference on Neural Networks (IJCNN) (pp. 1-8). IEEE. 

- Bass, L., Clements, P., & Kazman, R. (2013). Software architecture in practice (3.ª ed.). Addison-Wesley. 

- Chambi Condori, P. P. (2023). Segmentación de mercado: Machine Learning en marketing en contextos de COVID-19. Industrial Data, 26(1), 275-294. 

- Connolly, T., & Begg, C. (2015). Database systems: A practical approach to design, implementation, and management (6.ª ed.). Pearson. 

- Hernández, R., Fernández, C., & Baptista, P. (2014). Metodología de la investigación (6.ª ed.). McGraw-Hill. 

- Huber, J., & Stuckenschmidt, H. (2020). Daily retail demand forecasting using machine learning with emphasis on calendric special days. International Journal of Forecasting, 36(4), 1420-1438. 

International Publishers Association. (2022). Global publishing statistics 2022. 

- Islek, I., & Gunduz Oguducu, S. (2017). A decision support system for demand forecasting based on classifier ensemble. En Proceedings of the International Conference on Data Science and Advanced Analytics (pp. 215-224). IEEE. 

Mamani Rodríguez, Z. (2022). Proceso de machine learning para determinar la demanda social de puestos de empleo de profesionales de TI. Industrial Data, 25(2), 275-293. 

Myers, G., Sandler, C., & Badgett, T. (2011). The art of software testing (3.ª ed.). Wiley. 

pág. 52 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

Nithin, R., Rajasekar, S., Jayanthy, S., & Karthik, R. (2022). Retail demand forecasting using CNN-LSTM model. En Proceedings of the International Conference on Electrical, Automation and Robotics Systems (ICEARS) (pp. 1-6). IEEE. 

- Park, J., Lee, S., & Doo, M. (2020). A study of the demand forecasting model for publishing business using business analysis. International Journal of Computing and Digital Systems, 9(4), 685-694. 

- Pino-Vargas, E., et al. (2025). Identification of vulnerable areas to flash floods using weighted sum analysis and unsupervised machine learning. Scientia Agropecuaria, 16(2), 249-261. 

- Punia, D., & Shankar, R. (2022). Predictive analytics for demand forecasting: A deep learningbased decision support system. Journal of Business Analytics, 5(2), 210-228. 

- Rinaldi, M., Theodorakos, G., Crema Garcia, P., Agudelo, J., & De Moor, K. (2025). DSS4EX: A decision support system framework to explore AI pipelines for time series forecasting. Expert Systems with Applications, 238, 121993. 

Sabino, C. (2018). El proceso de investigación científica. Panapo. 

- Saha, S., Gudheniya, S., Mitra, S., Das, S., Narayana, V., & Tiwari, M. K. (2022). Demand forecasting of a multinational retail company using deep learning frameworks. Procedia Computer Science, 203, 473-480. 

- Salas, F., & Caldas, J. (2024). Predicting undergraduate academic performance in a leading Peruvian university: A machine learning approach. Educación, 33(64), 55-74. 

Schwaber, K., & Sutherland, J. (2020). The Scrum Guide. Scrum.org. 

Sommerville, I. (2016). Software engineering (10.ª ed.). Pearson. 

- Theodoridis, A., & Tsadiras, A. (2025). Retail demand forecasting: A comparative analysis of deep neural networks and the proposal of LSTMixer. Applied Soft Computing, 146, 110718. 

- Wang, D., Yucesoy, B., Varol, O., Eliassi-Rad, T., & Barabási, A.-L. (2019). Success in books: Predicting book sales before publication. EPJ Data Science, 8(31), 1-21. 

- Artificial Intelligence and Multimodal Diagnostic Approaches in Cardiovascular Disease. (2025). Archivos Peruanos de Cardiología y Cirugía Cardiovascular, 6(4), 230-238. 

## **XI. ANEXOS** 

## **11.1. Anexo 01:  Ficha de Registro** 

BD_FICHA_de_regis tro_v01.1.xlsx 

_Anexo 1 Ficha de Registro_ 

pág. 53 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **11.2. Anexo 02:  Instrumento validado por experto 01** 

_Anexo 2 Instrumento validado por experto 01_ 

## **11.3. Anexo 03: Instrumento alidado por experto 02** 

_Anexo 3 Instrumento validado por experto 01_ 

## **11.4. Anexo 04: Instrumento validado por experto 03** 

_Anexo 4 Instrumento validado por experto 01_ 

pág. 54 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## **11.5. Anexo 05: Matriz de Consistencia** 

## **Matriz de Consistencia** 

**“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en Lima Metropolitana, 2026”** 

|**11.5. Anexo 05: Matriz de Consistencia**|**11.5. Anexo 05: Matriz de Consistencia**|**11.5. Anexo 05: Matriz de Consistencia**|**11.5. Anexo 05: Matriz de Consistencia**|**11.5. Anexo 05: Matriz de Consistencia**|
|---|---|---|---|---|
|**Matriz de Consistencia**<br>**“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en Lima**<br>**Metropolitana, 2026”**|||||
|**PROBLEMA**|**OBJETIVOS**|**HIPÓTESIS**|**VARIABLES**|**METODOLOGÍA**|
|**1. Problema General**|1. Objetivo General|1. Hipótesis General|Variable 1:|**1. Tipo de Investigación:**|
|**¿En qué medida la**|Determinar en qué|La implementación de un|VARIABLE|**Aplicada**|
|**implementación de un**|medida la|Sistema de Soporte a|INDEPENDIENTE:||
|**Sistema de Soporte a**|implementación de un|Decisiones con|Sistema de Soporte a||
|**Decisiones con**|Sistema de Soporte a|Aprendizaje Automático|Decisiones con Aprendizaje||
|**Aprendizaje Automático**|Decisiones con|mejora significativamente|Automático||
|**mejora la predicción de**|Aprendizaje Automático|la predicción de la|||
|**la demanda bibliográfica**|mejora la predicción de la|demanda bibliográfica en|||
||demanda bibliográfica en|Lima Metropolitana, 2026.|||



## _Sistema de Soporte de Decisiones_ 

|**en Lima Metropolitana,**<br>**2026?**|Lima Metropolitana,<br>2026.||||
|---|---|---|---|---|
|**2. Problemas Específicos**|2. Objetivos Específicos|2. Hipótesis Específicas:|Variable 2:|**2. Nivel de la**<br>**Investigación:**|
|**PE1: ¿En qué medida los**<br>**modelos de Aprendizaje**<br>**Automático incrementan la**<br>**exactitud de los pronósticos**<br>**de demanda en comparación**<br>**con los métodos**<br>**convencionales**<br>**de la editorial?**|OE1: Determinar en qué<br>medida los modelos de<br>Aprendizaje Automático<br>incrementan la exactitud de los<br>pronósticos de demanda<br>respecto a los métodos<br>convencionales.|HE1: Los modelos de<br>Aprendizaje Automático<br>presentan mayor exactitud en los<br>pronósticos que los métodos<br>convencionales utilizados por la<br>editorial.|VARIABLE DEPENDIENTE:<br>Predicción de la Demanda<br>Bibliográfica|**Aplicado - Explicativo**|
|**PE2: ¿En qué medida el**<br>**SSD basado en datos**<br>**históricos contribuye a la**|OE2: Evaluar en qué<br>medida el SSD basado en datos<br>históricos reduce el|HE2: El SSD reduce<br>significativamente los niveles de<br>sobrestock de||**3. Diseño de la**<br>**Investigación:**<br>**Preexperimental**|
|**reducción del sobrestock de**<br>**títulos bibliográficos?**|sobrestock de títulos<br>bibliográficos en la<br>editorial.|títulos bibliográficos en la<br>editorial.|||



pág. 56 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

|**PE3: ¿En qué medida la**<br>**predicción mediante**<br>**Aprendizaje Automático**<br>**disminuye la incidencia de**<br>**quiebre de stock en la**<br>**editorial?**|OE3: Determinar en qué<br>medida la predicción mediante<br>Aprendizaje Automático<br>disminuye la incidencia de<br>quiebre de<br>stock.|HE3: La predicción mediante<br>Aprendizaje Automático<br>disminuye significativamente la<br>incidencia de quiebre de<br>stock.||**4. Método: Hipotético-**<br>**deductivo**|
|---|---|---|---|---|
|**PE4: ¿En qué medida la**<br>**integración del SSD reduce**<br>**el tiempo de planificación de**<br>**tirajes y aumenta el**<br>**porcentaje de**<br>**decisiones editoriales**|OE4: Evaluar en qué medida la<br>integración del SSD reduce el<br>tiempo de planificación de<br>tirajes y aumenta el porcentaje<br>de|HE4: La integración del SSD<br>con Aprendizaje Automático<br>reduce significativamente el<br>tiempo de planificación de<br>tirajes y aumenta el||**5. Población:**<br>**~3 250 registros históricos de**<br>**ventas e inventarios (2022–**<br>**2025)**|
|**respaldadas por datos en la**<br>**editorial?**|decisiones editoriales<br>respaldadas por datos.|porcentaje de decisiones<br>editoriales respaldadas por<br>datos en la editorial.|||
|||||**6. Muestra:**<br>**1 280 registros (segmento**<br>**9–17 años)**|



pág. 57 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

**7. Tipo de Muestreo: No probabilístico intencional 8. Técnica de Recolección: Análisis documental 9. Instrumento de Recolección: Ficha de registro estructurada (28 campos)** 

_Anexo 5 Matriz de consistencia_ 

pág. 58 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

## **11.6. Anexo 06: Matriz de Variables (Operacionales)** 

## **Anexo 1-B: Matriz de Variables (Operacionalización)** 

**“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en Lima Metropolitana, 2026”** 

|**11.6. Anexo 06: Matriz de Variables (Operacionales)**|**11.6. Anexo 06: Matriz de Variables (Operacionales)**|**11.6. Anexo 06: Matriz de Variables (Operacionales)**|**11.6. Anexo 06: Matriz de Variables (Operacionales)**|**11.6. Anexo 06: Matriz de Variables (Operacionales)**|**11.6. Anexo 06: Matriz de Variables (Operacionales)**|**11.6. Anexo 06: Matriz de Variables (Operacionales)**|
|---|---|---|---|---|---|---|
|**Anexo 1-B: Matriz de Variables (Operacionalización)**<br>**“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en Lima**<br>**Metropolitana, 2026”**|||||||
|**Variable**|Tipo de<br>Variable Según<br>su<br>naturaleza|Operacionalización<br>Definición Conceptual|Operacionalización<br>Definición Operacional|Dimensiones (Sub-<br>Variables)|Indicador|**Escala de**<br>**Medición**|
|**VARIABLE**<br>**INDEPENDIENTE:**<br>**Sistema de Soporte a**<br>**Decisiones con**<br>**Aprendizaje**<br>**Automático**|Cuantitativa<br>/ Cualitativa<br>(mixta)|Conjunto integrado de<br>herramientas tecnológicas,<br>algoritmos de aprendizaje<br>automático y bases de datos<br>históricas que procesan|Se operacionaliza a través de<br>cuatro dimensiones: (1)<br>Algoritmos de Aprendizaje<br>Automático: tipo de<br>modelo, tiempo de|Algoritmos de<br>Aprendizaje<br>Automático|Tipo de modelo<br>implementado (LSTM,<br>XGBoost,<br>Random Forest)|**Cualitativa**<br>**nominal**|
|||||Algoritmos de<br>Aprendizaje<br>Automático|Número de variables|**Cuantitativa**<br>**discreta**|
|||información de demanda<br>bibliográfica para generar<br>predicciones precisas y<br>apoyar la toma de|procesamiento y división<br>entrenamiento/prueba;<br>(2) Calidad de los Datos:<br>porcentaje de registros||predictoras<br>utilizadas||



pág. 59 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

|||decisiones editoriales. De<br>acuerdo con Punia y<br>Shankar (2022), un DSS<br>basado en aprendizaje<br>automático combina<br>modelos predictivos con<br>interfaces de decisión para<br>transformar datos|completos, sin duplicados y<br>rango temporal cubierto; (3)<br>Registro y Trazabilidad:<br>fuente del dato, versión del<br>modelo y log de<br>ejecuciones; (4) Monitoreo<br>del Sistema:|Algoritmos de<br>Aprendizaje<br>Automático|División<br>entrenamiento /<br>prueba (%)|**Cuantitativa**<br>**de razón**|
|---|---|---|---|---|---|---|
|||||Calidad de los<br>Datos|Porcentaje de registros<br>completos sin<br>valores nulos (%)|**Cuantitativa**<br>**de razón**|
|||||Calidad de los<br>Datos|Porcentaje de<br>registros sin<br>duplicados (%)|**Cuantitativa**<br>**de razón**|
|||||Calidad de los<br>Datos|Rango temporal<br>cubierto por los|**Cuantitativa**<br>**de razón**|
|||históricos en conocimiento<br>accionable.|frecuencia de<br>reentrenamiento, alertas por<br>degradación y tiempo de<br>respuesta.||datos históricos<br>(años)||



pág. 60 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

|Cada indicador es|Registro y|Fuente del dato (base|**Cualitativa**|
|---|---|---|---|
|cuantificable directamente a|Trazabilidad|histórica, ERP o|**nominal**|
|partir de la configuración, las||registro||
|métricas de rendimiento||manual)||
|(logs) y la trazabilidad del||||
|sistema informático||||
|desarrollado.||||
||Registro y|Estado del sistema al|**Cualitativa**|
||Trazabilidad|momento de la|**ordinal**|
|||predicción||
|||(Producción /||
|||Desarrollo /||
|||Mantenimiento)||
||Registro y|Versión del|**Cualitativa**|
||Trazabilidad|modelo de ML|**nominal**|
|||utilizado||



pág. 61 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

|Registro y|Porcentaje de|**Cuantitativa**|
|---|---|---|
|Trazabilidad|predicciones|**de razón**|
||registradas en el||
||sistema (%)||
|Registro y|Completitud del log de|**Cuantitativa**|
|Trazabilidad|ejecuciones (% de|**de razón**|
||campos||
||registrados)||
|Monitoreo del|Frecuencia de|**Cuantitativa**|
|Sistema|reentrenamiento del|**de razón**|
||modelo||
||(veces/mes)||
|Monitoreo del|N° de alertas|**Cuantitativa**|
|Sistema|generadas por|**discreta**|



pág. 62 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

||||||degradación del<br>modelo||
|---|---|---|---|---|---|---|
|||||Monitoreo del<br>Sistema|Tiempo promedio de<br>respuesta del<br>sistema (segundos)|**Cuantitativa**<br>**de razón**|
|||||Monitoreo del<br>Sistema|N° de versiones<br>del modelo<br>documentadas|**Cuantitativa**<br>**discreta**|
|**VARIABLE**<br>**DEPENDIENTE:**<br>**Predicción de la**<br>**Demanda**<br>**Bibliográfica**|Cuantitativa|Proceso mediante el cual el<br>sistema estima con<br>anticipación la cantidad de<br>unidades<br>bibliográficas que|Se operacionaliza a través de<br>cuatro dimensiones<br>evaluadas en los 1 280<br>registros de<br>la ficha: (1) Exactitud:|Exactitud de la<br>Predicción|Error Absoluto<br>Medio — MAE|**Cuantitativa**<br>**de razón**|
|||||Exactitud de la<br>Predicción|Raíz del Error<br>Cuadrático Medio<br>— RMSE|**Cuantitativa**<br>**de razón**|



pág. 63 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

|||serán demandadas en un<br>período futuro, mediante el<br>análisis de patrones<br>históricos de ventas e<br>inventarios.<br>Según Arias (2023), la<br>predicción cuantitativa<br>permite identificar<br>tendencias y<br>estacionalidades en series<br>temporales, reduciendo la<br>incertidumbre en la|MAE, RMSE y MAPE<br>en escenarios PRE/POST;<br>(2)<br>Eficiencia: tiempo de<br>procesamiento y títulos<br>procesados por ejecución;<br>(3) Optimización del<br>inventario: reducción de<br>sobrestock y quiebre de<br>stock; (4) Apoyo a<br>decisiones: % de<br>recomendaciones|Exactitud de la<br>Predicción|Error Porcentual<br>Absoluto Medio<br>— MAPE (%)|**Cuantitativa**<br>**de razón**|
|---|---|---|---|---|---|---|
|||||Eficiencia de la<br>Predicción|Tiempo de<br>procesamiento por<br>predicción<br>(segundos)|**Cuantitativa**<br>**de razón**|
|||||Eficiencia de la<br>Predicción|Reducción del<br>error vs. método<br>convencional (%)|**Cuantitativa**<br>**de razón**|
|||||Eficiencia de la<br>Predicción|N° de títulos<br>procesados por<br>ejecución|**Cuantitativa**<br>**discreta**|



pág. 64 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

|planificación operativa.|implementadas y reducción|Optimización del|Reducción del nivel de|**Cuantitativa**|
|---|---|---|---|---|
||del tiempo de planificación.|Inventario|sobrestock (%)|**de razón**|
||Se aplica prueba t de Student||||
||para muestras relacionadas||||
||(p < 0.05).||||
|||Optimización del|Reducción del|**Cuantitativa**|
|||Inventario|nivel de quiebre de|**de razón**|
||||stock (%)||
|||Optimización del|Variación en la|**Índice de**|
|||Inventario|rotación de títulos|**rotación**|
||||bibliográficos||
|||**Apoyo a la Toma**|**N° de decisiones**|**Cuantitativa**|
|||**de Decisiones**|**editoriales**|**discreta**|
||||**respaldadas por el**||
||||**sistema**||



_Anexo 6 Matriz de variables_ 

pág. 65 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

_Sistema de Soporte de Decisiones_ 

## **11.7. Anexo 07: Prototipos** 

_Anexo 7 Prototipos_ 

pág. 66 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

pág. 67 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

pág. 68 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

pág. 69 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

pág. 70 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

pág. 71 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

pág. 72 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

pág. 73 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

## _Sistema de Soporte de Decisiones_ 

pág. 74 

Briceño Portillo, E; Davila Atoche, E; Huaman Sarabia, J ; Sanchez Marin, S 

