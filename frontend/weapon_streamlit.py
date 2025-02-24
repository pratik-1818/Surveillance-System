import streamlit as st

st.set_page_config(page_title="Weapon Detection", layout="wide")

st.title("🔫 Weapon Detection System")
st.image("http://127.0.0.1:8000/weapon_feed/", use_column_width=True)
st.markdown("### Ensure the FastAPI server is running to view the live stream.")
