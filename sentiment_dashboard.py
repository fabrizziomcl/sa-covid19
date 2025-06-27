import streamlit as st
import pandas as pd
import plotly.express as px
from pandas import Period

# Escala de color personalizada
custom_scale = [
    (0.0, "darkred"),
    (0.15, "red"),
    (0.25, "orangered"),
    (0.40, "orange"),
    (0.5, "yellow"),
    (0.60, "yellowgreen"),
    (0.75, "limegreen"),
    (0.85, "green"),
    (1.0, "darkgreen")
]
rc = [-1, 1]

st.set_page_config(layout="wide", page_title="Mapa de Sentimientos COVID-19")
st.title("🌍 Comparación de Sentimientos por País")

# --- Cargar datos resumidos ya agrupados ---
@st.cache_data
def cargar_datos():
    df = pd.read_csv("tweets_resumen_mensual.csv")
    df["AñoMes"] = pd.PeriodIndex(df["AñoMes"], freq="M")
    df["year_month_str"] = df["year_month_str"].astype(str)
    return df

df = cargar_datos()

# --- Eventos clave ---
eventos_globales = {
    "Todos": None,
    "Surgimiento de la variante Delta (Jun 2021)": Period("2021-06"),
    "Surgimiento de la variante Ómicron (Nov 2021)": Period("2021-11"),
    "Anuncio de eficacia de la vacuna Pfizer (Nov 2020)": Period("2020-11"),
    "Inicio de la vacunación masiva global (Ene 2021)": Period("2021-01"),
    "Reapertura global tras el confinamiento (Jun 2021)": Period("2021-06"),
}

# --- Interfaz ---
evento = st.selectbox("🗓️ Selecciona un evento clave", list(eventos_globales.keys()))
fecha = eventos_globales[evento]

# --- Filtrar por evento ---
df_evento = df.copy()
if fecha:
    df_evento = df[df["AñoMes"] == fecha]

# --- Visualización por país (mapa de coropletas) ---
st.subheader("📊 Mapa de Sentimiento Promedio por País")
df_grouped = df_evento.groupby("País", as_index=False)["Score"].mean()

fig = px.choropleth(
    df_grouped,
    locations="País",
    locationmode="country names",
    color="Score",
    color_continuous_scale=custom_scale,
    range_color=rc,
)

fig.update_layout(
    title=f"🌐 Sentimiento Promedio por País – {evento}" if fecha else "🌐 Sentimiento Promedio Global por País",
    geo=dict(
        showframe=True, showcoastlines=True, coastlinecolor="Black",
        projection_type='natural earth', showland=True, landcolor="lightgray",
        subunitcolor="white", showlakes=True, lakecolor="lightblue"
    ),
    coloraxis_colorbar=dict(title="Sentimiento"),
    margin=dict(t=60, l=40, r=40, b=20),
    height=600
)
st.plotly_chart(fig, use_container_width=True)

# --- Evolución temporal del sentimiento ---
st.header("📈 Evolución del Sentimiento Promedio Mensual (2020–2022)")

df_avg = df.copy()
fig1 = px.choropleth(df_avg,
                     locations="País",
                     color="Score",
                     hover_name="País",
                     animation_frame="year_month_str",
                     color_continuous_scale=custom_scale,
                     range_color=rc,
                     title="Evolución Mensual del Sentimiento Promedio por País (2020–2022)",
                     locationmode="country names")
fig1.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
st.plotly_chart(fig1)

# --- Top 5 países negativos por mes ---
st.header("🚨 Top 5 Países con Sentimiento Más Negativo (2020–2022)")
top5_negativos = df.sort_values(['year_month_str', 'Score']).groupby('year_month_str').head(5)

fig_neg = px.bar(top5_negativos,
                 x='País',
                 y='Score',
                 color='Score',
                 color_continuous_scale=custom_scale,
                 range_color=rc,
                 animation_frame='year_month_str',
                 title='Top 5 Países con Sentimiento Más Negativo')
fig_neg.update_layout(yaxis=dict(range=[-1, 0], dtick=0.25))
fig_neg.update_traces(width=0.4)
st.plotly_chart(fig_neg)

# --- Top 5 países positivos por mes ---
st.header("🌟 Top 5 Países con Sentimiento Más Positivo (2020–2022)")
top5_positivos = df.sort_values(['year_month_str', 'Score'], ascending=False).groupby('year_month_str').head(5)

fig_pos = px.bar(top5_positivos,
                 x='País',
                 y='Score',
                 color='Score',
                 color_continuous_scale=custom_scale,
                 range_color=rc,
                 animation_frame='year_month_str',
                 title='Top 5 Países con Sentimiento Más Positivo')
fig_pos.update_layout(yaxis=dict(range=[0, 1], dtick=0.25))
fig_pos.update_traces(width=0.4)
st.plotly_chart(fig_pos)
