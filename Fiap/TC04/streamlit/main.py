import streamlit as st
from simulacao import render as simulacao_page
from dashboard import render as dashboard_page
from notebook import render as notebook_page

st.sidebar.markdown("## Selecione uma página")

# Seletor de páginas
page = st.sidebar.selectbox(
    "",
    ["Simulação", "Dashboard", "Notebook"]
)

st.sidebar.markdown("---")


if page == "Simulação":
    st.sidebar.markdown(
        "🧪 **Simulação**  \n"
        "Execute o modelo de Machine Learning e simule perfis de pacientes."
    )
    simulacao_page()

elif page == "Dashboard":
    st.sidebar.markdown(
        "📊 **Dashboard**  \n"
        "Visualização dos principais indicadores e análises exploratórias."
    )
    dashboard_page()

elif page == "Notebook":
    st.sidebar.markdown(
        "📓 **Notebook**  \n"
        "Análise exploratória completa em formato de notebook."
    )
    notebook_page()
