from pathlib import Path
import streamlit as st
from streamlit.components.v1 import html

def render():
    st.set_page_config(
        page_title="Análise Exploratória",
        page_icon="📊",
        layout="wide"
    )

    st.title("Notebook utilizado para a criação do modelo")
    st.markdown("Notebook convertido para HTML.")

    BASE_DIR = Path(__file__).parent
    html_path = BASE_DIR / "Tech_Challenge_04.html"

    if html_path.exists():
        with open(html_path, "r", encoding="utf-8") as f:
            html(
                f.read(),
                height=900,
                scrolling=True
            )
    else:
        st.error(f"Arquivo não encontrado em: {html_path}")
