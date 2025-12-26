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


st.sidebar.markdown(
    """
    <a href="https://github.com/GustavOnaga/Fiap/tree/main/Fiap/TC04" target="_blank"
       style="text-decoration:none; display:flex; align-items:center; gap:8px;">
        <svg height="20" viewBox="0 0 16 16" width="20" aria-hidden="true">
            <path fill="currentColor"
                  d="M8 0C3.58 0 0 3.58 0 8
                     c0 3.54 2.29 6.53 5.47 7.59
                     .4.07.55-.17.55-.38
                     0-.19-.01-.82-.01-1.49
                     -2.01.37-2.53-.49-2.69-.94
                     -.09-.23-.48-.94-.82-1.13
                     -.28-.15-.68-.52-.01-.53
                     .63-.01 1.08.58 1.23.82
                     .72 1.21 1.87.87 2.33.66
                     .07-.52.28-.87.51-1.07
                     -1.78-.2-3.64-.89-3.64-3.95
                     0-.87.31-1.59.82-2.15
                     -.08-.2-.36-1.02.08-2.12
                     0 0 .67-.21 2.2.82
                     .64-.18 1.32-.27 2-.27
                     .68 0 1.36.09 2 .27
                     1.53-1.04 2.2-.82 2.2-.82
                     .44 1.1.16 1.92.08 2.12
                     .51.56.82 1.27.82 2.15
                     0 3.07-1.87 3.75-3.65 3.95
                     .29.25.54.73.54 1.48
                     0 1.07-.01 1.93-.01 2.2
                     0 .21.15.46.55.38
                     A8.013 8.013 0 0 0 16 8
                     C16 3.58 12.42 0 8 0z">
            </path>
        </svg>
        <span>GitHub do projeto</span>
    </a>
    """,
    unsafe_allow_html=True
)

