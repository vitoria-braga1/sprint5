import pandas as pd
import plotly.express as px
from pathlib import Path
import streamlit as st

df = pd.read_csv(Path("Data/vehicles.csv"))
fig = px.histogram(df, x = 'days_listed')

st.title("projeto 5-teste")
st.plotly_chart(fig)