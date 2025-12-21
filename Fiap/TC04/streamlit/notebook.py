import streamlit as st
from streamlit.components.v1 import html
from pathlib import Path

def render():
    st.set_page_config(
        page_title="Análise Exploratória",
        page_icon="📊",
        layout="wide"
    )

    st.title("Análise Exploratória dos Dados")
    st.markdown("Notebook convertido para HTML.")

    html_path = Path("Tech_Challange_04.html")

    if html_path.exists():
        with open(html_path, "r", encoding="utf-8") as f:
            html(
                f.read(),
                height=900,
                scrolling=True
            )
    else:
        st.error("Arquivo Tech_Challange_04.html não encontrado.")
        
