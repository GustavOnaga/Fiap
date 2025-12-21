import streamlit as st

def render():
    st.title("Dashboard Looker")

    looker_url = "https://lookerstudio.google.com/embed/reporting/0d10cd44-a6bf-4cc7-b8ca-df3dea6896b5/page/lyQjF"

    st.components.v1.iframe(
        src=looker_url,
        height=900,
        scrolling=True)
