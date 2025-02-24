import streamlit as st

st.set_page_config(page_title="Helmet Detection", layout="wide")

st.title("🪖 Helmet Detection System")
st.image("http://127.0.0.1:8000/helmet_feed/", use_column_width=True)
st.markdown("### Ensure the FastAPI server is running to view the live stream.")
