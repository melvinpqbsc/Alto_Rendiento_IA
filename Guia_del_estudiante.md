# Guía del Estudiante: Nivel Intermedio de Machine Learning

Sep 22, 2026 · @Melvin Poveda

Este es un curso anual de deep learning que empieza el Oct 5, 2026 y termina a fines de junio de 2027. Nos vemos una vez por semana (2 horas), pero la mayor parte del aprendizaje ocurre fuera de clase: esperamos entre 4 y 5 horas semanales de trabajo tuyo.

## El curso en síntesis

El objetivo es que al final del año puedas entrenar, evaluar y explicar modelos de redes neuronales para imágenes, texto y audio. Seguimos el programa de la [Olimpiada Internacional de Inteligencia Artificial (IOAI)](https://ioai-official.org/syllabus/), cuya edición 2027 es en Singapur del 4 al 10 de julio.

La herramienta central es la plataforma [ioai.artix.tech](https://ioai.artix.tech/): ejercicios progresivos con un editor de código y un juez automático. La plataforma está en inglés, igual que la documentación de las librerías y la competencia; las clases son en español.

| Bloque | Fechas | Tema |
| --- | --- | --- |
| 1. Puente | 5 oct – 2 nov | Repaso de Python/NumPy, matemática para deep learning y ML clásico |
| 2. Redes neuronales y PyTorch | 9 nov – 14 dic | Perceptrón, backpropagation, PyTorch, cómo entrenar bien |
| Verano | Enero | Trabajo autónomo opcional: ML clásico y Kaggle |
| 3. Visión por computadora | 1 feb – 29 mar | CNN, transfer learning, detección, segmentación, modelos generativos |
| 4. Lenguaje, audio, multimodal | 5 abr – 24 may | Embeddings, atención, transformers, LLM, CLIP, Whisper |
| 5. Preparación final | 31 may – 28 jun | Problemas de ediciones anteriores, proyecto, simulacro de 6 horas |

Fechas que conviene anotar ya: Sprint 1 el 14 de diciembre, propuesta de proyecto el 3 de mayo, presentación del proyecto el 14 de junio y simulacro de 6 horas el 21 de junio (probablemente un sábado).

## Cómo funciona cada semana

Cada clase empieza con 15 minutos fijos:

1. Revisamos la tabla de posiciones de la plataforma.
2. **Bug de la semana**: un estudiante muestra un error que le costó más de 30 minutos y cómo lo resolvió.
3. **Resumen**: un estudiante presenta en una diapositiva lo que vimos la semana anterior.

Después viene uno de cuatro tipos de sesión:

| Tipo | Qué pasa | Qué se espera de ti |
| --- | --- | --- |
| Clase | El profesor explica un tema difícil (unas 11 veces en el año) | Venir con la cuota semanal hecha y preguntas |
| Laboratorio | Trabajas en la plataforma o en tu notebook; el profesor circula | Traer dudas concretas, ayudar a tus compañeros |
| Seminario | Un estudiante enseña un tema durante 20 minutos | Si presentas: notebook que funcione. Si escuchas: una pregunta escrita enviada antes |
| Sprint | Problema cronometrado, evaluado con datos de prueba ocultos | Trabajo individual, sin ayuda externa |

## Tus responsabilidades

Este curso funciona si tú haces el trabajo. El profesor guía, pero no va a resolverte los problemas.

1. **Cumplir la cuota semanal en la plataforma.** La cantidad de ejercicios se acuerda en la primera clase; tu progreso queda registrado y se revisa cada semana.
2. **Entregar los trabajos prácticos a tiempo.** Hay uno cada dos semanas aproximadamente. Se entregan al inicio de la clase indicada.
3. **Presentar seminarios.** Durante el año enseñarás 3 o 4 temas a tus compañeros. Se asignan con dos semanas de anticipación.
4. **Enviar una pregunta escrita antes de cada seminario** de otro compañero.
5. **Revisar el trabajo de un compañero** antes de cada entrega, con la rúbrica de cuatro criterios.
6. **Participar en la apertura de la clase** cuando te toque: bug de la semana o resumen.
7. **Asistir y avisar.** Si no puedes venir, avisa antes de la clase.
8. **Buscar ayuda en el orden correcto:** primero la documentación, después dos compañeros, y recién entonces el profesor.
9. **Ayudar a los demás.** Algunas veces al mes acompañarás a estudiantes del nivel inicial. Explicar algo es la mejor forma de aprenderlo.

## Reglas de los trabajos

- **Todo trabajo es un notebook de Colab que se ejecuta de principio a fin** en un entorno nuevo. Si no se ejecuta, no cuenta como entregado.
- **Todo trabajo se guarda en tu repositorio privado del trabajo**, que recibes por GitHub Classroom. No hay que enviar nada: cuenta la última versión guardada antes del inicio de la clase. El paso a paso está en la sección [Antes de empezar: GitHub](README.md#antes-de-empezar-github) del README.
- **Todo notebook termina con un párrafo** en lenguaje sencillo: qué significan los resultados y qué probarías después. Sin ese párrafo, no hay nota.
- **Los resultados se comparan con una línea base.** Un 90% de accuracy no dice nada si no sabemos cuánto logra un modelo simple.
- **Los sprints y el simulacro son individuales.** No se habla con otros ni se usa ayuda externa durante el tiempo cronometrado.

### Uso de herramientas de IA

Puedes usar asistentes de IA para entender un error, repasar un concepto o consultar cómo se usa una función. No puedes pedirle a una IA que escriba la solución de un trabajo práctico, ni entregar código que no sepas explicar línea por línea. En la competencia no hay asistentes: lo que no aprendas a hacer tú, no lo vas a poder hacer ahí.

Si usaste IA en un trabajo, agrega una línea al final diciendo para qué. El profesor puede pedirte que expliques cualquier parte de tu código.

## Evaluación

| Componente | Peso |
| --- | --- |
| Trabajos prácticos | 35% |
| Progreso en la plataforma (niveles superados) | 20% |
| Proyecto final (en parejas) | 20% |
| Seminarios presentados | 15% |
| Sprints y simulacro | 10% |

Cada notebook se evalúa con cuatro criterios, de 0 a 2 puntos cada uno: **se ejecuta**, **es correcto**, **está justificado** y **está bien comunicado**. Antes de entregar, asígnate tu propio puntaje: aprender a evaluar tu trabajo es parte del curso.

## Antes de la primera clase (Oct 5, 2026)

- [ ] Crear una cuenta en [ioai.artix.tech](https://ioai.artix.tech/) y leer la [guía de la plataforma](https://ioai.artix.tech/guide) (5 minutos).
- [ ] Tener una cuenta de Google y abrir un notebook en [Google Colab](https://colab.research.google.com/) para comprobar que funciona.
- [ ] Crear una cuenta en [GitHub](https://github.com/), enviarle tu usuario al profesor y conectar Colab con GitHub. Instrucciones en [Antes de empezar: GitHub](README.md#antes-de-empezar-github).
- [ ] Traer una computadora portátil a cada clase, si es posible.
- [ ] No hacer todavía el test de nivel: lo hacemos juntos en la primera clase.

## Si faltas o te atrasas

Ningún trabajo práctico depende de uno anterior, así que siempre puedes reincorporarte. Si faltaste, avanza en la plataforma con los niveles de esa semana y pide a un compañero sus apuntes. Si vas a entregar tarde, avisa antes de la fecha, no después.

## Contacto

- Profesor: @Melvin Poveda
- Día, horario y aula: por definir
- Canal del grupo: por definir
