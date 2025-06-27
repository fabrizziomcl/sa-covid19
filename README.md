# Análisis de Sentimiento Geolocalizado Sobre Vacunas Contra el COVID-19 en Twitter/X


El presente proyecto analiza el sentimiento de los usuarios de Twitter
hacia las vacunas contra la COVID-19 incorporando la geolocalización de las publicaciones
para identificar variaciones regionales en la percepción. Se recolectaron y procesaron, a
través de un análisis de datos exploratorio, tweets georreferenciados relacionados con
la vacunación, los cuales luego fueron clasificados como positivos, negativos o neutros
mediante técnicas de procesamiento de lenguaje natural. Posteriormente, se mapearon los
resultados de sentimiento a nivel geográfico, revelando patrones locales de aceptación y
rechazo a las vacunas. 

---

## Demo en línea

[Ver demo en Streamlit Cloud]((https://tf-pacd-sentiment-analysis-twitter-covid19.streamlit.app/))

---


## ⚙️ Instrucciones de instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/fabrizziomcl/sa-covid19.git
````

### 2. Crea y activa un entorno con conda

```bash
conda create -y -n covid_sentiment python=3.11
conda activate covid_sentiment
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación Streamlit

```bash
streamlit run sentiment_dashboard.py
```

## 🗂 Dataset

El dataset usado se encuentra en [Streamlit]([https://streamlit.io/](https://www.kaggle.com/datasets/kaushiksuresh147/covidvaccine-tweets))
---


