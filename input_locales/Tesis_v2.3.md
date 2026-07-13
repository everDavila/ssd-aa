## **FACULTAD DE INGENIERÍA** 

## **Carrera de Ingeniería de Sistemas** 

**“IMPLEMENTACIÓN DE UN SISTEMA DE SOPORTE A DECISIONES CON APRENDIZAJE AUTOMÁTICO PARA MEJORAR LA PREDICCIÓN DE LA DEMANDA BIBLIOGRÁFICA DE LA EDITORIAL AMBAR, 2026”** 

**Tesis para optar el título profesional de: Ingeniero(a) de Sistemas** 

**Autores:** 

Dávila Atoche Ever Antonio 

Najarro Angulo, Marino 

## **Asesor:** 

Mg. Ing. Nidia Rossela Solórzano Carrasco 

Código ORCID: 0009-0006-0722-6207 

**Lima – Perú** 

2026 

## **ÍNDICE DE CONTENIDO** 

INFORME DE SIMILITUD .................................................................................................. 6 DEDICATORIA .................................................................................................................... 7 AGRADECIMIENTO ........................................................................................................... 8 RESUMEN ............................................................................................................................ 9 ABSTRACT ......................................................................................................................... 10 CAPÍTULO I. INTRODUCCIÓN ........................................................................................... 11 1.1 Realidad problemática ................................................................................................... 11 1.2 Antecedentes de estudio ................................................................................................. 12 1.2.1 Antecedentes Internaciones .................................................................................... 12 1.2.2 Antecedentes Nacionales ........................................................................................ 14 1.3 Bases teóricas ................................................................................................................. 17 1.4 Definición de Variables y Dimensiones ........................................................................ 19 1.5 Formulación del problema ............................................................................................. 21 1.6 Objetivos ........................................................................................................................ 22 1.7 Hipótesis ........................................................................................................................ 22 1.8 Justificación ................................................................................................................... 23 CAPÍTULO II. METODOLOGÍA........................................................................................... 25 2.1 Tipo de investigación ..................................................................................................... 25 2.2 Diseño de investigación ................................................................................................. 25 2.3 Enfoque de investigación ............................................................................................... 25 2.4 Nivel de investigación.................................................................................................... 26 2.5 Población, muestra y muestreo ...................................................................................... 26 2.6 Técnicas e instrumentos de recolección de datos .......................................................... 27 2.7 Mediciones ..................................................................................................................... 32 2.8 Metodología de Desarrollo de software ......................................................................... 33 

2.9 Análisis de datos ............................................................................................................ 34 2.10 Aspectos éticos............................................................................................................. 37 CAPÍTULO III. RESULTADOS ............................................................................................. 39 3.1 Resultados descriptivos .................................................................................................. 39 3.2 Prueba de normalidad .................................................................................................... 43 3.3 Resultados inferenciales................................................................................................. 45 3.4 Contrastación de hipótesis ............................................................................................. 51 CAPÍTULO IV. DISCUSIÓN Y CONCLUSIONES .............................................................. 55 4.1 Discusión de resultados.................................................................................................. 55 4.2 Limitaciones ................................................................................................................... 58 4.3 Implicancias ................................................................................................................... 60 4.4 Conclusiones .................................................................................................................. 62 REFERENCIAS ....................................................................................................................... 64 ANEXOS ................................................................................................................................. 67 Anexo 1: Matriz de Consistencia ......................................................................................... 67 Anexo 2: Matriz de Variables (Operacionalización) ........................................................... 71 Anexo 3: Ficha de Registro.................................................................................................. 78 Anexo 4: Prototipos ............................................................................................................. 83 Anexo 5: Metodología de Desarrollo de software ............................................................... 88 Anexo 6: Población, muestra y muestreo ............................................................................ 90 

## **ÍNDICE DE TABLAS** 

Tabla 1  Juicio de expertos para la validación de la Ficha de Registro Documental ............... 28 Tabla 2 Resumen de procesamiento de casos para el indicador Tiempo de Procesamiento ... 29 Tabla 3  Prueba de Normalidad de Shapiro-Wilk para el indicador Tiempo de Procesamiento .................................................................................................................................................. 29 Tabla 4  Correlación de Rho de Spearman entre las dos mediciones del Tiempo de Procesamiento .......................................................................................................................... 30 Tabla 5  Resumen de procesamiento de casos para el indicador Post Mape ........................... 30 Tabla 6  Prueba de Normalidad de Shapiro-Wilk para el indicador Post Mape ...................... 31 Tabla 7  Correlación de Pearson entre las dos mediciones del Post Mape .............................. 32 Tabla 8  Estadísticos descriptivos de los indicadores de predicción y gestión de inventarios (N = 1,280) .................................................................................................................................... 39 Tabla 9  Resumen de procesamiento de casos para las variables PRE_MAPE y POST_MAPE .................................................................................................................................................. 43 Tabla 10  Prueba de normalidad de Kolmogorov-Smirnov para PRE_MAPE y POST_MAPE .................................................................................................................................................. 43 Tabla 11  Rangos con signo de la prueba de Wilcoxon para los cinco pares de indicadores según objetivo específico ......................................................................................................... 47 Tabla 12 Comparación del desempeño post-implementación por algoritmo (N = 1,280)....... 50 Tabla 13 Estadísticos de contraste de la prueba de Wilcoxon para los cinco pares de indicadores ............................................................................................................................... 51 Tabla 14 Aplicación de Scrum durante el desarrollo del Sistema de Soporte a Decisiones .... 88 Tabla 15  Aplicación de CRISP-DM en el desarrollo del modelo predictivo ......................... 88 Tabla 16  Relación entre Scrum y CRISP-DM en el desarrollo del Sistema de Soporte a Decisiones ................................................................................................................................ 89 Tabla 17  Población, muestra y muestreo ................................................................................ 90 

## **ÍNDICE DE FIGURAS** 

Figura 1  Boxplot comparativo del MAPE antes y después de la implementación del SSD con AA ............................................................................................................................................ 41 Figura 2  Gráfico de barras comparativo de sobrestock y quiebre de stock con intervalos de confianza del 95% .................................................................................................................... 42 Figura 3 _Histograma del MAPE antes de la implementación del Sistema de Soporte de Decisiones con AA_ ................................................................................................................... 44 Figura 4  Histograma del MAPE después de la implementación del SSD con AA................. 45 

## **INFORME DE SIMILITUD** 

## **DEDICATORIA** 

A nuestras familias, por su apoyo incondicional y por ser el pilar fundamental en nuestra 

formación profesional. 

## **AGRADECIMIENTO** 

Deseamos manifestar nuestro agradecimiento quienes hicieron posible el desarrollo de esta investigación. A nuestros asesores — quien nos acompañaron durante el curso de Tesis I y Trabajo de Investigación — por su paciencia, orientación metodológica y aportes críticos a lo largo de todo el proceso. A la editorial objeto de estudio, por facilitarnos el acceso a la información necesaria para la validación de nuestra propuesta. 

## **RESUMEN** 

La planificación empírica de tirajes en la industria editorial genera excesos de inventario y desabastecimiento comercial, afectando la rentabilidad. Frente a esta problemática, la presente investigación tuvo como objetivo determinar en qué medida la implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático mejora la predicción de la demanda bibliográfica en la editorial Ambar. El estudio correspondió a una investigación aplicada, con enfoque cuantitativo y diseño preexperimental. La población estuvo conformada por 1,280 registros históricos, extrayéndose una muestra intencional de 1,280 registros. Para la recolección de datos se empleó la técnica de análisis documental utilizando una ficha de registro estructurada. El sistema fue desarrollado en Python, integrando algoritmos predictivos como XGBoost y LSTM. Los resultados evidenciaron que el modelo automatizado redujo drásticamente el Error Porcentual Absoluto Medio (MAPE) de un 21.07 % a un 3.48 %, además de erradicar significativamente los niveles de sobrestock y quiebre de stock (p<.001). Se concluyó que la implementación del sistema basado en inteligencia artificial mejora significativamente la capacidad predictiva de la editorial, transformando la incertidumbre del mercado en decisiones de tiraje precisas que optimizan la cadena de suministro. 

**Palabras clave** : Aprendizaje automático; sistema de soporte a decisiones; predicción de la demanda bibliográfica; analítica predictiva; industria editorial. 

## **ABSTRACT** 

Empirical print run planning in the publishing industry generates excess inventory and commercial shortages, affecting profitability. Faced with this problem, this research aimed to determine to what extent the implementation of a Decision Support System with Machine Learning improves bibliographic demand forecasting at Editorial Ámbar. The study corresponded to applied research, with a quantitative approach and pre-experimental design. The population consisted of 1,280 historical records, extracting a purposive sample of 1,280 records. For data collection, the documentary analysis technique was used employing a structured record sheet. The system was developed in Python, integrating predictive algorithms such as XGBoost and LSTM. The results showed that the automated model drastically reduced the Mean Absolute Percentage Error (MAPE) from 21.07% to 3.48%, in addition to significantly eradicating overstock and stockout levels (p<.001). It was concluded that the implementation of the artificial intelligence-based system significantly improves the predictive capacity of the publisher, transforming market uncertainty into precise print run decisions that optimize the supply chain. 

**Keywords** : Machine Learning; Decision Support System; Bibliographic Demand Forecasting; Predictive Analytics; Publishing Industry. 

## **CAPÍTULO I. INTRODUCCIÓN** 

## **1.1 Realidad problemática** 

La industria editorial atraviesa una etapa de transición crítica, marcada por la convergencia entre la consolidación de los formatos digitales y la persistente relevancia del libro impreso. A pesar del auge de los libros electrónicos y el incremento del consumo de contenidos en dispositivos digitales, el libro físico se mantiene como un soporte fundamental de conexión sensorial y cognitiva, particularmente durante las etapas formativas del hábito lector. En este escenario, la supervivencia y competitividad de las organizaciones editoriales depende en gran medida de su capacidad para integrar tecnologías de la información que permitan una gestión inteligente de la producción física. 

La presente investigación se centra en el diseño e implementación de un Sistema de Soporte a las Decisiones (SSD) basado en técnicas de Aprendizaje Automático, orientado específicamente a la predicción de la demanda bibliográfica en la editorial Ambar. El problema central que motiva este estudio es la ineficiencia en la gestión de inventarios, manifestada en un desequilibrio persistente entre el sobrestock de títulos de baja rotación y el quiebre de stock de aquellos con alta demanda. Esta situación se ve agravada por una toma de decisiones basada predominantemente en la experiencia empírica y en herramientas de análisis rudimentarias, lo que limita la capacidad de respuesta ante un mercado juvenil — segmento de 9 a 17 años— cada vez más volátil y competitivo. 

A través de la aplicación de algoritmos predictivos, esta tesis busca transformar los datos históricos y las tendencias de consumo en conocimiento accionable. No se pretende únicamente optimizar los recursos financieros de la editorial, sino también proporcionar una base científica para la creación de contenidos que logren conectar eficazmente con las nuevas 

generaciones de lectores, fomentando el libro físico como un objeto de valor pedagógico y cultural en la era digital. 

Adicionalmente, la organización carece de una base de datos integrada que consolide información histórica de ventas, preferencias del lector y patrones de estacionalidad, lo que restringe el uso de herramientas analíticas avanzadas. La ausencia de un sistema automatizado de predicción obliga a mantener decisiones reactivas y empíricas, reduciendo la capacidad de la editorial para diseñar estrategias orientadas tanto a la rentabilidad como al fomento progresivo del hábito lector. 

De persistir esta situación, la editorial podría enfrentar un incremento sostenido del sobrestock, una disminución de su competitividad en el mercado y una menor capacidad para desarrollar propuestas editoriales que conecten eficazmente con los intereses del público infantil y juvenil. 

## **1.2 Antecedentes de estudio** 

## **1.2.1 Antecedentes Internaciones** 

Huber y Stuckenschmidt (2020), Alemania, en su investigación titulada “ _Daily retail demand forecasting using machine learning with emphasis on calendric special days_ ”, tuvieron como objetivo mejorar la precisión del pronóstico de demanda diaria incorporando días especiales del calendario como variables predictoras. La metodología adoptada fue cuantitativa y aplicada, con un diseño comparativo-experimental que utilizó series temporales de ventas diarias; aplicaron modelos de Aprendizaje Automático bajo el flujo CRISP-DM. Los resultados evidenciaron que dicho enfoque permite abordar patrones atípicos y generar pronósticos útiles para la planificación de la producción. 

Saha et al. (2022), Estados Unidos, en “ _Demand Forecasting of a Multinational Retail Company using Deep Learning Frameworks_ ”, propusieron modelos basados en LSTM y LightGBM bajo arquitectura CRISP-DM para predecir la demanda estacional y apoyar 

decisiones de compras y control de inventario. Los resultados confirman que los enfoques de Deep Learning y de boosting son eficaces para el pronóstico en contextos minoristas de alta variabilidad. 

Punia y Shankar (2022), India, en “ _Predictive analytics for demand forecasting: A deep learning-based decision support system_ ”, propusieron un modelo de analítica predictiva para generar pronósticos de demanda a corto, mediano y largo plazo, estructurado como un pipeline de DSS con Deep Learning dentro de un flujo CRISP-DM. Los autores concluyen que un DSS basado en Deep Learning fortalece significativamente la gestión de la demanda en organizaciones con grandes volúmenes de información histórica. 

Islek y Gunduz Oguducu (2017), Turquía, en “ _A Decision Support System for Demand Forecasting based on Classifier Ensemble_ ”, construyeron un esquema de pronóstico de demanda mediante combinación de clasificadores (MLP, Bayesian Network, SVM) y técnicas de ensamble como stacking. Los resultados reportan un MAPE de 12.7% en la mejor configuración evaluada, concluyendo que la combinación de modelos incrementa de manera consistente la precisión del pronóstico. 

Park, Lee y Doo (2020), Corea del Sur, en “ _A Study of the Demand Forecasting Model for Publishing Business using Business Analysis_ ”, identificaron los factores que inciden en la venta y devolución de libros, construyendo un modelo de pronóstico de demanda para una editorial a partir de cinco años de datos históricos (2012-2016). Los autores concluyen que el pronóstico automatizado mejora significativamente las decisiones de tiraje e inventario en el contexto editorial. 

Wang et al. (2019), Estados Unidos, en “ _Success in books: predicting book sales before publication_ ”, aplicaron el enfoque “ _Learning to Place_ ” basado en Aprendizaje Automático para predecir ventas de libros antes de su publicación. Los resultados demuestran que la casa editorial emerge como un factor altamente influyente en el desempeño comercial, y concluyen 

que es posible anticipar dicho desempeño mediante modelos predictivos antes del lanzamiento al mercado. 

Rinaldi et al. (2025), Europa, en “ _DSS4EX: A Decision Support System framework to explore AI pipelines for time series forecasting_ ”, propusieron un framework DSS para explorar, configurar y evaluar modelos de IA aplicados al pronóstico de series temporales. Los resultados evidencian que el framework facilita a usuarios no expertos la configuración de modelos y el análisis interactivo de resultados, concluyendo que los sistemas DSS orientados al forecasting promueven la adopción práctica del Aprendizaje Automático en organizaciones. Del conjunto de antecedentes revisados se desprenden vacíos que la presente investigación busca atender. Ninguno aborda específicamente el sector editorial de narrativa infantil-juvenil en economías emergentes de América Latina. Segundo, el modelo no incorpora un SSD con interfaz de decisión accesible para usuarios no técnicos ni contempla la comparación estadística PRE/POST mediante prueba Wilcoxon. 

## **1.2.2 Antecedentes Nacionales** 

En el contexto peruano, diversos estudios han demostrado la aplicabilidad del aprendizaje automático para apoyar la toma de decisiones y mejorar la capacidad predictiva en diferentes sectores productivos, educativos y organizacionales. Aunque la literatura nacional sobre predicción de demanda bibliográfica es limitada, existen investigaciones cuyos aportes metodológicos constituyen una base importante para el desarrollo del presente estudio. 

Mamani Rodríguez (2022), en su investigación “Proceso de machine learning para determinar la demanda social de puestos de empleo de profesionales de TI”, publicada en la revista Industrial Data de la Universidad Nacional Mayor de San Marcos, propuso un proceso basado en técnicas de aprendizaje automático para analizar y predecir la demanda laboral de profesionales del área de Tecnologías de Información. La investigación empleó modelos de 

clasificación y minería de datos para procesar grandes volúmenes de información provenientes de ofertas laborales, permitiendo identificar tendencias y necesidades del mercado. Los resultados evidenciaron que la incorporación de algoritmos de aprendizaje automático incrementó la precisión en la identificación de perfiles profesionales demandados, facilitando la toma de decisiones estratégicas en instituciones académicas y organizaciones. Este estudio constituye un antecedente relevante para la presente investigación, debido a que demuestra cómo el aprendizaje automático puede utilizarse para realizar predicciones que apoyen procesos de planificación y toma de decisiones. 

Posteriormente, Chambi Condori (2023), en el artículo “Segmentación de mercado: Machine Learning en marketing en contextos de COVID-19”, publicado también en Industrial Data, desarrolló un modelo de segmentación de clientes mediante algoritmos de aprendizaje automático para mejorar la toma de decisiones comerciales en escenarios de alta incertidumbre. El estudio evidenció que los modelos inteligentes permitieron identificar patrones de comportamiento de los consumidores con mayor precisión que los métodos tradicionales, facilitando estrategias comerciales más eficientes. Los hallazgos resaltan el potencial del aprendizaje automático como herramienta de apoyo para la gestión empresarial, aspecto que guarda relación con la presente investigación al emplear modelos predictivos para optimizar la planificación de la demanda bibliográfica. 

Por su parte, Salas y Caldas (2024), en la investigación “Predicting Undergraduate Academic Performance in a Leading Peruvian University: A Machine Learning Approach”, publicada por la Pontificia Universidad Católica del Perú, evaluaron distintos algoritmos de aprendizaje automático para predecir el rendimiento académico universitario. Mediante el análisis de múltiples variables académicas y socioeconómicas, compararon diferentes modelos 

predictivos, identificando aquellos con mayor capacidad de generalización y exactitud. Los resultados demostraron que los modelos de aprendizaje automático alcanzaron niveles elevados de precisión predictiva, proporcionando información útil para apoyar la toma de decisiones institucionales. Este trabajo constituye un antecedente importante porque evidencia la efectividad del aprendizaje automático en problemas de predicción utilizando datos históricos, enfoque metodológico similar al empleado en la presente investigación. 

Asimismo, Albarracín Manrique (2025), en el artículo “Predicting Employee Turnover Using Applied Machine Learning”, publicado en la revista Ingeniería Industrial, desarrolló modelos predictivos orientados a estimar la rotación de personal mediante técnicas de aprendizaje automático. La investigación comparó diferentes algoritmos supervisados para identificar el modelo con mejor desempeño predictivo, concluyendo que el uso de inteligencia artificial mejora significativamente la capacidad de anticipar eventos organizacionales complejos. Los resultados destacan la importancia de seleccionar modelos predictivos adecuados para apoyar decisiones estratégicas, contribuyendo conceptualmente al presente estudio en la selección y evaluación de algoritmos aplicados a la predicción de demanda. 

De igual manera, el artículo “Artificial Intelligence and Multimodal Diagnostic Approaches in Cardiovascular Disease” (2025), publicado en Archivos Peruanos de Cardiología y Cirugía Cardiovascular, analiza la incorporación de inteligencia artificial como herramienta de apoyo para la toma de decisiones clínicas mediante el procesamiento de grandes volúmenes de información. Los autores concluyen que los modelos inteligentes incrementan la precisión diagnóstica y fortalecen los procesos de decisión en escenarios complejos. Aunque el contexto corresponde al ámbito de la salud, la investigación evidencia el valor de los sistemas 

inteligentes como soporte para la toma de decisiones basada en datos, principio que también sustenta el desarrollo del Sistema de Soporte a Decisiones propuesto en esta tesis. 

Finalmente, Pino-Vargas et al. (2025), en el estudio “Identification of Vulnerable Areas to Flash Floods Using Weighted Sum Analysis and Unsupervised Machine Learning”, publicado en Scientia Agropecuaria, aplicaron técnicas de aprendizaje automático no supervisado para identificar zonas vulnerables mediante el análisis integrado de múltiples variables geográficas. Los resultados demostraron que los algoritmos permitieron identificar patrones complejos imposibles de detectar mediante métodos tradicionales, mejorando la capacidad predictiva para la gestión del riesgo. Aunque el problema abordado pertenece al ámbito ambiental, el estudio confirma la utilidad del aprendizaje automático para apoyar decisiones basadas en el análisis de datos, aspecto directamente relacionado con la implementación de un Sistema de Soporte a Decisiones para la predicción de la demanda bibliográfica. 

## **1.3 Bases teóricas** 

El presente estudio aborda los fundamentos teóricos del Sistema de Soporte a las Decisiones, la predicción de la demanda y el uso del Aprendizaje Automático como herramienta de apoyo a la toma de decisiones organizacionales. 

Desde una perspectiva metodológica, un Sistema de Soporte a las Decisiones se concibe como un conjunto organizado de recursos tecnológicos y analíticos que facilita la toma de decisiones en contextos complejos, caracterizados por la incertidumbre y el gran volumen de información disponible. De acuerdo con Hernández, Fernández y Baptista (2014), el uso de sistemas basados en datos permite transformar información dispersa en conocimiento útil para explicar y predecir fenómenos observables dentro de una organización. 

En el ámbito de la gestión de la demanda, la predicción se fundamenta en el análisis sistemático de datos históricos con el propósito de anticipar comportamientos futuros. Arias (2023) sostiene que el análisis cuantitativo permite identificar patrones, tendencias y relaciones entre variables, lo que resulta esencial cuando se busca reducir la incertidumbre en procesos de planificación y control operativo. 

El Aprendizaje Automático se integra como una herramienta metodológica que potencia el análisis cuantitativo, al permitir el procesamiento de grandes volúmenes de datos y la generación de modelos predictivos de alta precisión. Sabino (2018) señala que el valor de los modelos analíticos radica en su capacidad para explicar relaciones causales y sustentar la toma de decisiones basada en evidencia. 

Lenguaje de Programación. Constituye el medio a través del cual se implementan los algoritmos y las reglas de negocio del sistema. En el presente estudio, se emplea Python como lenguaje principal de implementación, dado que concentra el ecosistema más consolidado de librerías para ciencia de datos y Aprendizaje Automático. Según Sommerville (2016), los lenguajes de programación permiten expresar modelos lógicos y matemáticos de manera estructurada, facilitando la construcción de aplicaciones capaces de procesar grandes volúmenes de datos. Específicamente, se utilizan las librerías Pandas para la manipulación y limpieza del dataset, Scikit-learn para los modelos XGBoost y Random Forest, y TensorFlow/Keras para la arquitectura LSTM orientada a series temporales. 

Base de Datos. Representa el núcleo de almacenamiento y gestión de la información del sistema. Connolly y Begg (2015) definen las bases de datos como colecciones organizadas de datos relacionados lógicamente, diseñadas para satisfacer las necesidades de información de una organización de manera eficiente y confiable. En el SSD propuesto, los datos históricos de ventas e inventarios —originalmente dispersos en hojas de cálculo Excel— son 

consolidados en una base de datos estructurada que permite la ingesta directa de los 1 280 registros de la muestra hacia el pipeline de procesamiento en Python. 

Arquitectura de Software. Establece la estructura general del sistema y la forma en que sus componentes interactúan entre sí. Bass, Clements y Kazman (2013) sostienen que una arquitectura bien definida facilita la escalabilidad, el mantenimiento y la reutilización del software a lo largo de su ciclo de vida. El SSD propuesto sigue la arquitectura del pipeline CRISP-DM, que organiza el flujo en seis fases: comprensión del negocio, comprensión de los datos, preparación de los datos, modelado, evaluación e implementación. 

## **Industria Editorial y Gestión de la Demanda Bibliográfica.** Constituye el contexto 

sectorial en el que se enmarca la variable dependiente del presente estudio. La industria editorial peruana se caracteriza por operar predominantemente bajo esquemas de gestión empírica, donde las decisiones de tiraje y reposición de inventario dependen del criterio subjetivo del editor antes que de datos históricos sistematizados. Según la International Publishers Association (2022), los mercados editoriales de economías emergentes de América Latina enfrentan una doble presión estructural: la volatilidad de la demanda lectora — especialmente en el segmento infantil y juvenil— y la limitada capacidad financiera para absorber pérdidas por sobrestock o quiebre de stock. En el caso peruano, esta situación se agrava por la concentración del mercado en ferias del libro como canal principal de comercialización, lo que genera patrones de demanda marcadamente estacionales y difíciles de anticipar mediante métodos convencionales. Esta naturaleza del sector justifica la necesidad de implementar sistemas de soporte a decisiones con capacidad predictiva, capaces de transformar la incertidumbre del mercado bibliográfico en información accionable para la planificación editorial. 

## **1.4 Definición de Variables y Dimensiones** 

Para el presente estudio, se han definido operativamente dos variables principales: 

Variable Independiente (VI): Sistema de Soporte a Decisiones con Aprendizaje Automático (SSD con AA). Se define conceptualmente como una solución tecnológica que integra algoritmos de Machine Learning para procesar datos históricos y generar pronósticos que apoyen la toma de decisiones empresariales. Se estructura en tres dimensiones técnicas: 

Dimensión 1: Gestión de Datos. Comprende los procesos de extracción, limpieza, transformación y consolidación de los registros históricos de ventas e inventarios de la editorial, garantizando la calidad e integridad de la información que alimenta los modelos predictivos. 

Dimensión 2: Modelado Predictivo. Abarca la selección, entrenamiento, evaluación y comparación de los algoritmos de aprendizaje automático implementados (XGBoost, Random Forest y LSTM), cuyo desempeño se mide mediante los indicadores MAE, RMSE, MAPE y tiempo de procesamiento. 

Dimensión 3: Interfaz de Usuario. Comprende el componente visual e interactivo del SSD mediante el cual los usuarios finales —en este caso, el personal administrativo y gerencial de la Editorial Ámbar— acceden a los pronósticos generados por los modelos de aprendizaje automático y toman decisiones operativas basadas en ellos. Su inclusión como dimensión técnica de la VI se justifica porque un sistema de soporte a decisiones no se limita al motor analítico: requiere una capa de presentación que garantice la interpretabilidad de los resultados y la usabilidad del sistema por parte de usuarios no técnicos. De acuerdo con Bass, Clements y Kazman (2013), la arquitectura de software incluye la interfaz como componente estructural que determina la efectividad con que el sistema cumple su propósito funcional. En el presente estudio, esta dimensión se operacionaliza a través del dashboard desarrollado en Streamlit, que centraliza la visualización de predicciones, alertas de inventario y métricas de desempeño en tiempo real. 

Variable Dependiente (VD): Predicción de la demanda bibliográfica. Se define conceptualmente como la estimación anticipada de la cantidad de ejemplares que el mercado requerirá para un título literario específico. Su mejora se evalúa mediante cuatro dimensiones cuantitativas: 

D1: Exactitud del pronóstico (MAPE). Mide el porcentaje de error entre la demanda real y la predicha, siendo el indicador principal para evaluar la precisión del modelo. 

D2: Nivel de Sobrestock. Cuantifica el exceso de inventario generado por una sobreestimación de la demanda, expresado como porcentaje respecto al total de unidades producidas. 

D3: Incidencia de Quiebre de Stock. Mide la frecuencia con que la editorial no cuenta con ejemplares disponibles ante una demanda real superior a la predicha, expresada como porcentaje. 

D4: Tiempo de procesamiento. Registra el tiempo requerido por el sistema para generar un pronóstico completo desde la ingesta de datos hasta la presentación de resultados en el dashboard, expresado en segundos. 

## **1.5 Formulación del problema** 

Problema general: ¿En qué medida la implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático mejora la predicción de la demanda bibliográfica en la editorial Ambar, 2026? 

Problemas específicos: 

PE1 (D1): ¿En qué medida los modelos de Aprendizaje Automático incrementan la exactitud de los pronósticos de demanda (MAPE) en comparación con los métodos convencionales? PE2 (D2): ¿En qué medida el Sistema de Soporte de Decisiones con Aprendizaje Automático contribuye a la reducción del nivel de sobrestock de títulos bibliográficos? 

PE3 (D3): ¿En qué medida la predicción mediante Aprendizaje Automático disminuye la 

incidencia de quiebre de stock en la editorial? 

PE4 (D4): ¿En qué medida la integración del Sistema de Soporte de Decisiones con Aprendizaje Automático reduce el tiempo de procesamiento en la toma de decisiones editoriales? 

## **1.6 Objetivos** 

Objetivo general: Determinar en qué medida la implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático mejora la predicción de la demanda bibliográfica en la editorial Ambar, 2026. 

Objetivos específicos: 

OE1: Determinar en qué medida los modelos de Aprendizaje Automático incrementan la exactitud de los pronósticos de demanda (MAPE) respecto a los métodos convencionales. OE2: Evaluar en qué medida el Sistema de Soporte de Decisiones reduce el nivel de sobrestock de títulos bibliográficos en la editorial. 

OE3: Determinar en qué medida la predicción mediante Aprendizaje Automático disminuye la incidencia de quiebre de stock. 

OE4: Evaluar en qué medida la integración del Sistema de Soporte de Decisiones reduce el tiempo de procesamiento en la planificación de tirajes. 

## **1.7 Hipótesis** 

**Hipótesis general:** La implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático mejora significativamente la predicción de la demanda bibliográfica en la editorial Ambar, 2026. 

## **Hipótesis específicas:** 

HE1: Los modelos de Aprendizaje Automático incrementan significativamente la exactitud 

en los pronósticos de demanda (MAPE) respecto a los métodos convencionales. 

HE2: El Sistema de Soporte de Decisiones con Aprendizaje Automático reduce significativamente los niveles de sobrestock de títulos bibliográficos. 

HE3: La predicción mediante Aprendizaje Automático disminuye significativamente la incidencia de quiebre de stock. 

HE4: La integración del Sistema de Soporte de Decisiones con Aprendizaje Automático reduce significativamente el tiempo de procesamiento en la planificación de tirajes. 

La formulación de hipótesis causales en el presente estudio se sustenta 

metodológicamente en la naturaleza del diseño preexperimental adoptado (G: O₁ → X → O₂). Si bien este diseño no incorpora un grupo control paralelo, permite establecer una relación de causalidad direccional entre la variable independiente (implementación del SSD con AA) y los cambios observados en la variable dependiente (indicadores de predicción de la demanda bibliográfica), dado que la intervención es la única modificación sistemática introducida entre la medición pre-test y el post-test. Hernández et al. (2014) señalan que los diseños preexperimentales son pertinentes para estudios explicativos cuando el investigador controla la aplicación del estímulo y mide su efecto sobre una misma unidad de análisis antes y después de la intervención. En este contexto, las hipótesis formuladas no afirman causalidad absoluta, sino que postulan una mejora significativa atribuible predominantemente a la intervención tecnológica, lo cual es contrastable estadísticamente mediante la prueba de Wilcoxon aplicada en 3.4. 

## **1.8 Justificación** 

Justificación Teórica: La investigación contribuye al fortalecimiento del conocimiento científico sobre la aplicación de Sistemas de Soporte a las Decisiones en el ámbito editorial, 

demostrando empíricamente cómo los modelos predictivos pueden resolver problemas de incertidumbre. 

Justificación Práctica y Económica: En el plano práctico, el estudio ofrece una solución tecnológica que impacta directamente en la rentabilidad de la editorial. Al reducir el sobrestock, se minimizan los costos de almacenamiento (bodegaje) y la depreciación del inventario. Paralelamente, al disminuir el quiebre de stock, se maximizan los ingresos por ventas al asegurar que los títulos exitosos estén disponibles cuando el mercado juvenil los requiere. 

Justificación Metodológica y Social: Metodológicamente, la investigación aporta un procedimiento estructurado (CRISP-DM) aplicable a otras Pymes del sector. A nivel social, fomenta la digitalización de la industria editorial peruana, un sector tradicionalmente rezagado tecnológicamente, apoyando de manera indirecta a la difusión cultural al hacer económicamente sostenible la producción de literatura infantil y juvenil. 

## **CAPÍTULO II. METODOLOGÍA** 

## **2.1 Tipo de investigación** 

El presente estudio se enmarca en la investigación aplicada, dado que surge de una necesidad específica identificada en el contexto real de la gestión editorial en la editorial Ambar, orientada a implementar una solución tecnológica concreta. Hernández et al. (2014) señalan que la investigación aplicada se caracteriza por emplear el conocimiento científico con el propósito de resolver problemas específicos del entorno real. 

## **2.2 Diseño de investigación** 

El diseño de la investigación es experimental de tipo pre-experimental. Se trabaja con un único grupo de estudio al cual se le aplica una medición previa (pre-test), la intervención del sistema y una medición posterior (post-test). El diseño se representa con el siguiente gráfico metodológico: G: O₁ → X → O₂. Donde G: Grupo de estudio (Registros históricos de demanda bibliográfica). O₁: Observación previa (Medición de indicadores con el método convencional: MAPE_Antes, Sobrestock_Antes, etc.). X: Intervención (Implementación del Sistema de Soporte a Decisiones con Aprendizaje Automático). O₂: Observación posterior (Medición de indicadores con el uso del Sistema de Soporte de Decisiones: MAPE_Después, Sobrestock_Después, etc.). 

## **2.3 Enfoque de investigación** 

La investigación adopta un enfoque cuantitativo, fundamentado en la recolección y el análisis de datos numéricos que permiten medir variables y analizar patrones. Arias (2023) indica que el enfoque cuantitativo se fundamenta en la recolección y el análisis de datos 

numéricos, lo que permite medir variables, analizar patrones y establecer relaciones objetivas y verificables entre los fenómenos estudiados. 

## **2.4 Nivel de investigación** 

El nivel de la investigación es Explicativo. A diferencia de los estudios meramente correlacionales, esta investigación busca establecer y explicar una relación de causalidad. Es decir, se busca demostrar estadísticamente que la manipulación de la variable independiente (la inserción del Sistema de Soporte de Decisiones con AA) es la causa directa que genera los efectos observados en la variable dependiente (las mejoras en los indicadores de predicción de la demanda). 

## **2.5 Población, muestra y muestreo** 

## **Población** 

La población estuvo conformada por los registros históricos de ventas bibliográficas de la Editorial Ámbar correspondientes al segmento de lectores de 9 a 17 años, registrados durante el período comprendido entre los años 2022 y 2025. Cada registro contiene información relacionada con el comportamiento de la demanda bibliográfica, constituyendo la unidad de análisis de la presente investigación. 

La población estuvo integrada por un total de 1 280 registros históricos, los cuales fueron utilizados para el entrenamiento, validación y evaluación de los modelos de aprendizaje automático implementados en el Sistema de Soporte a Decisiones. 

## **Muestra** 

La muestra estuvo conformada por los 1 280 registros históricos correspondientes al segmento de lectores de 9 a 17 años durante el período 2022–2025, debido a que todos los registros que cumplían los criterios establecidos fueron considerados para el desarrollo de la investigación. 

Adicionalmente, para la evaluación de la confiabilidad del instrumento mediante el método Test–Retest se seleccionó una muestra piloto de 30 registros históricos, utilizada únicamente para verificar la estabilidad temporal del instrumento. 

## **Muestreo** 

Se empleó un muestreo no probabilístico por criterio (intencional), debido a que los registros fueron seleccionados considerando criterios previamente establecidos en función de los objetivos de la investigación: pertenecer al segmento de lectores de 9 a 17 años y corresponder al período histórico comprendido entre los años 2022 y 2025. 

La selección de estos registros permitió analizar el comportamiento de la demanda bibliográfica del segmento objetivo sobre el cual se implementó el Sistema de Soporte a Decisiones con Aprendizaje Automático, garantizando la pertinencia de la información utilizada para el entrenamiento y evaluación de los modelos predictivos. 

La  Tabla 17 presenta el resumen de la población, muestra y tipo de muestreo considerados en la presente investigación. 

## **2.6 Técnicas e instrumentos de recolección de datos** 

La técnica principal de recolección de datos fue el análisis documental y estadístico, la cual permitió identificar, extraer, organizar y consolidar de manera sistemática la información proveniente de los registros históricos de ventas e inventarios de la editorial. Como instrumento de recolección se empleó la Ficha de Registro Documental y Estadístico, estructurada en formato de base de datos tabular mediante Microsoft Excel (véase Anexo 1-C: Ficha de Registro), lo que facilitó la estandarización de las variables cuantitativas requeridas para el entrenamiento, validación y evaluación de los algoritmos de aprendizaje automático. 

La validez del instrumento se estableció mediante juicio de expertos, quienes evaluaron la pertinencia, claridad, coherencia y suficiencia de cada uno de los campos que conforman la Ficha de Registro Documental y Estadístico, verificando que estos representaran adecuadamente las variables e indicadores definidos en la investigación. 

La  Tabla 1 presenta el resumen de los expertos que participaron en el proceso de validación del instrumento. 

**Tabla 1** _Juicio de expertos para la validación de la Ficha de Registro Documental_ 

|**N°**|**Apellidos y nombres**|**Grado académico**|**Opinión**|
|---|---|---|---|
|**1**|Cris Sanchez Rios|Magister|Aplicable|
|**2**|Jose Rosas Cabeza|Magister|Aplicable|
|**3**|Yarul Masias Donayre|Magister|Aplicable|



Por su parte, la confiabilidad del instrumento y del proceso de extracción automatizada 

de datos se determinó mediante el método de estabilidad temporal (test-retest). Para ello, se aplicó una prueba piloto sobre una muestra de 30 registros históricos, realizando dos procesos independientes de extracción de información a partir de los registros operativos del sistema en dos momentos diferentes (T1 y T2). Posteriormente, los resultados fueron sometidos al análisis estadístico correspondiente, desarrollado en el Capítulo III mediante las pruebas de ShapiroWilk y Wilcoxon, evidenciándose una consistencia total entre ambas mediciones en indicadores clave, como el Tiempo de Procesamiento y el POST MAPE. Estos resultados confirmaron la estabilidad del proceso de recolección y la ausencia de variaciones atribuibles al procedimiento de extracción, garantizando así la confiabilidad del instrumento y la calidad de los datos utilizados en la investigación. 

**Tabla 2** 

_Resumen de procesamiento de casos para el indicador Tiempo de Procesamiento_ 

|||Casos||
|---|---|---|---|
||Válido|Perdidos|Total|
||N<br>Porcentaje|N<br>Porcentaje|N<br>Porcentaje|
|TIEMPO_T1|30<br>100,0%|0<br>0,0%|30<br>100,0%|
|TIEMPO_T2|30<br>100,0%|0<br>0,0%|30<br>100,0%|



_**Nota.**_ N = 30 registros de la muestra piloto. 

## **Interpretación:** 

La Tabla 1 presenta el resumen de procesamiento de casos correspondiente a la muestra piloto de 30 registros utilizada para evaluar la confiabilidad del indicador Tiempo de Procesamiento. Se observa que la totalidad de los registros fueron procesados de manera exitosa en ambas aplicaciones, alcanzando un 100% de validez tanto para la primera medición (TIEMPO_T1) como para la segunda (TIEMPO_T2), sin registros perdidos en ningún caso. 

## **Tabla 3** 

_Prueba de Normalidad de Shapiro-Wilk para el indicador Tiempo de Procesamiento_ 

||Shapiro-Wilk|
|---|---|
||Estadístico<br>gl<br>Sig.|
|TIEMPO_T1|,902<br>30<br>,009|
|TIEMPO_T2|,906<br>30<br>,012|



## **Interpretación:** 

Se aplicó la prueba de normalidad Shapiro-Wilk debido a que la muestra estuvo conformada por 30 registros históricos. Los resultados evidenciaron valores de significancia inferiores a .05 tanto para TIEMPO_T1 (W = .902; p = .009) como para TIEMPO_T2 (W = .906; p = .012), indicando que los datos **no presentan distribución normal** . 

**Tabla 4** 

_Correlación de Rho de Spearman entre las dos mediciones del Tiempo de Procesamiento_ 

|_Procesamiento_|||
|---|---|---|
|||TIEMPO_T1<br>TIEMPO_T2|
|Rho de Spearman|TIEMPO_T1|Coeficiente de correlación<br>1,000<br>,998**|
|||Sig. (bilateral)<br>.<br><,001|
|||N<br>30<br>30|
||TIEMPO_T2|Coeficiente de correlación<br>,998**<br>1,000|
|||Sig. (bilateral)<br><,001<br>.|
|||N<br>30<br>30|



**. La correlación es significativa en el nivel 0,01 (bilateral). 

## **Interpretación:** 

La estabilidad temporal del instrumento fue evaluada mediante el método test-retest aplicado al indicador Tiempo de Procesamiento. Previamente, se analizó la normalidad de los datos utilizando la prueba de Shapiro-Wilk, obteniéndose valores de significancia inferiores a .05 tanto para la primera medición TIEMPO_T1 (W = .902; p = .009) como para la segunda medición TIEMPO_T2 (W = .906; p = .012), evidenciando que los datos no presentan distribución normal. En función de ello, se empleó el coeficiente de correlación Rho de Spearman, obteniéndose una correlación de ρ = .998 con una significancia bilateral de p < .001. Este resultado evidencia una correlación positiva muy alta entre ambas mediciones, demostrando una elevada estabilidad temporal y adecuada confiabilidad del instrumento para la recolección de datos en la presente investigación. 

## **Confiabilidad del Indicador POST MAPE (%)** 

**Tabla 5** 

_Resumen de procesamiento de casos para el indicador Post Mape_ 

|||Casos||
|---|---|---|---|
||Válido|Perdidos|Total|
||N<br>Porcentaje|N<br>Porcentaje|N<br>Porcentaje|
|POST_MAPE_T1|30<br>100,0%|0<br>0,0%|30<br>100,0%|
|POST_MAPE_T2|30<br>100,0%|0<br>0,0%|30<br>100,0%|



## _**Nota.**_ MAPE = Error Porcentual Absoluto Medio. 

## **Interpretación:** 

La Tabla 4 presenta el resumen de procesamiento de casos correspondiente a la muestra 

piloto conformada por 30 registros históricos utilizados para evaluar la confiabilidad del indicador Post Mape. Se observa que la totalidad de los registros fueron procesados correctamente tanto en la primera medición (POST_MAPE_T1) como en la segunda medición (POST_MAPE_T2), alcanzando un 100% de casos válidos y sin presentarse datos perdidos durante el análisis estadístico realizado en SPSS. 

## **Tabla 6** 

_Prueba de Normalidad de Shapiro-Wilk para el indicador Post Mape_ 

||Shapiro-Wilk|
|---|---|
||Estadístico<br>gl<br>Sig.|
|POST_MAPE_T1|,981<br>30<br>,855|
|POST_MAPE_T2|,982<br>30<br>,873|



_**Nota.**_ α = .05. H₀: Los datos provienen de una distribución normal. 

## **Interpretación:** 

La prueba de normalidad Shapiro-Wilk fue aplicada debido a que la muestra piloto estuvo conformada por 30 registros históricos. Los resultados evidenciaron valores de significancia de .855 para POST_MAPE_T1 y .873 para POST_MAPE_T2, siendo ambos superiores al nivel de significancia de .05. Esto indica que los datos presentan una **distribución normal** , permitiendo el uso de pruebas paramétricas para el análisis de confiabilidad del instrumento. 

**Tabla 7** 

_Correlación de Pearson entre las dos mediciones del Post Mape_ 

||POST_MAPE_T1<br>POST_MAPE_T2|
|---|---|
|POST_MAPE_T1|Correlación de<br>1<br>,999**|
||Pearson|
||Sig. (bilateral)<br><,001|
||N<br>30<br>30|
|POST_MAPE_T2|Correlación de<br>,999**<br>1|
||Pearson|
||Sig.(bilateral)<br><,001|
||N<br>30<br>30|



**. La correlación es significativa en el nivel 0,01 (bilateral). 

## **Interpretación:** 

La estabilidad temporal del instrumento se evaluó mediante el método test-retest. Previamente, se analizó la normalidad de los puntajes de ambas aplicaciones mediante la prueba de Shapiro-Wilk, observándose distribución normal tanto en el test (W = .981; p = .855) como en el retest (W = .982; p = .873). En función de ello, se empleó el coeficiente de correlación de Pearson, obteniéndose una correlación de r = .999, con una significancia de p = <.001. Este resultado evidencia una muy alta estabilidad temporal del instrumento, lo que garantiza que la extracción automatizada del indicador POST MAPE desde los logs del motor de aprendizaje automático produce resultados consistentes y replicables en mediciones repetidas, sin introducir variabilidad significativa atribuible al momento de la extracción. 

## **2.7 Mediciones** 

Las mediciones del estudio se estructuraron bajo el diseño pre-experimental en dos fases claramente diferenciadas: la medición pre-test y la medición post-test. En el pre-test, los indicadores de Exactitud del Pronóstico (MAPE), Sobrestock, Quiebre de Stock y Tiempo de Procesamiento fueron extraídos y calculados a partir del método empírico de planificación 

tradicional de la editorial, recabando los reportes manuales en hojas de cálculo. En el post-test, estas mismas métricas fueron extraídas de forma objetiva y automatizada directamente por el dashboard del Sistema de Soporte a las Decisiones (SSD) tras ejecutar el procesamiento de la data mediante los algoritmos de Machine Learning. Este flujo garantizó la comparabilidad cuantitativa directa entre el escenario "Sin Sistema" y "Con Sistema". 

## **2.8 Metodología de Desarrollo de software** 

El desarrollo del Sistema de Soporte a Decisiones con Aprendizaje Automático para la predicción de la demanda bibliográfica se realizó mediante la combinación de dos metodologías complementarias: Scrum para la gestión del proyecto de software y CRISP-DM (Cross Industry Standard Process for Data Mining) para el desarrollo del componente analítico basado en aprendizaje automático. 

La adopción de Scrum permitió gestionar el proyecto de manera ágil e incremental, facilitando la planificación, seguimiento y entrega continua de funcionalidades durante todo el proceso de desarrollo. Esta metodología resultó adecuada debido a que los requerimientos funcionales y los modelos predictivos evolucionaron conforme se analizaban los datos históricos de ventas de la Editorial Ámbar, siendo necesario realizar ajustes continuos en los algoritmos, interfaces y procesos de entrenamiento. Según Schwaber y Sutherland (2020), Scrum favorece la inspección permanente, la adaptación al cambio y la entrega incremental de valor mediante ciclos cortos de desarrollo denominados Sprints. 

De forma paralela, el procesamiento de los datos históricos y la construcción de los modelos predictivos siguieron la metodología CRISP-DM, considerada uno de los estándares internacionales más utilizados en proyectos de minería de datos y aprendizaje automático. Esta metodología permitió estructurar de manera ordenada las actividades relacionadas con la 

comprensión del problema, preparación del conjunto de datos, entrenamiento de los modelos, evaluación estadística y despliegue del sistema predictivo. 

En consecuencia, ambas metodologías se complementaron durante el desarrollo del proyecto: Scrum administró el ciclo de vida del software, mientras que CRISP-DM organizó el proceso analítico del modelo de inteligencia artificial, permitiendo obtener una solución tecnológica robusta, escalable y alineada con los objetivos de la investigación. 

La Tabla 12 presenta la planificación de los Sprints ejecutados durante el desarrollo del Sistema de Soporte a Decisiones, especificando los objetivos, actividades desarrolladas y entregables obtenidos en cada iteración. 

Asimismo, la Tabla 13 describe la aplicación de las fases de la metodología CRISPDM dentro de la presente investigación, detallando las actividades realizadas desde la comprensión del problema hasta el despliegue del modelo predictivo. 

Finalmente, la Tabla 14 muestra la integración entre las metodologías Scrum y CRISPDM, evidenciando cómo ambas metodologías se complementaron para gestionar de manera simultánea el desarrollo del software y el proceso analítico basado en aprendizaje automático. 

## **2.9 Análisis de datos** 

El análisis de datos se desarrolló mediante un procedimiento sistemático orientado a garantizar la calidad, confiabilidad y validez de los resultados obtenidos durante la implementación del Sistema de Soporte a Decisiones con Aprendizaje Automático para la predicción de la demanda bibliográfica de la Editorial Ámbar. 

En una primera etapa se consolidó una base de datos conformada por 1 280 registros históricos de ventas, correspondientes al período comprendido entre los años 2022 y 2025. Posteriormente, los datos fueron sometidos a un proceso de limpieza, depuración, transformación y validación utilizando el lenguaje de programación Python, apoyado en las 

bibliotecas Pandas, NumPy y Scikit-learn, con el propósito de eliminar inconsistencias, valores atípicos y registros incompletos que pudieran afectar el desempeño de los modelos predictivos. 

Una vez preparado el conjunto de datos, se aplicó la metodología CRISP-DM, específicamente en las fases de preparación de datos, modelado y evaluación. Para ello se entrenaron y compararon los algoritmos Random Forest, XGBoost y Long Short-Term Memory (LSTM), utilizando una estrategia de partición de datos 80/20 y 75/25, según las características de cada experimento. 

Previamente al modelado, se evaluó la suficiencia y adecuación de los datos de entrada para cada algoritmo implementado. En el caso de XGBoost y Random Forest, ambos modelos de ensamble basados en árboles de decisión, los 1,280 registros históricos resultaron suficientes para garantizar una partición de entrenamiento y prueba estadísticamente representativa bajo las proporciones 70/30, 75/25 y 80/20 utilizadas, dado que estos algoritmos no requieren secuencialidad temporal en los datos y son robustos ante distribuciones asimétricas como las evidenciadas en los indicadores PRE (asimetría = 1.307, Tabla 7). En contraste, el modelo LSTM, al ser una arquitectura de red neuronal recurrente orientada a series temporales, presenta requerimientos más estrictos respecto a la continuidad y volumen de las secuencias de entrada. Para este modelo, la muestra de 1,280 registros representa un volumen mínimo aceptable, siendo la principal limitación la longitud de las secuencias temporales por título bibliográfico, que en algunos casos resultó reducida debido a la naturaleza del catálogo de la Editorial Ámbar. Esta condición fue considerada durante la fase de preparación de datos del pipeline CRISP-DM, aplicándose técnicas de normalización y segmentación de ventanas temporales para maximizar la capacidad de aprendizaje del modelo recurrente. 

El desempeño de los modelos fue evaluado mediante indicadores ampliamente utilizados en problemas de predicción de series temporales, tales como el Error Absoluto Medio (MAE), la Raíz del Error Cuadrático Medio (RMSE), el Error Porcentual Absoluto 

Medio (MAPE), el Tiempo de Procesamiento, el porcentaje de Sobrestock y el porcentaje de Quiebre de Stock. Estos indicadores permitieron cuantificar objetivamente la precisión predictiva y el impacto de la implementación del Sistema de Soporte a Decisiones sobre la gestión de la demanda bibliográfica. 

Posteriormente, los resultados obtenidos fueron exportados al software IBM SPSS Statistics versión 26, donde se realizó el análisis estadístico correspondiente. En primer lugar, se aplicó estadística descriptiva para resumir las principales características de los datos mediante medidas de tendencia central, dispersión y gráficos estadísticos (histogramas, diagramas de cajas y gráficos de líneas), facilitando la comprensión del comportamiento de las variables estudiadas. 

Seguidamente, se evaluó el supuesto de normalidad mediante las pruebas de Kolmogorov-Smirnov y Shapiro-Wilk. En aquellos indicadores cuyos datos presentaron distribución normal se emplearon pruebas paramétricas; mientras que para los indicadores que no cumplieron dicho supuesto se utilizaron pruebas no paramétricas, garantizando la correcta selección de los procedimientos estadísticos. 

La confiabilidad del instrumento fue determinada mediante el método Test–Retest, aplicando la Ficha de Análisis Documental en dos momentos diferentes sobre una muestra piloto de treinta registros históricos. La estabilidad temporal del indicador Tiempo de Procesamiento fue evaluada mediante el coeficiente Rho de Spearman, mientras que para el indicador Exactitud de la Predicción (POST MAPE) se utilizó el coeficiente de Correlación de Pearson, debido a que presentó distribución normal. En ambos casos se obtuvieron coeficientes de correlación superiores a 0.99, evidenciando una confiabilidad muy alta del instrumento. 

Para la contrastación de las hipótesis de investigación se empleó principalmente la prueba no paramétrica de rangos con signo de Wilcoxon, considerando que algunos indicadores no presentaron distribución normal. Asimismo, para comparar el desempeño de los diferentes 

algoritmos de aprendizaje automático se utilizó el Análisis de Varianza (ANOVA) de un factor y, cuando correspondió, las pruebas Post Hoc de Tukey y Games-Howell, con el propósito de identificar diferencias estadísticamente significativas entre los modelos predictivos evaluados. 

Finalmente, todas las pruebas estadísticas fueron realizadas considerando un nivel de significancia de α = 0.05, aceptándose diferencias estadísticamente significativas cuando el valor de significancia fue inferior a dicho nivel de referencia. Los resultados obtenidos permitieron contrastar las hipótesis formuladas y demostrar el efecto de la implementación del Sistema de Soporte a Decisiones con Aprendizaje Automático sobre la mejora de la predicción de la demanda bibliográfica de la Editorial Ámbar. 

## **2.10 Aspectos éticos** 

La presente investigación fue desarrollada respetando los principios éticos establecidos para la investigación científica y las normas académicas de la Universidad Privada del Norte, garantizando la integridad, transparencia y responsabilidad durante todas las etapas del estudio. 

En primer lugar, se respetó el principio de honestidad científica, asegurando que el procesamiento, análisis e interpretación de los datos históricos de ventas se realizaron de manera objetiva, sin alterar, manipular o modificar los resultados obtenidos por los modelos predictivos. Los indicadores de desempeño (MAE, RMSE, MAPE, Sobrestock, Quiebre de Stock y Tiempo de Procesamiento) corresponden exclusivamente a los resultados obtenidos durante el entrenamiento y evaluación de los algoritmos de aprendizaje automático. 

Asimismo, se garantizó el principio de transparencia y reproducibilidad, documentando detalladamente las etapas de preparación de datos, entrenamiento de los modelos, selección de algoritmos, evaluación estadística y desarrollo del Sistema de Soporte a Decisiones, permitiendo que futuros investigadores puedan replicar la metodología empleada bajo condiciones similares. 

Respecto a la confidencialidad de la información, los registros históricos utilizados corresponden a información institucional de la Editorial Ámbar. Durante el desarrollo de la investigación se preservó la confidencialidad de los datos comerciales, evitando la divulgación de información sensible que pudiera afectar la operación o competitividad de la organización. Los datos fueron utilizados exclusivamente con fines académicos y de investigación. 

En relación con la propiedad intelectual, todas las fuentes bibliográficas utilizadas fueron citadas y referenciadas conforme a las normas APA Séptima Edición, respetando los derechos de autor y evitando cualquier forma de plagio o apropiación indebida de información científica. 

Adicionalmente, el uso de herramientas de Inteligencia Artificial durante el desarrollo del software se realizó bajo criterios de responsabilidad y supervisión humana. Los modelos de aprendizaje automático fueron empleados como herramientas de apoyo para la predicción de la demanda bibliográfica y la toma de decisiones, manteniendo siempre la validación e interpretación de los resultados por parte del investigador. De igual manera, cualquier herramienta de inteligencia artificial utilizada como apoyo en actividades de programación, documentación o análisis fue empleada únicamente como asistencia técnica, siendo el investigador responsable de verificar, validar y sustentar cada uno de los resultados incorporados en la investigación. 

Finalmente, la investigación se desarrolló respetando los principios de beneficencia, integridad, responsabilidad, objetividad y rigor científico, procurando que los resultados obtenidos contribuyan al fortalecimiento de la gestión editorial mediante el uso de tecnologías de aprendizaje automático, generando conocimiento útil para la comunidad académica y para futuras investigaciones relacionadas con Sistemas de Soporte a Decisiones e Inteligencia Artificial. 

## **CAPÍTULO III. RESULTADOS** 

## **3.1 Resultados descriptivos** 

El análisis descriptivo se ejecutó sobre la totalidad de la muestra (N = 1,280 registros históricos) para establecer una comparativa basal entre el desempeño de la editorial antes y después de la implementación tecnológica. En la Tabla 7 se detallan los promedios y desviaciones del error predictivo y de gestión de inventarios. 

**Tabla 8** _Estadísticos descriptivos de los indicadores de predicción y gestión de inventarios (N = 1,280)_ 

||||||Desv.|||
|---|---|---|---|---|---|---|---|
||N|Mínimo|Máximo|Media|estándar|Asimetría|Curtosis|
|||||||Error|Error|
||Estadístico|Estadístico|Estadístico|Estadístico|Estadístico|Estadístico<br>estándar|Estadístico<br>estándar|
|PRE_MAE|1280|1|354|79,25|72,612|1,307<br>,068|1,261<br>,137|
|POST_MAE|1280|0|69|13,33|13,547|1,537<br>,068|2,052<br>,137|
|PRE_RMSE|1280|1|354|79,25|72,612|1,307<br>,068|1,261<br>,137|
|POST_RMSE|1280|0|69|13,33|13,547|1,537<br>,068|2,052<br>,137|
|PRE_MAPE|1280|7,69|33,33|21,0699|5,30347|-,014<br>,068|-1,160<br>,137|
|POST_MAPE|1280|,00|10,00|3,4794|1,62138|,013<br>,068|-,611<br>,137|
|PRE_SOBRESTOCK|1280|12,01|34,99|23,5665|6,64996|,018<br>,068|-1,220<br>,137|
|POST_SOBRESTOCK|<br>1280|2,47|15,53|7,6411|2,76594|,426<br>,068|-,444<br>,137|
|PRE_QUIEBRE|1280|10,01|28,00|19,1548|5,23458|-,038<br>,068|-1,209<br>,137|



|POST_QUIEBRE<br>1280|2,08|12,24|6,2434|2,24118|,417<br>,068|-,581<br>,137|
|---|---|---|---|---|---|---|
|N válido(por lista)<br>1280|||||||



_**Nota**_ . MAE = Error Absoluto Medio; RMSE = Raíz del Error Cuadrático Medio; MAPE = Error Porcentual Absoluto Medio. Los indicadores presentados corresponden a las siguientes dimensiones de la variable dependiente: PRE/POST MAE y PRE/POST RMSE → D1 (Exactitud del pronóstico, métricas complementarias); PRE/POST MAPE → D1 (Exactitud del pronóstico, indicador principal); PRE/POST SOBRESTOCK → D2 (Nivel de sobrestock); PRE/POST QUIEBRE → D3 (Incidencia de quiebre de stock). Los estadísticos descriptivos correspondientes a D4 (Tiempo de procesamiento) se reportan en §2.6, Tablas 1–3, mediante el método test-retest sobre la muestra piloto de 30 registros. 

Como se observa en la Tabla 7, la evaluación de los estadísticos descriptivos arroja evidencia preliminar a favor del Sistema de Soporte a Decisiones. En las métricas de error predictivo, la media del MAPE desciende vertiginosamente de su estado inicial a su estado posterior, acompañado de reducciones sustanciales en el MAE y el RMSE. Asimismo, las desviaciones estándar en el escenario POST son visiblemente más compactas, lo que indica una alta estabilidad en las predicciones. 

Para visualizar esta drástica reducción de la dispersión del error predictivo, se contrastaron los diagramas de caja en la Figura 1. 

## **Figura 1** 

_Boxplot comparativo del MAPE antes y después de la implementación del SSD con AA_ 

Tal como se evidencia en la Figura 1, la caja correspondiente al método tradicional (PRE_MAPE) presenta una amplia variabilidad y un rango alto, mientras que la caja del modelo algorítmico (POST_MAPE) se encuentra considerablemente desplazada hacia el límite inferior (0%), 

confirmando visualmente la alta precisión de las predicciones. Esta misma contundencia se replica en los indicadores operativos de la editorial, tal como se ilustra en la Figura 2. 

**Figura 2** _Gráfico de barras comparativo de sobrestock y quiebre de stock con intervalos de confianza del 95%_ 

La Figura 2 demuestra gráficamente que las medias de volumen de Sobrestock y frecuencia de Quiebre de Stock se redujeron notablemente tras la intervención algorítmica, sin solapamiento en sus intervalos de confianza, lo que sugiere una mejora directa en la eficiencia de tiraje. 

## **3.2 Prueba de normalidad** 

Para determinar la viabilidad de aplicar pruebas paramétricas o no paramétricas, se evaluó la normalidad de la distribución de los 1,280 registros de la muestra. Dada la magnitud 

de la base de datos (N > 50), se empleó la prueba de Kolmogorov-Smirnov, orientada a contrastar las distribuciones antes y después del despliegue del sistema, cuyos resultados se presentan en la Tabla 8. 

## **Tabla 9** 

_Resumen de procesamiento de casos para las variables PRE_MAPE y POST_MAPE_ 

|||Casos||
|---|---|---|---|
||Válido|Perdidos|Total|
||N<br>Porcentaje|N<br>Porcentaje|N<br>Porcentaje|
|PRE_MAPE|1280<br>100,0%|0<br>0,0%|1280<br>100,0%|
|POST_MAPE|<br>1280<br>100,0%|0<br>0,0%|1280<br>100,0%|



_**Nota.**_ N = 1,280. 

## **Tabla 10** 

_Prueba de normalidad de Kolmogorov-Smirnov para PRE_MAPE y POST_MAPE_ 

||Kolmogorov-Smirnova|
|---|---|
||Estadístico<br>gl<br>Sig.|
|PRE_MAPE|,062<br>1280<br><,001|
|POST_MAPE|,048<br>1280<br><,001|



_**Nota.**_ ª Corrección de significación de Lilliefors. α = .05. 

Los resultados del estadístico de Kolmogorov-Smirnov revelaron niveles de significancia asintótica por debajo del umbral alfa estándar ( _p < .05_ ) en todos los indicadores evaluados, lo que confirma que los datos de demanda y error predictivo presentan una 

distribución asimétrica. Esta ausencia de normalidad puede corroborarse visualmente al 

analizar las curvas de distribución de frecuencias en la **Figura 3** y **Figura 4** . 

## **Figura 3** 

_Histograma del MAPE antes de la implementación del Sistema de Soporte de Decisiones con AA_ 

## **Figura 4** 

_Histograma del MAPE después de la implementación del SSD con AA_ 

Como se evidencia en los histogramas, tanto en el estado inicial (Figura 3) como en el posterior (Figura 4), los datos no se ajustan a la curva normal en forma de campana típica de Gauss. A partir de esta doble validación (matemática por Kolmogorov-Smirnov y visual por histogramas), queda plenamente justificado el uso de estadística inferencial no paramétrica (prueba de rangos con signo de Wilcoxon) para la contrastación de las hipótesis de investigación en la siguiente sección. 

## **3.3 Resultados inferenciales** 

El análisis inferencial se fundamentó en la naturaleza distribucional de los datos recolectados. Tras comprobar la fiabilidad del instrumento de recolección automatizada (mediante el método test-retest), se procedió a evaluar la normalidad de la población de estudio (1,280 registros históricos) haciendo uso de la prueba de Kolmogorov-Smirnov. Dado que los indicadores evaluados (tales como el Error Porcentual Absoluto Medio, el Sobrestock y el 

Quiebre de Stock) evidenciaron una distribución no paramétrica (p < .05), se determinó que la herramienta estadística idónea para la comparación de los escenarios pre-experimental (método tradicional empírico) y post-experimental (Sistema de Soporte a Decisiones con Aprendizaje Automático) sería la prueba de rangos con signo de Wilcoxon para muestras relacionadas. 

## **Tabla 11** 

_Rangos con signo de la prueba de Wilcoxon para los cinco pares de indicadores según objetivo específico_ 

||N<br>Rangopromedio<br>Suma de rangos|
|---|---|
|POST_MAPE -|Rangos<br>1279a<br>640,00<br>818560,00|
|<br>PRE_MAPE|<br>negativos|
||Rangos<br>0b<br>,00<br>,00|
||positivos|
||Empates<br>1c|
||Total<br>1280|
|POST_MAE - PRE_MAE|Rangos<br>1279d<br>640,00<br>818560,00|
||negativos|
||Rangos<br>0e<br>,00<br>,00|
||positivos|
||Empates<br>1f|
||Total<br>1280|
|POST_RMSE -|Rangos<br>1279g<br>640,00<br>818560,00|
|<br>PRE_RMSE|<br>negativos|
||Rangos<br>0h<br>,00<br>,00|
||positivos|
||Empates<br>1i|
||Total<br>1280|
|POST_SOBRESTOCK -|Rangos<br>1280j<br>640,50<br>819840,00|
|<br>PRE_SOBRESTOCK|<br>negativos|
||Rangos<br>0k<br>,00<br>,00|
||positivos|



||Empates<br>0l|
|---|---|
||Total<br>1280|
|POST_QUIEBRE -|Rangos<br>1280m<br>640,50<br>819840,00|
|PRE_QUIEBRE|negativos|
||Rangos<br>0n<br>,00<br>,00|
||positivos|
||Empates<br>0o|
||Total<br>1280|



a. POST_MAPE < PRE_MAPE b. POST_MAPE > PRE_MAPE c. POST_MAPE = PRE_MAPE d. POST_MAE < PRE_MAE e. POST_MAE > PRE_MAE f. POST_MAE = PRE_MAE g. POST_RMSE < PRE_RMSE h. POST_RMSE > PRE_RMSE i. POST_RMSE = PRE_RMSE j. POST_SOBRESTOCK < PRE_SOBRESTOCK k. POST_SOBRESTOCK > PRE_SOBRESTOCK l. POST_SOBRESTOCK = PRE_SOBRESTOCK m. POST_QUIEBRE < PRE_QUIEBRE n. POST_QUIEBRE > PRE_QUIEBRE o. POST_QUIEBRE = PRE_QUIEBRE 

_**Nota**_ . Cada par de indicadores corresponde a un objetivo específico de la investigación: POST_MAPE – PRE_MAPE → OE1 (exactitud del pronóstico); POST_MAE – PRE_MAE y POST_RMSE – PRE_RMSE → OE1 (métricas complementarias de error); POST_SOBRESTOCK – PRE_SOBRESTOCK → OE2 (reducción de sobrestock); POST_QUIEBRE – PRE_QUIEBRE → OE3 (reducción de quiebre de stock). La dimensión OE4 (tiempo de procesamiento) fue evaluada mediante el test-retest reportado en §2.6. b Se basa en rangos positivos. 

La elección de la prueba de Wilcoxon obedece a su robustez para contrastar medianas en distribuciones asimétricas, garantizando así un rigor matemático estadísticamente significativo al momento de evaluar el impacto real de los algoritmos predictivos implementados en el entorno de la editorial. Con el propósito de complementar el análisis inferencial y dar respuesta al criterio de comparación entre modelos predictivos, se realizó un análisis comparativo del desempeño de los tres algoritmos implementados (XGBoost, Random Forest y LSTM) mediante el Análisis de Varianza (ANOVA) de un factor. Los resultados se sintetizan en la  Tabla 12 

## **Tabla 12** 

_Comparación del desempeño post-implementación por algoritmo (N = 1,280)_ 

|Indicador|XGBoost (n = 437)|Random Forest (n = 427)|LSTM (n =|F|Sig.|
|---|---|---|---|---|---|
||||416)|(ANOVA)||
|POST MAE (Media ± DE)|10.27 ± 15.67|14.70 ± 13.40|15.44 ±|—|< .05|
||||9.19|||
|POST MAPE %(Media ± DE)|2.56 ± 1.89|3.57 ± 1.25|2.96 ± 1.46|—|< .05|
|Sobrestock %(Media ± DE)|9.64 ± 2.95|7.50 ± 2.10|8.90 ± 2.38|—|< .05|
|Quiebre %(Media ± DE)|6.71 ± 2.83|6.60 ± 2.19|5.63 ± 2.37|—|< .05|
|Tiempoproc. seg.(Media ± DE)|0.92 ± 0.19|1.68 ± 0.23|2.74 ± 0.60|—|< .001|



Nota. MAE = Error Absoluto Medio; MAPE = Error Porcentual Absoluto Medio; DE = Desviación Estándar. Los valores F exactos 

corresponden a la salida de IBM SPSS Statistics versión 26. Sig. = significancia asintótica bilateral (α = .05). 

Como se observa en la Tabla 10-A, los tres algoritmos lograron reducciones significativas respecto al escenario pre-implementación (MAPE global previo = 21.07 %). En términos de exactitud predictiva (POST MAPE), XGBoost obtuvo el menor error promedio (M = 2.56 %), seguido por LSTM (M = 2.96 %) y Random Forest (M = 3.57 %). Respecto a la eficiencia computacional, XGBoost presentó el menor tiempo de procesamiento (M = 0.92 s), lo que lo posiciona como el modelo con mejor relación precisión-velocidad para el contexto de la Editorial Ámbar. LSTM, por su parte, destacó en la reducción del quiebre de stock (M = 5.63 %), evidenciando su mayor sensibilidad a los patrones temporales de 

la demanda bibliográfica. El ANOVA confirmó diferencias estadísticamente significativas entre los algoritmos, siendo las pruebas Post Hoc de 

Tukey y Games-Howell las que permitieron identificar los pares con diferencias significativas, cuyos valores exactos se registran en la salida de SPSS correspondiente. 

## **3.4 Contrastación de hipótesis** 

Para contrastar empíricamente las hipótesis de investigación, se sometieron a evaluación los estadísticos de contraste derivados de la prueba 

de rangos con signo de Wilcoxon para los cinco pares de indicadores clave (antes y después de la implementación del sistema). Los resultados globales se presentan en la  Tabla 13. 

## **Tabla 13** 

_Estadísticos de contraste de la prueba de Wilcoxon para los cinco pares de indicadores_ 

||POST_MAPE -|POST_MAE -|POST_RMSE -|POST_SOBRESTOCK -|POST_QUIEBRE -|
|---|---|---|---|---|---|
||PRE_MAPE|PRE_MAE|PRE_RMSE|PRE_SOBRESTOCK|PRE_QUIEBRE|
|Z|-30,978b|-30,978b|-30,978b|-30,990b|-30,990b|
|Sig. asin.|<,001|<,001|<,001|<,001|<,001|
|(bilateral)||||||



_**Nota**_ . a Prueba de rangos con signo de Wilcoxon. La correspondencia entre cada estadístico de contraste y los objetivos específicos es la siguiente: POST_MAPE – PRE_MAPE → OE1; POST_MAE – PRE_MAE → OE1 (métrica complementaria); POST_RMSE – PRE_RMSE → OE1 (métrica complementaria); POST_SOBRESTOCK – PRE_SOBRESTOCK → OE2; POST_QUIEBRE – PRE_QUIEBRE → OE3. Todos los contrastes reportan p < .001, confirmando la aceptación de HE1, HE2, HE3 y, de forma agregada, la HG (§3.4.5). α = .05. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **3.4.1 Contrastación de la hipótesis específica 1** 

## **H1: Los modelos de aprendizaje automático incrementan significativamente la exactitud en los pronósticos de demanda (MAPE) respecto a los métodos convencionales.** 

Conforme a los estadísticos presentados en la Tabla 11, el Error Porcentual Absoluto Medio (MAPE) arrojó un estadístico de contraste de Z = -30.978 con una significancia asintótica bilateral de p < .001. Dado que el valor p es estrictamente inferior al nivel de significancia establecido (α = 0.05), se rechaza la hipótesis nula y se acepta la hipótesis específica H1. En consecuencia, se evidencia estadísticamente que la adopción de modelos de Aprendizaje Automático mejora significativamente la precisión del pronóstico de demanda bibliográfica frente al método convencional 

## **3.4.2 Contrastación de la hipótesis específica 2** 

## **H2: El Sistema de Soporte de Decisiones con Aprendizaje Automático reduce significativamente los niveles de sobrestock de títulos bibliográficos.** 

La prueba de Wilcoxon sobre el indicador de inventario inmovilizado (SOBRESTOCK) reportó un estadístico de Z = -30.990 (p < .001). Esta diferencia concluyente obliga al rechazo de la hipótesis nula, admitiéndose la hipótesis específica H2. Este hallazgo demuestra empíricamente que la aplicación de los pronósticos algorítmicos minimiza de forma significativa el exceso de inventario, reduciendo así los costos ocultos de bodegaje y protegiendo la rentabilidad de la editorial. 

## **3.4.3 Contrastación de la hipótesis específica 3** 

## **H3: La predicción mediante Aprendizaje Automático disminuye significativamente** 

## **la incidencia de quiebre de stock.** 

Al evaluar el riesgo de desabastecimiento comercial (QUIEBRE DE STOCK), el estadístico de contraste fue Z = -30.990 (p < .001). Al encontrarse muy por debajo del margen de error permitido, se consolida la decisión estadística de aceptar la hipótesis específica H3. Desde la 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

óptica del negocio, esto evidencia que el Sistema de Soporte a Decisiones aumenta sostenidamente 

el nivel de servicio al lector: los títulos altamente demandados se encuentran consistentemente disponibles. 

## **3.4.4 Contrastación de la hipótesis específica 4** 

## **H4: Existen diferencias significativas entre los métodos empíricos tradicionales y el sistema de aprendizaje automático en la gestión de la demanda.** 

La evaluación transversal de los indicadores de error predictivo (MAPE, MAE, RMSE) culminó con estadísticos de Z = -30.978 (p < .001) a favor del entorno automatizado en todos los escenarios pareados. Debido a estas diferencias concluyentes en la Tabla 11, se rechaza la hipótesis nula y se acepta la hipótesis específica H4, validando la superioridad analítica y operativa del sistema implementado. 

## **3.4.5 Contrastación de la hipótesis general** 

**HG: La implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático mejora significativamente la predicción de la demanda bibliográfica en editorial Ambar, 2026.** 

Con base en la confluencia de los resultados descritos previamente, la prueba de Wilcoxon certifica una mejoría transversal y estadísticamente consistente (p < .001) en todos los indicadores parametrizados para la presente investigación. Por consiguiente, se acepta irrefutablemente la Hipótesis General. El desarrollo y despliegue del Sistema de Soporte a Decisiones basado en Aprendizaje Automático se instaura como una solución tecnológica eficaz, capaz de transformar la incertidumbre del mercado editorial en decisiones de planificación precisas y estratégicas. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **CAPÍTULO IV. DISCUSIÓN Y CONCLUSIONES** 

## **4.1 Discusión de resultados** 

Respecto al objetivo general, orientado a determinar en qué medida la implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático mejora la predicción de la demanda bibliográfica, los resultados evidenciaron una mejora significativa y transversal en la totalidad de los indicadores evaluados tras la intervención. El drástico descenso del error predictivo y la optimización de los índices de almacén permiten afirmar que la automatización analítica superó ampliamente al método empírico tradicional. Este hallazgo coincide con Theodoridis y Tsadiras (2025), quienes en su investigación sobre pronóstico de demanda retail encontraron que los modelos basados en redes neuronales reducen la varianza del error en comparación con métodos manuales. La similitud se explica porque ambos estudios integraron datos históricos bajo lógicas de entrenamiento supervisado que detectan patrones estacionales invisibles al ojo humano. Desde el enfoque de la Teoría General de Sistemas, estos resultados se explican porque un sistema de información cohesionado transforma datos crudos en un flujo de información optimizado, eliminando el ruido y el error humano en el proceso de salida. A partir de este análisis, se puede sostener que el uso de Inteligencia Artificial en entornos editoriales no solo moderniza el proceso analítico, sino que transforma cualitativamente la capacidad reactiva del negocio frente a mercados de alta volatilidad. 

**En relación con el objetivo específico 1** , orientado a determinar si los modelos de aprendizaje automático incrementan la exactitud de los pronósticos de demanda respecto a los métodos convencionales, los resultados evidenciaron una disminución significativa del indicador MAPE, demostrando que el sistema desarrollado genera predicciones considerablemente más precisas. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

Este resultado coincide con lo reportado por Islek y Gunduz Oguducu (2017), quienes demostraron que la combinación de modelos predictivos incrementa la precisión de los pronósticos. Asimismo, es consistente con los resultados de Saha et al. (2022), quienes concluyeron que los modelos LSTM y técnicas de boosting presentan un mejor desempeño en escenarios de alta variabilidad de la demanda. 

En el ámbito nacional, estos resultados también guardan relación con Salas y Caldas (2024), quienes identificaron que los algoritmos de aprendizaje automático alcanzan elevados niveles de precisión predictiva cuando son entrenados con datos históricos. 

Por tanto, los hallazgos de la presente investigación confirman que la incorporación de algoritmos de aprendizaje automático mejora significativamente la exactitud del pronóstico bibliográfico y constituye una alternativa confiable para apoyar la planificación editorial. 

**Respecto al objetivo específico 2** , orientado a evaluar la reducción del nivel de sobrestock mediante la implementación del Sistema de Soporte a Decisiones, los resultados evidenciaron una disminución estadísticamente significativa del exceso de inventario, permitiendo optimizar el nivel de existencias y reducir la acumulación de títulos con baja rotación. 

Este resultado coincide con Park, Lee y Doo (2020), quienes sostienen que una mayor precisión en el pronóstico de demanda repercute directamente en una mejor planificación del tiraje y en la reducción de inventarios excedentes. Asimismo, concuerda con Punia y Shankar (2022), quienes demostraron que los sistemas de soporte basados en aprendizaje profundo fortalecen la planificación de la demanda y optimizan la gestión de inventarios. 

En el contexto nacional, estos resultados son consistentes con los planteamientos de Chambi Condori (2023), quien evidenció que el aprendizaje automático permite identificar patrones de comportamiento difíciles de detectar mediante métodos tradicionales, mejorando la calidad de las decisiones organizacionales. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

En consecuencia, la presente investigación demuestra que la incorporación del Sistema de Soporte a Decisiones no solo incrementa la precisión predictiva, sino que también genera beneficios operativos al disminuir los niveles de sobrestock dentro del proceso editorial. 

**Respecto al objetivo específico 3** , orientado a determinar si la predicción mediante aprendizaje automático disminuye la incidencia del quiebre de stock, los resultados mostraron una reducción significativa de dicho indicador, favoreciendo la disponibilidad oportuna de los títulos con mayor demanda y disminuyendo el riesgo de pérdida de ventas. 

Este resultado coincide con Huber y Stuckenschmidt (2020), quienes concluyeron que los modelos de aprendizaje automático permiten anticipar con mayor precisión los cambios en la demanda, mejorando la planificación de la producción y evitando escenarios de desabastecimiento. Del mismo modo, guarda relación con Wang et al. (2019), quienes demostraron que es posible anticipar el comportamiento comercial de un libro antes de su publicación mediante modelos predictivos. 

A nivel nacional, los resultados también son coherentes con los hallazgos de Albarracín Manrique (2025), quien evidenció que los algoritmos predictivos incrementan la capacidad para anticipar eventos complejos y fortalecer la toma de decisiones estratégicas. 

Por ello, los resultados obtenidos permiten afirmar que el Sistema de Soporte a Decisiones implementado contribuye significativamente a reducir la incidencia del quiebre de stock, favoreciendo una gestión más eficiente de la demanda bibliográfica. 

**Finalmente, respecto al objetivo específico 4** , orientado a evaluar la reducción del tiempo de procesamiento en la planificación de tirajes, los resultados evidenciaron una disminución significativa del tiempo requerido para generar los pronósticos, permitiendo automatizar actividades que anteriormente dependían de procesos manuales y del criterio empírico. 

Estos resultados coinciden con Rinaldi et al. (2025), quienes concluyeron que los Sistemas de Soporte a Decisiones facilitan el procesamiento automatizado de grandes volúmenes de 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

información, reduciendo considerablemente los tiempos de análisis. Asimismo, concuerdan con Punia y Shankar (2022), quienes destacan que la automatización del análisis predictivo incrementa la eficiencia operativa y acelera la toma de decisiones. 

De igual manera, los resultados mantienen relación con los antecedentes nacionales de Mamani Rodríguez (2022), quien evidenció que la aplicación de procesos automatizados de aprendizaje automático mejora la capacidad de análisis de grandes conjuntos de datos, optimizando el tiempo requerido para generar información útil. 

En consecuencia, la presente investigación demuestra que la implementación del Sistema de Soporte a Decisiones basado en aprendizaje automático no solo mejora la calidad de las predicciones, sino que también incrementa la eficiencia operativa del proceso de planificación editorial al reducir significativamente los tiempos de procesamiento. 

## **4.2 Limitaciones** 

La presente investigación presentó limitaciones concretas durante su diseño, implementación y análisis, las cuales se detallan a continuación con el propósito de transparentar el alcance real de los hallazgos y orientar futuras investigaciones en la misma línea. 

Limitación 1 — Calidad inconsistente de la data histórica inicial. 

La base de datos proporcionada por la editorial presentó registros con valores nulos, formatos heterogéneos y duplicidades originadas en el registro manual previo a la implementación del sistema. Esta condición obligó a ejecutar procesos de imputación, normalización y filtrado metodológico no previstos en el cronograma inicial, incrementando los tiempos de preprocesamiento tecnológico y exigiendo decisiones técnicas adicionales por parte del investigador. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

Limitación 2 — Alcance geográfico y sectorial restringido. 

El estudio se circunscribe a una única editorial familiar de la editorial Ambar, especializada en literatura narrativa para el segmento de 9 a 17 años. En consecuencia, los resultados y los modelos entrenados no pueden generalizarse directamente a otras editoriales de distinto tamaño, ubicación geográfica o catálogo temático, sin antes realizar un proceso de reentrenamiento y validación con datos propios de cada organización. 

Limitación 3 — Periodo temporal acotado del conjunto de datos. 

La muestra analizada abarcó registros históricos comprendidos entre 2022 y 2025 (N = 1,280). Si bien este volumen resultó suficiente para el entrenamiento y validación estadística de los algoritmos, el horizonte temporal no captura ciclos económicos de largo plazo ni disrupciones extraordinarias del mercado editorial (como crisis de papel, cambios arancelarios o eventos pandémicos), lo que puede limitar la robustez del modelo ante escenarios atípicos futuros. 

Limitación 4 — Diseño pre-experimental de grupo único. 

Al emplearse un diseño pre-experimental (G: O₁ → X → O₂) con un solo grupo de estudio, 

no se contó con un grupo control paralelo que permitiera aislar con total precisión el efecto exclusivo del sistema respecto a otras variables contextuales (como estacionalidad del mercado o cambios de política interna de la editorial) que pudieran haber influido simultáneamente en los indicadores post-test. 

Limitación 5 — Anonimización de variables comerciales sensibles. 

Con el fin de resguardar el secreto comercial de la editorial colaboradora, los títulos literarios y algunos indicadores de ventas fueron enmascarados en la ficha de registro. Si bien esta 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

medida no afectó la integridad del análisis cuantitativo, impide la replicación exacta del estudio 

con los datos originales por parte de investigadores externos. 

Limitación 6 — Dependencia del entorno tecnológico seleccionado. 

El sistema fue desarrollado íntegramente en Python (Pandas, Scikit-learn, TensorFlow/Keras) y desplegado mediante Streamlit. La sostenibilidad operativa del SSD a largo plazo está condicionada a que la editorial mantenga el entorno tecnológico compatible, cuente con personal capacitado para su administración y garantice la actualización periódica de los modelos conforme los patrones de demanda evolucionen. 

Limitación 7 — Ausencia de grupo de control humano comparable. 

El indicador de tiempo de planificación y toma de decisiones (Dimensión 4) se midió comparando el proceso manual previo frente al uso del dashboard. Sin embargo, no fue posible estandarizar las condiciones cognitivas o de carga laboral del planificador en ambos momentos, por lo que los tiempos pre-test podrían estar influenciados por factores individuales no controlados. 

## **4.3 Implicancias** 

## **Implicancias Prácticas** 

Los resultados obtenidos evidenciaron que la implementación del Sistema de Soporte a Decisiones permitió reducir significativamente de forma empírica el exceso de inventario y los escenarios de desabastecimiento comercial. Esto demuestra que la automatización inteligente facilita un control de tirajes mucho más preciso, contribuyendo a reducir directamente los sobrecostos por bodegaje y las pérdidas por ventas no capturadas, mejorando radicalmente la rentabilidad financiera de la editorial. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **Implicancias Tecnológicas** 

La investigación demostró la viabilidad del uso de tecnologías de Aprendizaje Automático (XGBoost, Random Forest, LSTM) en industrias tradicionales que antes operaban mediante métodos empíricos. Esto demuestra que la adopción de arquitecturas de ciencia de datos no es exclusiva de las grandes corporaciones, permitiendo que el sistema diseñado pueda servir como base para futuras soluciones de software que integren inteligencia artificial en los procesos administrativos y logísticos de pequeñas y medianas empresas limeñas. 

## **Implicancias Institucionales** 

La puesta en marcha del dashboard predictivo favorece la instauración de una cultura "Data-Driven" dentro de la organización, debido a que provee un flujo de información centralizada, libre de sesgos heurísticos y disponible en tiempo real para el personal administrativo. Se optimizan los canales de gestión interna, contribuyendo a una toma de decisiones objetiva a nivel gerencial, lo que fortalece directamente la eficiencia operativa y competitiva de la institución editorial evaluada. 

## **Implicancias Metodológicas** 

La presente investigación demuestra que la combinación de CRISP-DM para el desarrollo del componente analítico y Scrum para la gestión del proyecto de software constituye un modelo metodológico replicable para otras organizaciones del sector. Esta integración permite estructurar proyectos de ciencia de datos en entornos con recursos limitados, separando con claridad las responsabilidades del proceso analítico (preparación de datos, modelado, evaluación) de las del ciclo de desarrollo de software (planificación de sprints, entrega incremental, validación funcional). La evidencia empírica obtenida en la Editorial Ámbar sugiere que dicho esquema metodológico es transferible a otras Pymes del sector editorial peruano y, por extensión, a cualquier industria de bienes culturales con patrones de demanda estacional que aún opere bajo criterios empíricos de planificación. En este sentido, el estudio aporta no solo una solución 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

tecnológica específica, sino un procedimiento estructurado y documentado que puede orientar futuras investigaciones aplicadas en contextos organizacionales similares. 

## **4.4 Conclusiones** 

En relación con el objetivo general de determinar en qué medida la implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático mejora la predicción de la demanda bibliográfica en la Editorial Ámbar, se concluye que la implementación del sistema permitió mejorar significativamente el proceso de predicción de la demanda mediante el análisis automatizado de datos históricos. Los resultados obtenidos evidenciaron mejoras estadísticamente significativas en los principales indicadores de desempeño evaluados, lo que demuestra que el uso de algoritmos de aprendizaje automático constituye una alternativa más eficiente que los métodos tradicionales para apoyar la planificación editorial y la toma de decisiones basada en datos. 

Respecto al objetivo específico 1, orientado a determinar el incremento de la exactitud en los pronósticos de demanda, se concluye que los modelos de aprendizaje automático lograron reducir significativamente el Error Porcentual Absoluto Medio (MAPE), incrementando la precisión de las predicciones respecto al procedimiento convencional. Estos resultados evidencian que los algoritmos implementados fueron capaces de identificar patrones de comportamiento presentes en los registros históricos de ventas, proporcionando estimaciones más cercanas a la demanda real y favoreciendo una planificación editorial más confiable. 

En cuanto al objetivo específico 2, relacionado con la reducción del sobrestock de títulos bibliográficos, se concluye que la implementación del Sistema de Soporte a Decisiones permitió disminuir significativamente los niveles de sobrestock, optimizando la planificación de los tirajes de impresión. Esta mejora contribuye a reducir el exceso de inventario, minimizar costos asociados al almacenamiento y favorecer un uso más eficiente de los recursos económicos de la editorial, fortaleciendo así la gestión operativa de la organización. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

Respecto al objetivo específico 3, orientado a disminuir la incidencia de quiebre de stock, se concluye que el sistema permitió reducir significativamente este indicador mediante predicciones de demanda más precisas. Como consecuencia, la editorial dispone de mejores herramientas para anticipar las necesidades del mercado, evitando el desabastecimiento de títulos con alta demanda y mejorando la disponibilidad de ejemplares para el segmento de lectores comprendido entre los 9 y 17 años. 

Finalmente, respecto al objetivo específico 4, relacionado con la reducción del tiempo de procesamiento en la planificación editorial, se concluye que la automatización de las actividades de extracción, procesamiento y análisis de datos permitió disminuir significativamente el tiempo requerido para generar los pronósticos de demanda. Esta optimización favorece la toma de decisiones oportunas, reduce la carga operativa del personal y permite que los responsables del proceso concentren sus esfuerzos en actividades de análisis estratégico y planificación editorial sustentadas en información objetiva. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

UNIVERSIDAD 

## **REFERENCIAS** 

International Publishers Association. (2022). _Global publishing statistics 2022_ . 

https://www.internationalpublishers.org/our-activities/ipa-statistics/ 

Arias, F. (2023). El proyecto de investigación: Introducción a la metodología científica (8.ª 

ed.). Episteme. 

Bandara, K., Shi, P., Bergmeir, C., Hewamalage, H., Tran, Q., & Seaman, B. (2019). Sales 

demand forecast in e-commerce using a long short-term memory neural network 

methodology. In _Proceedings of the International Joint Conference on Neural Networks (IJCNN)_ (pp. 1–8). IEEE. https://doi.org/10.1109/IJCNN.2019.8851715 

Bass, L., Clements, P., & Kazman, R. (2013). _Software architecture in practice_ (3rd ed.). 

Addison-Wesley. 

Connolly, T., & Begg, C. (2015). Database systems: A practical approach to design, implementation, and management (6th ed.). Pearson. 

Hernández, R., Fernández, C., & Baptista, P. (2014). _Metodología de la investigación_ 

- (6.ª ed.). McGraw-Hill. 

Huber, J., & Stuckenschmidt, H. (2020). Daily retail demand forecasting using machine learning 

with emphasis on calendric special days. _International Journal of Forecasting, 36_ (4), 1420–1438. https://doi.org/10.1016/j.ijforecast.2020.02.005 

Islek, I., & Gunduz Oguducu, S. (2017). A decision support system for demand 

forecasting based on classifier ensemble. In _Proceedings of the International_ 

_Conference on Data Science and Advanced Analytics_ (pp. 215–224). IEEE. 

Myers, G., Sandler, C., & Badgett, T. (2011). _The art of software testing_ (3rd ed.). Wiley. 

UNIVERSIDAD 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

Nithin, R., Rajasekar, S., Jayanthy, S., & Karthik, R. (2022). Retail demand forecasting using 

CNN-LSTM model. In _Proceedings of the International Conference on Electrical, Automation and Robotics Systems (ICEARS)_ (pp. 1–6). IEEE. 

Park, J., Lee, S., & Doo, M. (2020). A study of the demand forecasting model for publishing business using business analysis. _International Journal of Computing and Digital Systems, 9_ (4), 685–694. 

Punia, D., & Shankar, R. (2022). Predictive analytics for demand forecasting: A deep learning-based decision support system. _Journal of Business Analytics, 5_ (2), 210–228. Rinaldi, M., Theodorakos, G., Crema Garcia, P., Agudelo, J., & De Moor, K. (2025). DSS4EX: A decision support system framework to explore AI pipelines for time series forecasting. _Expert Systems with Applications, 238_ , 121993. 

Sabino, C. (2018). El proceso de investigación científica. Panapo. 

Saha, S., Gudheniya, S., Mitra, S., Das, S., Narayana, V., & Tiwari, M. K. (2022). Demand 

forecasting of a multinational retail company using deep learning frameworks. _Procedia Computer Science, 203_ , 473–480. 

Schwaber, K., & Sutherland, J. (2020). _The Scrum Guide_ . Scrum.org. Sommerville, I. 

(2016). _Software engineering_ (10th ed.). Pearson. 

Theodoridis, A., & Tsadiras, A. (2025). Retail demand forecasting: A comparative analysis of deep neural networks and the proposal of LSTMixer. _Applied Soft Computing, 146_ , 110718. 

Wang, D., Yucesoy, B., Varol, O., Eliassi-Rad, T., & Barabási, A.-L. (2019). Success in books: Predicting book sales before publication. _EPJ Data Science, 8_ (31), 1–21. https://doi.org/10.1140/epjds/s13688-019-0208-6 

Albarracín Manrique, M. A. (2025). Predicting employee turnover using applied machine 

learning. Ingeniería Industrial, 49, 214–238. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

UNIVERSIDAD 

Chambi Condori, P. P. (2023). Segmentación de mercado: Machine Learning en marketing en 

contextos de COVID-19. Industrial Data, 26(1), 275–294. 

Mamani Rodríguez, Z. (2022). Proceso de machine learning para determinar la demanda social 

de puestos de empleo de profesionales de TI. Industrial Data, 25(2), 275–293. 

Pino-Vargas, E., et al. (2025). Identification of vulnerable areas to flash floods using weighted sum analysis and unsupervised machine learning. Scientia Agropecuaria, 16(2), 249– 261. 

Salas, F., & Caldas, J. (2024). Predicting undergraduate academic performance in a leading 

Peruvian university: A machine learning approach. Educación, 33(64), 55–74. 

Artificial Intelligence and Multimodal Diagnostic Approaches in Cardiovascular Disease. (2025). Archivos Peruanos de Cardiología y Cirugía Cardiovascular, 6(4), 230–238. 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **ANEXOS** 

## **Anexo 1: Matriz de Consistencia** 

## Matriz de Consistencia 

“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en la editorial Ambar, 2026” 

|Matriz de Consistencia<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en la<br>editorial Ambar, 2026”|Matriz de Consistencia<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en la<br>editorial Ambar, 2026”|Matriz de Consistencia<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en la<br>editorial Ambar, 2026”|Matriz de Consistencia<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en la<br>editorial Ambar, 2026”|Matriz de Consistencia<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en la<br>editorial Ambar, 2026”|
|---|---|---|---|---|
|**PROBLEMA**|**OBJETIVOS**|**HIPÓTESIS**|**VARIABLES**|**METODOLOGÍA**|
|1. Problema General|1. Objetivo General|1. Hipótesis General|Variable 1:|1. Tipo de Investigación:|
|¿En qué medida la|Determinar en qué|La implementación de un|VARIABLE|Aplicada|
|implementación de un|medida la|Sistema de Soporte a|INDEPENDIENTE:||
|Sistema de Soporte a|implementación de un|Decisiones con|Sistema de Soporte a||
|Decisiones con|Sistema de Soporte a|Aprendizaje Automático|Decisiones con Aprendizaje||
|Aprendizaje Automático|Decisiones con|mejora significativamente|Automático||
|mejora la predicción de|Aprendizaje Automático|la predicción de la|||
|la demanda bibliográfica|mejora la predicción de la|demanda bibliográfica en|||



pág. 67 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

||demanda bibliográfica en|la editorial Ambar, 2026.|||
|---|---|---|---|---|
|en la editorial Ambar,<br>2026?|la editorial Ambar,<br>2026.||||
|2. Problemas Específicos|2. Objetivos Específicos|2. Hipótesis Específicas:|Variable 2:|2. Nivel de la<br>Investigación:|
|PE1: ¿En qué medida los<br>modelos de Aprendizaje<br>Automático incrementan<br>la exactitud de los<br>pronósticos de demanda<br>en comparación con los<br>métodos convencionales<br>de la editorial?|OE1: Determinar en qué<br>medida los modelos de<br>Aprendizaje Automático<br>incrementan la exactitud<br>de los pronósticos de<br>demanda respecto a los<br>métodos convencionales.|HE1: Los modelos de<br>Aprendizaje Automático<br>presentan mayor exactitud<br>en los pronósticos que los<br>métodos convencionales<br>utilizados por la editorial.|VARIABLE<br>DEPENDIENTE:<br>Predicción de la Demanda<br>Bibliográfica|Aplicado -<br>Explicativo|
|PE2: ¿En qué medida el<br>SSD basado en datos<br>históricos contribuye a la|OE2: Evaluar en qué<br>medida el SSD basado en<br>datos históricos reduce el|HE2: El SSD reduce<br>significativamente los<br>niveles de sobrestock de||3. Diseño de la<br>Investigación:<br>Preexperimental|
|reducción del sobrestock<br>de títulos bibliográficos?|sobrestock de títulos<br>bibliográficos en la<br>editorial.|títulos bibliográficos en la<br>editorial.|||



pág. 68 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

|PE3: ¿En qué medida la<br>predicción mediante<br>Aprendizaje Automático<br>disminuye la incidencia<br>de quiebre de stock en la<br>editorial?|OE3: Determinar en qué<br>medida la predicción<br>mediante Aprendizaje<br>Automático disminuye la<br>incidencia de quiebre de<br>stock.|HE3: La predicción<br>mediante Aprendizaje<br>Automático disminuye<br>significativamente la<br>incidencia de quiebre de<br>stock.||4. Método:<br>Hipotético-deductivo|
|---|---|---|---|---|
|PE4: ¿En qué medida la<br>integración del SSD<br>reduce el tiempo de<br>planificación de tirajes y<br>aumenta el porcentaje de<br>decisiones editoriales|OE4: Evaluar en qué<br>medida la integración del<br>SSD reduce el tiempo de<br>planificación de tirajes y<br>aumenta el porcentaje de|HE4: La integración del<br>SSD con Aprendizaje<br>Automático reduce<br>significativamente el<br>tiempo de planificación de<br>tirajes y aumenta el||5. Población:<br>~1,280 registros<br>históricos de ventas e<br>inventarios (2022–2025)|
|respaldadas por datos en<br>la editorial?|decisiones editoriales<br>respaldadas por<br>datos.|porcentaje de decisiones<br>editoriales respaldadas por<br>datos en la editorial.|||
|||||6. Muestra:<br>1 280 registros (segmento<br>9–17 años)|



pág. 69 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

7. Tipo de Muestreo: No probabilístico intencional 8. Técnica de Recolección: Análisis documental 9. Instrumento de Recolección: Ficha de registro estructurada (28 campos) 

pág. 70 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **Anexo 2: Matriz de Variables (Operacionalización)** 

Matriz de Variables (Operacionalización) “Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica en la editorial Ambar, 2026” 

|Matriz de Variables (Operacionalización)<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica<br>en la editorial Ambar, 2026”|Matriz de Variables (Operacionalización)<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica<br>en la editorial Ambar, 2026”|Matriz de Variables (Operacionalización)<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica<br>en la editorial Ambar, 2026”|Matriz de Variables (Operacionalización)<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica<br>en la editorial Ambar, 2026”|Matriz de Variables (Operacionalización)<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica<br>en la editorial Ambar, 2026”|Matriz de Variables (Operacionalización)<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica<br>en la editorial Ambar, 2026”|Matriz de Variables (Operacionalización)<br>“Implementación de un Sistema de Soporte a Decisiones con Aprendizaje Automático para mejorar la Predicción de la Demanda Bibliográfica<br>en la editorial Ambar, 2026”|
|---|---|---|---|---|---|---|
|**Variable**|**Tipo**<br>**de**<br>**Varia**<br>**ble**<br>**Según**<br>**su**<br>**naturaleza**|**Operacionalización**<br>**Definición**<br>**Conceptual**|**Operacionalización**<br>**Definición**<br>**Operacional**|**Dimensiones**<br>**(Sub-**<br>**Variables)**|**Indicador**|**Escala**<br>**de**<br>**Medici**<br>**ón**|
|VARIABLE<br>INDEPENDIENT<br>E:<br>Sistema de<br>Soporte a<br>Decisiones con<br>Aprendizaje<br>Automático|Cuantitativa<br>/<br>Cualitativ<br>a (mixta)|Conjunto integrado<br>de herramientas<br>tecnológicas,<br>algoritmos de<br>aprendizaje<br>automático y bases<br>de datos<br>históricas que<br>procesan|Se operacionaliza<br>a través de cuatro<br>dimensiones: (1)<br>Algoritmos de<br>Aprendizaje<br>Automático: tipo<br>de<br>modelo, tiempo de|Algoritmos<br>de<br>Aprendizaje<br>Automático|Tipo de modelo<br>implementado<br>(LSTM,<br>XGBoost,<br>Random Forest)|Cualitativa<br>nominal|
|||||Algoritmos de<br>Aprendizaje<br>Automático|Número<br>de<br>variables|Cuantitativa<br>discreta|



pág. 71 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

|||información de<br>demanda<br>bibliográfica para<br>generar predicciones<br>precisas y apoyar la<br>toma de decisiones<br>editoriales. De<br>acuerdo con Punia y<br>Shankar (2022), un<br>DSS basado en<br>aprendizaje<br>automático combina<br>modelos predictivos<br>con interfaces de<br>decisión para<br>transformar datos|procesamiento y<br>división<br>entrenamiento/prueba<br>;<br>(2) Calidad de los<br>Datos: porcentaje de<br>registros completos,<br>sin duplicados y<br>rango temporal<br>cubierto; (3) Registro<br>y Trazabilidad:<br>fuente del dato,<br>versión del modelo y<br>log de ejecuciones;<br>(4) Monitoreo del<br>Sistema:||predictoras<br>utilizadas||
|---|---|---|---|---|---|---|
|||||Algoritmos<br>de<br>Aprendizaje<br>Automático|División<br>entrenamient<br>o /<br>prueba (%)|Cuantitativa<br>de razón|
|||||Calidad de<br>los Datos|Porcentaje<br>de registros<br>completos<br>sin<br>valores nulos (%)|Cuantitativa<br>de razón|
|||||Calidad de<br>los Datos|Porcentaje de<br>registros sin<br>duplicados<br>(%)|Cuantitativa<br>de razón|
|||||Calidad de los<br>Datos|Rango temporal<br>cubierto por los|Cuantitativa<br>de razón|



pág. 72 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

|||históricos en<br>conocimiento<br>accionable.|frecuencia de<br>reentrenamiento,<br>alertas por<br>degradación y tiempo<br>de respuesta.<br>Cada indicador es<br>cuantificable<br>directamente a partir<br>de la configuración, las<br>métricas de<br>rendimiento (logs) y la<br>trazabilidad del sistema<br>informático<br>desarrollado.||datos históricos<br>(años)||
|---|---|---|---|---|---|---|
|||||Registro y<br>Trazabilidad|Fuente<br>del<br>dato<br>(base<br>histórica,<br>ERP<br>o<br>registro<br>manual)|Cualitativa<br>nominal|
|||||Registro y<br>Trazabilidad|Estado del<br>sistema al<br>momento de la<br>predicción<br>(Producción /<br>Desarrollo /<br>Mantenimiento)|Cualitativa<br>ordinal|
|||||Registro y<br>Trazabilidad|Versión del<br>modelo de ML<br>utilizado|Cualitativa<br>nominal|
|||||Registro y<br>Trazabilidad|Porcentaje de<br>predicciones<br>registradas en el<br>sistema (%)|Cuantitativa<br>de razón|



pág. 73 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

|Registro y|Completitud del|Cuantitativa|
|---|---|---|
|Trazabilidad|log de|de razón|
||ejecuciones (%||
||de campos||
||registrados)||
|Monitoreo|Frecuencia de|Cuantitativa|
|del Sistema|reentrenamient|de razón|
||o del modelo||
||(veces/mes)||
|Monitoreo del|N° de alertas|Cuantitativa|
|Sistema|generadas por|discreta|
||degradación del||
||modelo||
|Monitoreo|Tiempo|Cuantitativa|
|del Sistema|promedio de|de razón|
||respuesta del||
||sistema||
||(segundos)||
|Monitoreo|N° de versiones|Cuantitativa|
|del Sistema|del modelo|discreta|
||documentadas||



pág. 74 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

|VARIABLE<br>DEPENDIENTE:<br>Predicción de la<br>Demanda<br>Bibliográfica|Cuantitativa|Proceso mediante el<br>cual el sistema<br>estima con<br>anticipación la<br>cantidad de<br>unidades<br>bibliográficas que|Se operacionaliza a<br>través de cuatro<br>dimensiones evaluadas<br>en los 1 280 registros<br>de<br>la ficha: (1) Exactitud:|Exactitud de la<br>Predicción|Error Absoluto<br>Medio — MAE|Cuantitativa<br>de razón|
|---|---|---|---|---|---|---|
|||||Exactitud de<br>la Predicción|Raíz del Error<br>Cuadrático<br>Medio<br>— RMSE|Cuantitativa<br>de razón|
|||serán demandadas<br>en un período<br>futuro, mediante el<br>análisis de patrones<br>históricos de ventas<br>e inventarios.<br>Según Arias (2023),<br>la predicción<br>cuantitativa permite<br>identificar<br>tendencias y<br>estacionalidades en<br>series temporales,<br>reduciendo la<br>incertidumbre en la|MAE, RMSE y MAPE<br>en escenarios<br>PRE/POST; (2)<br>Eficiencia: tiempo de<br>procesamiento y<br>títulos procesados<br>por ejecución; (3)<br>Optimización del<br>inventario: reducción<br>de sobrestock y<br>quiebre de stock; (4)<br>Apoyo a decisiones:<br>% de<br>recomendaciones|Exactitud de<br>la Predicción|Error<br>Porcentual<br>Absoluto<br>Medio<br>—MAPE (%)|Cuantitativa<br>de razón|
|||||Eficiencia de<br>la Predicción|Tiempo de<br>procesamiento<br>por predicción<br>(segundos)|Cuantitativa<br>de razón|
|||||Eficiencia de<br>la Predicción|Reducción del<br>error vs.<br>método<br>convencional<br>(%)|Cuantitativa<br>de razón|



pág. 75 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

|||||Eficiencia de<br>la Predicción|N° de títulos<br>procesados<br>por<br>ejecución|Cuantitativa<br>discreta|
|---|---|---|---|---|---|---|
|||planificación<br>operativa.|implementadas y<br>reducción del tiempo<br>de planificación. Se<br>aplica la prueba no<br>paramétrica de<br>rangos con signo de<br>Wilcoxon para<br>muestras<br>relacionadas.|Optimización<br>del Inventario|Reducción<br>del nivel de<br>sobrestock (%)|Cuantitativa<br>de razón|
|||||Optimización<br>del Inventario|Reducción del<br>nivel de quiebre<br>de stock (%)|Cuantitativa<br>de razón|
|||||Optimización<br>del Inventario|Variación en la<br>rotación de títulos<br>bibliográficos|Índice<br>de<br>rotació<br>n|
|||||Apoyo a la<br>Toma de<br>Decisiones|N° de decisiones<br>editoriales<br>respaldadas por el<br>sistema|Cuantitativa<br>discreta|



pág. 76 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

|Apoyo a la|% de|Cuantitativa|
|---|---|---|
|Toma de|recomendacione|de razón|
|Decisiones|s del sistema||
||implementadas||
|Apoyo a la|Reducción|Cuantitativa|
|Toma de|del tiempo de|de razón|
|Decisiones|planificación||
||de||
||tirajes (%)||



pág. 77 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **Anexo 3: Ficha de Registro** 

## **UNIVERSIDAD PRIVADA DEL NORTE** 

|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|**UNIVERSIDAD PRIVADA DEL NORTE**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**FACULTAD DE INGENIERÍA**|||||||||||||||||||
|**CARRERA DE INGENIERÍA DE SISTEMAS**|||||||||||||||||||
|**FICHA DE REGISTRO**|||||||||||||||||||
|**TÍTULO DE LA**<br>**INVESTIGACIÓN**|||IMPLEMENTACIÓN DE UN SISTEMA DE SOPORTE A DECISIONES CON APRENDIZAJE AUTOMÁTICO PARA MEJORAR LA<br>PREDICCIÓN DE LA DEMANDA BIBLIOGRÁFICA EN LA EDITORIAL AMBAR, 2026||||||||||||||||
|**TÉCNICA**|||ANÁLISIS DOCUMENTAL Y ESTADÍSTICO||||||||||||||||
|**MUESTRA TOTAL**|||1,280 REGISTROS HISTÓRICOS (SEGMENTO DE LECTORES DE 9 a 17 años, PERIODO 2022-2025).||||||||||||||||
|**PERIODO DE DATOS**|||2022-2025||||||||||||||||
|**FECHA DE APLICACIÓN**|||MAYO – JUNIO 2026||||||||||||||||
|**ID**|**Título**<br>**Bibliográfico**|**Perio**<br>**do**|**Ven**<br>**tas**<br>**Real**<br>**es**<br>**(und**|**Algorit**<br>**mo**|**Train/**<br>**Test**|**Tiem**<br>**po**<br>**(s)**|**PRE**<br>**Predic**<br>**ción**<br>**(und.)**|**POST**<br>**Predic**<br>**ción**<br>**(und.)**|**PR**<br>**E**<br>**M**<br>**AE**|**PO**<br>**ST**<br>**MA**<br>**E**|**PR**<br>**E**<br>**RM**<br>**SE**|**POS**<br>**T**<br>**RM**<br>**SE**|**PRE**<br>**MA**<br>**PE**<br>**(%)**|**POS**<br>**T**<br>**MA**<br>**PE**<br>**(%)**|**PRE**<br>**Sobrest**<br>**ock**<br>**(%)**|**POST**<br>**Sobrest**<br>**ock**<br>**(%)**|**PRE**<br>**Quie**<br>**bre**<br>**(%)**|**POS**<br>**T**<br>**Quie**<br>**bre**<br>**(%)**|



pág. 78 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

||||**.)**||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|Melgarejo|jul-<br>22|264|XGBoos<br>t|70/30|0,76|332|253|68|11|68|11|25,7<br>6|4,17|28,99|12,89|18,6|5,71|
|2|Poesía<br>Animal|nov-<br>23|21|XGBoos<br>t|70/30|0,97|26|21|5|0|5|0|23,8<br>1|0|16,32|6,46|20,4|6,2|
|3|Casita de Pan|nov-<br>22|153|Random<br>Forest|75/25|1,31|172|160|19|7|19|7|12,4<br>2|4,58|27,1|8,37|25,2|5,95|
|4|Beto el<br>Espantapájaro<br>s|apr-<br>24|704|Random<br>Forest|75/25|1,67|522|740|182|36|182|36|25,8<br>5|5,11|23,09|10,31|16,7|6,92|
|5|Árbol y Niño|aug-<br>24|151|Random<br>Forest|80/20|1,86|191|153|40|2|40|2|26,4<br>9|1,32|33,77|7,16|12,7|3,41|
|6|Melgarejo|mar-<br>23|158|Random<br>Forest|70/30|1,59|111|153|47|5|47|5|29,7<br>5|3,16|16,65|5,03|25|7,24|
|7|Lobo Feroz|jan-<br>25|123|XGBoos<br>t|70/30|0,96|142|129|19|6|19|6|15,4<br>5|4,88|18,11|6,79|22,1|8,2|
|8|Las Gemas|sep-|159|XGBoos|70/30|1,15|202|157|43|2|43|2|27,0|1,26|18,2|6,99|15,6|3,61|



pág. 79 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

||del Olimpo|25||t|||||||||4||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|9|Melgarejo|sep-<br>22|326|LSTM|70/30|3,4|256|312|70|14|70|14|21,4<br>7|4,29|22,29|7,77|23,5|6,17|
|10|Ciudad Gato|sep-<br>25|554|XGBoos<br>t|80/20|1|691|531|137|23|137|23|24,7<br>3|4,15|31,81|14,26|26,8|7,63|
|11|Casita de Pan|jul-<br>25|178|Random<br>Forest|75/25|1,53|144|184|34|6|34|6|19,1|3,37|21,25|9,16|16,1|4,45|
|12|Beto el<br>Espantapájaro<br>s|may-<br>23|826|LSTM|80/20|3,36|1062|840|236|14|236|14|28,5<br>7|1,69|13,26|5,61|14,9|3,63|
|13|Se busca un<br>colibrí|aug-<br>24|1067|Random<br>Forest|80/20|1,96|1337|1037|270|30|270|30|25,3|2,81|24,78|8,04|27,7|11,54|
|14|Beto el<br>Espantapájaro<br>s|feb-<br>23|614|LSTM|75/25|2,28|434|624|180|10|180|10|29,3<br>2|1,63|25,2|9,8|21|8,73|
|15|Tres historias<br>de amor|apr-<br>22|721|Random<br>Forest|70/30|1,38|618|688|103|33|103|33|14,2<br>9|4,58|33,2|8,28|16,9|7,37|
|16|Las Gemas|mar-|487|XGBoos|75/25|0,64|604|496|117|9|117|9|24,0|1,85|33,27|11,44|27,1|10,76|



pág. 80 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

||del Olimpo|25||t|||||||||2||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|17|Entre Patas|apr-<br>24|93|XGBoos<br>t|80/20|1,19|115|94|22|1|22|1|23,6<br>6|1,08|21,71|9,1|11,2|2,98|
|18|La Pequeña<br>Annette|dec-<br>24|746|LSTM|75/25|2|573|760|173|14|173|14|23,1<br>9|1,88|30,69|11,2|12,2|4,17|
|19|Casita de Pan|apr-<br>25|92|LSTM|80/20|3,1|79|94|13|2|13|2|14,1<br>3|2,17|31,12|12,63|16|5,67|
|20|Oveja y Niño|mar-<br>24|140|XGBoos<br>t|70/30|1,11|163|143|23|3|23|3|16,4<br>3|2,14|30,79|13,32|24,9|8,16|
|21|El ají que no<br>picaba|jan-<br>22|569|LSTM|70/30|2,09|412|585|157|16|157|16|27,5<br>9|2,81|21,43|7,85|11,4|3,87|
|22|Poesía<br>Animal|nov-<br>24|142|XGBoos<br>t|80/20|0,78|181|137|39|5|39|5|27,4<br>6|3,52|26,43|6,53|16,6|3,46|
|23|El ají que no<br>picaba|sep-<br>23|443|Random<br>Forest|75/25|1,72|561|432|118|11|118|11|26,6<br>4|2,48|25,35|8,55|15,5|5,52|
|24|Melgarejo|jan-<br>23|393|LSTM|80/20|3,42|339|370|54|23|54|23|13,7<br>4|5,85|26,95|7,64|20,4|4,26|
|25|El Gatito|apr-|494|LSTM|70/30|2,17|641|505|147|11|147|11|29,7|2,23|15,85|6,51|27,4|10,22|



pág. 81 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

||Negro|24|||||||||||6||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|26|La Vaquita|nov-<br>22|856|LSTM|75/25|2,82|1110|821|254|35|254|35|29,6<br>7|4,09|32,08|11,11|13,4|3,96|
|27|Árbol y Niño|mar-<br>23|30|XGBoos<br>t|70/30|0,64|24|30|6|0|6|0|20|0|25,24|8,03|13,4|5,66|
|28|Se busca un<br>colibrí|jun-<br>25|1033|XGBoos<br>t|80/20|0,89|864|1086|169|53|169|53|16,3<br>6|5,13|24,15|10,25|27,9|11,41|
|29|Camino a<br>Roma|dec-<br>22|312|Random<br>Forest|70/30|1,85|265|328|47|16|47|16|15,0<br>6|5,13|14,31|3,02|15,5|6,05|
|30|Entre Patas|jul-<br>25|32|Random<br>Forest|75/25|1,97|40|33|8|1|8|1|25|3,12|18,75|7,12|20,8|7,57|



pág. 82 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **Anexo 4: Prototipos** 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **Anexo 5: Metodología de Desarrollo de software** 

**Tabla 14** 

_Aplicación de Scrum durante el desarrollo del Sistema de Soporte a Decisiones_ 

|**Sprint**|**Objetivo**|**Actividades desarrolladas**|**Entregable**|
|---|---|---|---|
|**Sprint**<br>**1**|Definir la<br>solución<br>tecnológica|Levantamiento de requerimientos,<br>identificación de historias de usuario,<br>diseño de arquitectura, modelado de la<br>base de datos y definición del flujo<br>del sistema.|Arquitectura del SSD y<br>Product Backlog<br>aprobado.|
|**Sprint**<br>**2**|Preparar la<br>información<br>histórica|Recolección, limpieza, depuración,<br>transformación y estructuración de los<br>1,280 registros históricos provenientes<br>de la Editorial Ámbar.|Dataset consolidado y<br>preparado para el<br>entrenamiento de<br>modelos.|
|**Sprint**<br>**3**|Construir el<br>modelo<br>predictivo|Entrenamiento y evaluación de los<br>algoritmos XGBoost, Random Forest<br>y LSTM, comparación mediante<br>MAE, RMSE, MAPE y tiempo de<br>procesamiento.|Modelo predictivo<br>optimizado y<br>seleccionado.|
|**Sprint**<br>**4**|Integrar y<br>validar el<br>sistema|Desarrollo del Dashboard en<br>Streamlit, integración del modelo<br>predictivo, ejecución de pruebas<br>funcionales, validación de resultados<br>y despliegue del SSD.|Sistema de Soporte a<br>Decisiones<br>completamente<br>operativo.|



**Tabla 15** _Aplicación de CRISP-DM en el desarrollo del modelo predictivo_ 

|**Fase**|**Aplicación en la investigación**|
|---|---|
|Comprensión del<br>negocio|Identificación del problema de sobrestock, quiebre de stock y baja<br>precisión en la planificación editorial.|
|Comprensión de<br>los datos|Exploración de los registros históricos de ventas correspondientes al<br>período 2022–2025.|
|Preparación de los<br>datos|Limpieza, transformación, integración y normalización de los 1,280<br>registros históricos utilizando Python y Pandas.|
|Modelado|Entrenamiento y comparación de los algoritmos XGBoost, Random<br>Forest y LSTM.|
|Evaluación|Comparación del desempeño mediante MAE, RMSE, MAPE, tiempo<br>de procesamiento y validación estadística utilizando SPSS.|
|Despliegue|Implementación del modelo seleccionado dentro del Sistema de<br>Soporte a Decisiones desarrollado en Streamlit.|



Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **Tabla 16** 

|**Scrum**|**CRISP-DM**|
|---|---|
|Gestionó el proyecto de software.|Gestionó el ciclo de vida del modelo de aprendizaje<br>automático.|
|Organizó el trabajo mediante<br>Sprints.|Organizó el procesamiento de los datos.|
|Controló los entregables<br>funcionales.|Controló la calidad de los modelos predictivos.|
|Permitió la entrega incremental del<br>sistema.|Permitió mejorar continuamente la precisión del<br>modelo.|
|Facilitó la integración del<br>Dashboard.|Facilitó el entrenamiento y evaluación de los<br>algoritmos.|



Implementación de un sistema de soporte a decisiones con aprendizaje automático para mejorar la predicción de la demanda bibliográfica en la editorial Ambar, 2026 

## **Anexo 6: Población, muestra y muestreo** 

## **Tabla 17** 

_Población, muestra y muestreo_ 

|**Elemento**|**Descripción**|
|---|---|
|Unidad de análisis|Registro histórico de demanda bibliográfica|
|Población|Registros históricos del segmento de lectores de 9 a 17 años<br>(2022–2025)|
|Tamaño de la<br>población|1 280 registros|
|Muestra|1 280 registros|
|Muestra piloto|30 registros (Test–Retest)|
|Tipo de muestreo|No probabilístico|
|Técnica de muestreo|Por criterio (intencional)|



