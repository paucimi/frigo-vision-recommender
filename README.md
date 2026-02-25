# 🥗 SmartFridge: Vision-Based Recipe Recommender System
### *Sistema de Visión y Recomendación de Recetas Inteligente*

Este proyecto combina **Computer Vision**, **Procesamiento de Lenguaje Natural (NLP)** y **Sistemas de Recomendación** para automatizar la gestión de alimentos en un frigorífico y reducir el desperdicio de comida.

---

## 🇪🇸 Descripción del Proyecto
**SmartFridge** transforma una fotografía de la nevera en un inventario digital dinámico. A diferencia de los sistemas genéricos, este proyecto utiliza un enfoque de tres capas (Localización + OCR + LLM) para identificar con precisión marcas y productos específicos, cruzando estos datos con un motor de recomendaciones para sugerir qué cocinar.



## 🇺🇸 Project Description
**SmartFridge** leverages Artificial Intelligence to turn a simple photo of your refrigerator into a smart culinary experience. The system detects food items, manages a dynamic inventory, and recommends recipes based on what you actually have in stock.

---

## 🛠️ Arquitectura Técnica / Technical Stack

| Componente | Tecnología | Función |
| :--- | :--- | :--- |
| **Object Detection** | Google Vision API | Localizar alimentos (Bounding Boxes). |
| **Brand Recognition** | OCR (Google Vision) | Leer etiquetas y nombres específicos de productos. |
| **Text Normalization** | LLM (OpenAI/Gemini) | Mapear texto de etiquetas a ingredientes base (limpieza). |
| **Database** | SQLite | Almacenar inventario, fechas de entrada y estado. |
| **Recommendation** | TBD API | Motor de búsqueda de recetas basado en ingredientes. |
| **Environment** | Google Colab | Entorno de desarrollo colaborativo. |

---

## 🚀 Instalación y Uso / Setup & Usage

### 1. Requisitos / Prerequisites
* Cuenta de **Google Cloud** con la Vision API habilitada.
* API Key de **TBD**.
* Cuenta de **Kaggle** (para descargar datasets).

### 2. Configuración / Configuration
Sube tus archivos de credenciales a la raíz de tu entorno en Colab:
* `google_vision_key.json`
* `kaggle.json`

### 3. Ejecución / Execution
Abre el notebook `SmartFridge_Main.ipynb` y ejecuta las celdas en orden para:
1. Clonar el repositorio.
2. Procesar la imagen mediante la API de Google.
3. Normalizar ingredientes con el LLM.
4. Obtener sugerencias de recetas personalizadas.

---

## 📊 Esquema de Datos / Database Schema

El sistema mantiene la persistencia mediante una base de datos SQLite con la siguiente relación:



* **Inventario:** Almacena el `id`, `nombre_ocr`, `ingrediente_limpio` y `fecha_captura`.
* **Usuarios:** Almacena preferencias dietéticas y alergias para filtrar las recetas.

---

## 📅 Roadmap & Future Work / Trabajo Futuro

* [ ] **Deployment:** Crear una interfaz web con **Streamlit** o **Flask**.
* [ ] **Mobile App:** Integración con **Flutter** para capturar fotos desde el móvil.
* [ ] **Expiration Tracking:** Alertas automáticas de caducidad mediante OCR de fechas.
* [ ] **Edge AI:** Migrar el modelo a **AutoML Edge (TFLite)** para funcionamiento offline.

---

## 👥 Colaboradores / Contributors
* **Paola León** - AI & Vision Lead
* **Isabel Castrejon, David RH, Julio Cesar, JositoRené** - Data Engineering & API Integration
