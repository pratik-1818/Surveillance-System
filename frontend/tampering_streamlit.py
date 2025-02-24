import streamlit as st

st.set_page_config(page_title="Camera Tampering Detection", layout="wide")

st.title("🎥 Camera Tampering Detection System")
st.image("http://127.0.0.1:8000/tampering_feed/", use_column_width=True)
st.markdown("### Ensure the FastAPI server is running to view the live stream.")
