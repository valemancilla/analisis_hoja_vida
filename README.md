# 📄 Análisis de Hojas de Vida con IA

Repositorio del curso **Inteligencia Artificial 2**, dedicado al aprendizaje práctico de
**LangChain** y modelos de lenguaje (LLMs). El proyecto avanza de forma progresiva desde
los primeros ejemplos con modelos de lenguaje hasta una aplicación completa: un
**analizador inteligente de currículums (CVs)** construido con Streamlit.

---

## 📝 Descripción del Proyecto

Este proyecto reúne el material desarrollado a lo largo del curso, dividido en tres temas
que construyen conocimiento de manera incremental:

- **Tema 1 — Primeros pasos con LLMs:** ejemplos introductorios de invocación de modelos
  (OpenAI y Google Gemini) y un chatbot interactivo con Streamlit.
- **Tema 2 — Prompts, cadenas y salidas estructuradas:** uso de plantillas de prompts,
  cadenas con LCEL (LangChain Expression Language) y respuestas estructuradas con Pydantic.
  Incluye el proyecto estrella: **CV Analyzer**.
- **Tema 3 — RAG (Retrieval-Augmented Generation):** carga de documentos, división de texto
  en *chunks*, generación de *embeddings* y carga desde Google Drive.

El componente principal es **CV Analyzer** (`Tema_2/cv_analyzer/`), una aplicación web que
recibe un currículum en PDF y una descripción de puesto, y devuelve un análisis profesional
del candidato generado por un LLM: experiencia, habilidades, fortalezas, áreas de mejora y
un porcentaje de ajuste al puesto.

---

## 🎯 Objetivo

Aprender e implementar los conceptos fundamentales del desarrollo de aplicaciones con
modelos de lenguaje usando **LangChain**, aplicándolos a un caso de uso real: **automatizar
la evaluación de hojas de vida**.

Objetivos específicos:

- Conectar y consumir distintos proveedores de LLMs (OpenAI y Google Gemini).
- Diseñar *prompts* especializados que guíen el comportamiento del modelo.
- Obtener respuestas en **formato estructurado y validado** mediante Pydantic.
- Procesar documentos PDF para extraer y analizar su contenido.
- Construir interfaces web interactivas con **Streamlit**.
- Aplicar técnicas de **RAG**: *loaders*, *text splitters* y *embeddings*.

---

## ✨ Características Destacadas

- 🤖 **Análisis de CVs con IA:** evalúa automáticamente un currículum frente a una descripción
  de puesto y genera un informe profesional.
- 📊 **Salida estructurada y validada:** los resultados se modelan con Pydantic
  (`AnalisisCV`), garantizando datos consistentes (nombre, experiencia, habilidades,
  fortalezas, áreas de mejora y porcentaje de ajuste 0–100).
- 📄 **Procesamiento de PDF:** extrae el texto del currículum página por página.
- 🎯 **Porcentaje de ajuste ponderado:** experiencia (40%), habilidades técnicas (35%),
  formación (15%) y coherencia profesional (10%).
- 🧑‍💼 **Prompt de reclutador experto:** el modelo asume el rol de un reclutador senior con
  criterios de evaluación claros y objetivos.
- 💬 **Chatbot multimodelo:** soporta OpenAI y Gemini, con respuesta en *streaming* e
  historial de conversación.
- 🔌 **Soporte multiproveedor:** ejemplos tanto con OpenAI como con Google Gemini.
- 🔐 **Gestión segura de credenciales:** las claves de API se cargan desde un archivo `.env`
  (ignorado por git).

---

## 🛠️ Tecnologías Utilizadas

| Categoría | Herramientas |
|-----------|--------------|
| **Lenguaje** | Python 3.13 |
| **Framework LLM** | LangChain (`langchain`, `langchain-core`, `langchain-community`) |
| **Proveedores de LLM** | OpenAI (`langchain-openai`), Google Gemini (`langchain-google-genai`) |
| **Interfaz web** | Streamlit |
| **Validación de datos** | Pydantic |
| **Procesamiento de PDF** | PyPDF2 / PyPDFLoader |
| **RAG / Embeddings** | OpenAIEmbeddings, RecursiveCharacterTextSplitter, GoogleDriveLoader |
| **Variables de entorno** | python-dotenv |
| **Utilidades** | NumPy (similitud coseno) |

---

## 📁 Estructura del Proyecto

```
analisis_hoja_vida/
│
├── Tema_1/                          # Primeros pasos con LLMs
│   ├── hello_world.py              # Invocación básica con OpenAI (gpt-4o-mini)
│   ├── hello_world_gemini.py       # Invocación básica con Google Gemini
│   ├── hello_world_avanzado.py     # (ejemplo avanzado)
│   └── streamlit_chatbot.py        # Chatbot multimodelo con Streamlit + streaming
│
├── Tema_2/                          # Prompts, cadenas y salidas estructuradas
│   ├── output_parsers.py           # Salida estructurada con Pydantic (sentimiento)
│   ├── analisis_sentimientos.py    # (ejemplo de análisis de sentimientos)
│   ├── chat_prompt_template.py     # (plantillas de chat)
│   ├── ejemplo_runnables.py        # (ejemplos de Runnables / LCEL)
│   │
│   └── cv_analyzer/                # ⭐ Aplicación principal: Analizador de CVs
│       ├── app.py                  # Punto de entrada (carga .env y lanza la UI)
│       ├── models/
│       │   └── cv_model.py         # Modelo Pydantic AnalisisCV
│       ├── prompts/
│       │   └── cv_prompts.py       # Prompts del reclutador experto
│       ├── services/
│       │   ├── pdf_processor.py    # Extracción de texto del PDF
│       │   └── cv_evaluator.py     # Evaluación del CV con el LLM
│       └── ui/
│           └── streamlit_ui.py     # Interfaz de usuario (Streamlit)
│
├── Tema_3/                          # RAG: carga de documentos y embeddings
│   ├── document_loaders.py         # Carga de PDF con PyPDFLoader
│   ├── text_splitters.py           # División en chunks + resumen con LLM
│   ├── embeddings_langchain.py     # Embeddings + similitud coseno
│   └── google_drive_loader.py      # Carga de documentos desde Google Drive
│
├── .gitignore
└── README.md
```

---

## ▶️ Cómo Ejecutar el Analizador de CVs

1. **Crear y activar el entorno virtual** (PowerShell):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Instalar dependencias:**
   ```powershell
   pip install streamlit langchain langchain-openai langchain-community langchain-google-genai pydantic python-dotenv PyPDF2 numpy
   ```

3. **Configurar las credenciales** en `Tema_2/cv_analyzer/.env`:
   ```env
   OPENAI_API_KEY=tu_clave_de_openai
   GOOGLE_API_KEY=tu_clave_de_google   # opcional
   ```

4. **Ejecutar la aplicación:**
   ```powershell
   cd Tema_2\cv_analyzer
   streamlit run .\app.py
   ```

5. Abrir el navegador en **http://localhost:8501**, subir un CV en PDF, escribir la
   descripción del puesto y pulsar **"Analizar candidato"**.

> 💡 El PDF debe contener **texto seleccionable**; los PDF que son solo imágenes escaneadas
> no permiten extraer el texto.

---

## 👥 Autores

- **valentina mancilla** 


