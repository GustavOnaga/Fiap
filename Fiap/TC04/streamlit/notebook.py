import streamlit as st
from streamlit.components.v1 import html
from pathlib import Path

def render():
    st.set_page_config(
        page_title="Análise Exploratória",
        page_icon="📊",
        layout="wide"
    )

    st.title("Notebook utilizado para a criação do modelo")
    st.markdown("Notebook convertido para HTML.")

    html_path = Path("Tech_Challenge_04.html")

    if html_path.exists():
        with open(html_path, "r", encoding="utf-8") as f:
            html(
                f.read(),
                height=900,
                scrolling=True
            )
    else:
        st.error("Arquivo Tech_Challenge_04.html não encontrado.")

