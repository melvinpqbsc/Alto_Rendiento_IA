## Entremaniento 
# Nivel Intermedio: Cronograma del Curso de Machine Learning
### 28 de septiembre de 2026 → 2 de julio de 2027 (IOAI 2027: Singapur, 4–10 de julio)
Plataforma: [ioai.artix.tech](https://ioai.artix.tech/) · se desarrolla en paralelo con el Nivel Inicial (septiembre–diciembre)
 
---
 
## 0. Supuestos
 
| Ítem | Supuesto |
|---|---|
| Encuentros | 1 por semana, 2 h, identificados por el **lunes** de cada semana |
| Tiempo de trabajo fuera de clase | 4–5 h/semana (más que en el nivel inicial) |
| Requisito de entrada | Escribe funciones y bucles en Python sin ayuda; sabe qué es una derivada y una matriz |
| Calendario | Primer período 28 sep – 14 dic · receso de verano · 1 feb – 2 jul |
| Sesiones | **31 encuentros** (se descuentan feriados en lunes y Carnaval) |
 
Si el curso se dicta otro día de la semana, o con otro calendario de feriados, basta con mover las filas marcadas como feriado: 12 oct, 2 nov, 20 nov, 25 dic, 8–9 feb, 26 mar, 21 abr, 27 may.
 
**Tipos de sesión:**
**[A]** clase expositiva del profesor (≈11 en total) · **[B]** laboratorio, los estudiantes avanzan en la plataforma · **[C]** seminario de estudiantes (20 min + notebook ejecutable) · **[D]** sprint / simulacro, conjunto de prueba oculto, tabla de posiciones pública.
 
**Apertura fija de 15 minutos cada semana:** tabla de posiciones en pantalla → "bug de la semana" presentado por un estudiante → resumen de una diapositiva de la semana anterior, a cargo de un estudiante rotativo.
 
---
 
## 1. Visión general
 
| Bloque | Fechas | Sesiones | Tema |
|---|---|---|---|
| **1. Puente** | 28 sep – 26 oct | 4 | Repaso: Python/NumPy, matemática para deep learning, ML clásico en síntesis |
| **2. Redes neuronales y PyTorch** | 9 nov – 14 dic | 6 | Perceptrón → backpropagation → PyTorch → entrenar bien |
| **☀ Verano** | Enero 2027 | asincrónico | ML clásico / datos tabulares + Kaggle |
| **3. Visión por computadora** | 1 feb – 29 mar | 8 | CNN, transfer learning, detección/segmentación, modelos generativos |
| **4. Lenguaje, audio, multimodal** | 5 abr – 24 may | 8 | Embeddings, atención, transformers, LLM, CLIP, Whisper |
| **5. Preparación para la competencia** | 31 may – 28 jun | 5 | Repaso de ML clásico, problemas de ediciones anteriores, simulacro de 6 horas, cierre |
 
---
 
## 2. Semana por semana
 
### Bloque 1: Puente (repaso acelerado del contenido del nivel inicial)
 
Objetivo: en 4 sesiones, asegurar que todos tengan exactamente las herramientas que el deep learning da por sabidas. Quienes ya dominan el contenido vencen al "jefe" (*boss*) de esos niveles en la plataforma y actúan como monitores.
 
| Sem | Semana del | Sesión | Tipo | Entrega al inicio de la clase |
|---|---|---|---|---|
| 1 | **28 sep** | **Inicio + diagnóstico.** Qué es la IOAI. Creación de cuentas, test de nivel *en clase*, configuración de Colab. Notebook diagnóstico de 45 min (NumPy, una derivada, un ajuste con sklearn) para confirmar quién va en cada nivel. | [A] | — |
| 2 | 5 oct | **Python y NumPy para tensores**: formas (*shapes*), indexación, *broadcasting*, vectorización, `reshape`/`axis`. El modelo mental que PyTorch reutiliza en todo. | [A] | Test de nivel hecho, niveles de Python superados |
| — | 12 oct | *Feriado. Asincrónico: pregunta del día, racha de 5 días.* | — | — |
| 3 | 19 oct | **Paquete de matemática para DL**: vectores, producto punto, matriz × vector como "una capa"; derivadas, regla de la cadena, gradiente; descenso de gradiente a mano; probabilidad → softmax → logaritmo → entropía cruzada. | [A] | **B1: Ejercicios de NumPy** (vectorizar 6 funciones con bucles, reportar la aceleración) |
| 4 | 26 oct | **ML clásico en una sesión**: entrenamiento/validación/prueba, sobreajuste, validación cruzada, *accuracy* vs precisión/recall/F1, `fit/predict` de sklearn. Dos seminarios de estudiantes de 15 min (kNN, árboles de decisión). | [C] | **B2: Descenso de gradiente a mano** (1-D y 2-D, gráfico de contornos, romperlo con una mala tasa de aprendizaje) |
| — | 2 nov | *Feriado. **Sprint 0** asincrónico: se publica el lunes, se entrega el viernes. Limpiar un CSV desordenado, ajustar dos modelos de sklearn, reportar métricas.* | [D] | Sprint 0 |
 
**Punto de control del bloque (semana 4):** **B3 — Regresión lineal y logística desde cero** en NumPy, comparadas con sklearn sobre la misma partición. Es la puerta de entrada: contiene todas las ideas sobre las que se construye el Bloque 2.
 
### Bloque 2: Redes neuronales y PyTorch
 
| Sem | Semana del | Sesión | Tipo | Entrega |
|---|---|---|---|---|
| 5 | 9 nov | **Perceptrón → MLP.** Propagación hacia adelante en papel; funciones de activación (ReLU, sigmoide, tanh) y por qué importa la no linealidad. | [A] | **B3** + informe del Sprint 0 |
| 6 | 16 nov | **Backpropagation.** La clase que no se debe delegar. Regla de la cadena sobre un grafo computacional pequeño, despacio, en la pizarra. | [A] | Cuota semanal de la plataforma |
| 7 | 23 nov | **PyTorch**: tensores, `autograd`, `nn.Module`, `DataLoader`, el bucle de entrenamiento de 5 líneas, CPU vs GPU. | [A] | **P1: Motor de diferenciación automática desde cero** (estilo micrograd, entrenar un MLP sobre "two moons") |
| 8 | 30 nov | **Funciones de pérdida, inicialización, batch norm.** Seminarios: MSE vs MAE vs entropía cruzada; inicialización de pesos; batch norm. | [C] | **P2: MLP sobre Fashion-MNIST + tabla de ablación** (una variable a la vez) |
| 9 | 7 dic | **Entrenar bien**: SGD, mini-batch, momentum, Adam/AdamW, tasas de aprendizaje y *schedules*; dropout, weight decay, early stopping. | [A] | **P3: Carrera de optimizadores** (SGD / momentum / Adam / AdamW, un gráfico, un párrafo) |
| 10 | 14 dic | **Sprint 1**: el mejor modelo que se pueda entrenar en 15 minutos de GPU, evaluado con un conjunto de prueba oculto. Luego, retrospectiva + presentación del plan de verano. | [D] | Sprint 1 |
 
### ☀ Verano (enero): asincrónico, con seguimiento público
 
El programa de la IOAI sigue exigiendo ML clásico (árboles, gradient boosting, SVM, PCA, k-means, t-SNE/UMAP), y los problemas tabulares de competencia suelen ganarse con esas técnicas. El verano es el lugar para eso. Cada estudiante elige un nivel:
 
- **Bronce**: mantener la racha en la plataforma; superar los niveles de ML clásico.
- **Plata**: una competencia Kaggle Playground, ≥10 envíos, bitácora de 1 página. Debe probar gradient boosting (XGBoost/LightGBM).
- **Oro**: Plata + **S1 — Informe no supervisado**: PCA, k-means y UMAP sobre un conjunto de datos real (por ejemplo, indicadores socioeconómicos por municipio o región), ponerle nombre a los clústeres y argumentar si significan algo.
Un mensaje por semana, no más.
 
### Bloque 3: Visión por computadora
 
| Sem | Semana del | Sesión | Tipo | Entrega |
|---|---|---|---|---|
| 11 | 1 feb | **Reinicio.** Muestra de los trabajos de verano. Repaso de 30 min del bucle de entrenamiento (también es la puerta de entrada para los egresados del nivel inicial que se suman ahora; ver §4). | [C] | Bitácora de verano |
| — | 8 feb | *Carnaval.* | — | — |
| 12 | 15 feb | **Convolución**: qué es un filtro; construir uno en NumPy y luego con `nn.Conv2d`; *padding*, *stride*, *pooling* (máximo/promedio). | [A] | Cuota semanal |
| 13 | 22 feb | **Arquitecturas CNN**: de LeNet a ResNet, conexiones residuales. Laboratorio. | [B] | **P4: CNN desde cero sobre CIFAR-10** |
| 14 | 1 mar | **Transfer learning y fine-tuning**: ResNet preentrenada, congelar capas vs ajuste completo. La habilidad de competencia más útil del año. | [A] | Cuota semanal |
| 15 | 8 mar | **Aumentación de datos y datos reales.** Seminario: aumentación (volteos, recortes, ruido) y qué aporta. | [C] | **P5: CNN desde cero vs ResNet ajustada**, mismo presupuesto de 15 min de GPU |
| 16 | 15 mar | **Detección y segmentación**: YOLO (práctico), U-Net. Seminarios. | [C] | **P6: Tu propio dataset de 200 imágenes**, 4 clases, partición correcta, clasificador + informe de aumentación |
| 17 | 22 mar | **Panorama generativo y autosupervisado**: autoencoders, GAN, difusión, aprendizaje autosupervisado. Seminarios, nivel práctico. | [C] | **P7: Autoencoder sobre MNIST** + gráfico del espacio latente |
| 18 | 29 mar | **Sprint 2 (visión)**: clasificación de imágenes en un dataset nuevo, conjunto de prueba oculto. | [D] | Sprint 2 |
 
### Bloque 4: Lenguaje, audio, multimodal
 
| Sem | Semana del | Sesión | Tipo | Entrega |
|---|---|---|---|---|
| 19 | 5 abr | **Embeddings y tokenización**: texto (BPE, vocabulario), parches de imagen, audio. *Padding* de secuencias de longitud variable. | [A] | Informe del Sprint 2 |
| 20 | 12 abr | **Atención**, paso a paso en la pizarra: *queries*, *keys*, *values*, softmax, enmascaramiento. | [A] | Cuota semanal |
| 21 | 19 abr | **Transformers y BERT**: bloques codificadores, codificación posicional; ajustar un BERT en español (p. ej. BETO). | [B] | **P8: Atención desde cero** en PyTorch, verificada contra `nn.MultiheadAttention` |
| 22 | 26 abr | **Visión-texto**: ViT, CLIP, clasificación *zero-shot*. Seminarios. | [C] | **P9: Análisis de sentimiento en español**: BERT en español vs línea base TF-IDF + regresión logística |
| 23 | 3 may | **Modelado de lenguaje**: construir un GPT pequeño (el camino de nanoGPT de Karpathy), muestreo, temperatura. | [A] | **P10: CLIP zero-shot sobre fotos propias + galería de errores** · **Propuesta de proyecto** (1 página, en parejas) |
| 24 | 10 may | **LLM preentrenados** (de código abierto y vía API), *prompting*, construcción de un conjunto de evaluación; **fine-tuning eficiente en parámetros (LoRA)**. | [A] | **P11: GPT pequeño** entrenado sobre un corpus de texto en español |
| 25 | 17 may | **Audio**: Whisper, HuBERT; modelos codificador-decodificador. Seminarios. | [C] | **P12: Benchmark de prompts**: conjunto de evaluación de 30 preguntas, 3 estrategias de *prompting*, *accuracy* con barras de error |
| 26 | 24 may | **Sprint 3 (multimodal)**: tarea de texto o imagen+texto, conjunto de prueba oculto. | [D] | Sprint 3 |
 
### Bloque 5: Preparación para la competencia
 
| Sem | Semana del | Sesión | Tipo | Entrega |
|---|---|---|---|---|
| 27 | 31 may | **Día tabular y clásico**: gradient boosting, clustering, PCA/t-SNE/UMAP, ingeniería de variables, datos faltantes. Ejercicio cronometrado al final. | [A] | **P13: Whisper con distintos acentos del español** (WER por región) |
| 28 | 7 jun | **Técnica de competencia con problemas de ediciones anteriores de la IOAI**: leer el problema, línea base en 20 minutos, después iterar; manejo del tiempo; interpretar métricas. | [B] | Problema de edición anterior n.º 1 |
| 29 | 14 jun | **Presentaciones de proyectos** (en parejas, 8 min cada una). | [C] | **Proyecto** |
| 30 | 21 jun | **Simulacro completo, 6 horas** (los días de competencia de la IOAI duran 6 h en máquinas con GPU). Idealmente un sábado. Problemas de ediciones anteriores, solo en inglés, sin ayuda. | [D] | — |
| 31 | 28 jun | **Análisis del simulacro + cierre.** Repaso de las soluciones del simulacro; qué sigue (universidad, investigación, próximas competencias). | [A] | Reflexión sobre el simulacro |
 
---
 
## 3. Cobertura del programa (programa IOAI 2026 → semana)
 
| Área del programa | Dónde |
|---|---|
| Python, NumPy, pandas, Matplotlib, sklearn | Sem 1–4, plataforma |
| PyTorch, tensores, CPU/GPU | Sem 7 en adelante |
| Regresión lineal/logística, kNN, árboles, métricas, validación cruzada, sobreajuste | Sem 3–4 (B3), verano, sem 27 |
| Ensambles, SVM, L1/L2 | Verano, sem 27 |
| PCA, k-means, t-SNE/UMAP, DBSCAN | Verano (S1), sem 27 |
| Perceptrón, backprop, activaciones, pérdidas, MLP | Sem 5–8 |
| SGD/Adam, tasa de aprendizaje, dropout, weight decay, inicialización, batch norm | Sem 8–9 |
| Capas convolucionales, pooling, clasificación, codificadores preentrenados, aumentación | Sem 12–15 |
| Detección, segmentación | Sem 16 |
| Autoencoders, GAN, difusión, autosupervisado | Sem 17 |
| Embeddings, atención, transformers, BERT | Sem 19–22 |
| CLIP, visión-texto | Sem 22 |
| Modelado de lenguaje, LLM preentrenados, fine-tuning (completo + PEFT) | Sem 23–24 |
| Codificador-decodificador, audio (Whisper, HuBERT) | Sem 25 |
 
---
 
## 4. Cómo conviven los dos niveles
 
- **El Bloque Puente también sirve para clasificar.** El diagnóstico de la semana 1 y el B3 indican, a fines de octubre, quién conviene que pase al nivel inicial y quién del nivel inicial podría subir.
- **Los egresados del nivel inicial se suman en febrero.** La semana 11 está pensada como su punto de entrada. En enero reciben un paquete de nivelación de 2 semanas: B3 + P2 (ablación del MLP) + los videos de backpropagation y PyTorch (3Blue1Brown, Karpathy). Si se suman muchos, agregar una sesión extra de nivelación [B] en la semana 12.
- **Los estudiantes intermedios como monitores del nivel inicial**, una o dos veces por mes. Explicarle NumPy a un principiante es el mejor repaso posible, y le quita carga al profesor.
- **Sprints compartidos.** El Sprint 1 (14 dic) puede tener una variante para el nivel inicial (solo sklearn) sobre el mismo dataset y en la misma tabla de posiciones. Les da a los principiantes un objetivo concreto.
---
 
## 5. Evaluación
 
| Componente | Peso |
|---|---|
| Progreso en la plataforma (niveles superados) | 20% |
| Trabajos prácticos (B1–B3, P1–P13) | 35% |
| Seminarios presentados | 15% |
| Sprints + simulacro | 10% |
| Proyecto | 20% |
 
Cada notebook se evalúa con cuatro criterios, de 0 a 2 cada uno: **se ejecuta de principio a fin / es correcto / está justificado / está bien comunicado**, y termina con un párrafo en lenguaje sencillo sobre qué significan los números. Antes de que lo corrija el profesor, lo revisa un compañero.
 
---
 
## 6. Notas prácticas
 
- **Recursos de cómputo**: Colab gratuito alcanza hasta abril, aproximadamente. Desde el Bloque 4 (GPT pequeño, LoRA, Whisper) conviene prever las horas gratuitas de GPU de los notebooks de Kaggle o una máquina de laboratorio de la universidad; organizarlo en marzo.
- **El simulacro de 6 horas (sem 30)** necesita un aula, GPU y un sábado. Reservarlo en mayo.
- **Idioma**: las clases y los materiales van en español, pero la plataforma, la documentación y la competencia están en inglés. No traducir la plataforma: esa fricción también es entrenamiento.
- **Es esperable una deserción** del 30–50% hacia febrero; ningún trabajo práctico debe depender de uno de un bloque anterior.Çk
