import pandas as pd
import plotly.express as px
from pathlib import Path
import streamlit as st

df = pd.read_csv(Path("Data/vehicles.csv"))

df["model_year"] = df["model_year"].fillna(0).astype(int)

st.title("projeto 5-teste")


tipos = st.multiselect(
    "Selecione o(s) tipo(s) de carro:",
    df["type"].dropna().unique(),
    default=list(df["type"].dropna().unique())
)
df_filtrado = df[df["type"].isin(tipos)]

if not df_filtrado.empty:
    df_tipo = df_filtrado.groupby("type").size().reset_index(name="count")

    fig = px.bar(
        df_tipo,
        x="type",
        y="count",
        title="📊 Quantidade de Carros por Tipo",
        labels={"type": "Tipo de Carro", "count": "Quantidade"}
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ Nenhum carro encontrado para esse(s) tipo(s).")