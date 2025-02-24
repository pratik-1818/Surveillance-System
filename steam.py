import streamlit as st

# FastAPI backend URL
BASE_URL = "http://127.0.0.1:8000"

# Detection routes
DETECTION_ROUTES = {
    "Helmet Detection": f"{BASE_URL}/helmet_feed/",
    "Mask Detection": f"{BASE_URL}/mask_feed/",
    "Weapon Detection": f"{BASE_URL}/weapon_feed/",
    "Camera Tampering": f"{BASE_URL}/tampering_feed/"
}

# Streamlit Page Configuration
st.set_page_config(page_title="Real-Time Detection", layout="wide")

# Sidebar for Selection
st.sidebar.title("🛠️ Real-Time Detection System")
selected_detection = st.sidebar.radio("Choose Detection Type:", list(DETECTION_ROUTES.keys()))

# Page Header
st.title("🔍 Live Detection System")
st.markdown("### Select a detection type from the sidebar to start streaming.")

# **Update Video Stream Dynamically**
st.subheader(f"📡 {selected_detection} Stream")
st.markdown("### If the stream doesn't start, ensure the FastAPI server is running!")

video_url = DETECTION_ROUTES[selected_detection]
st.image(video_url, use_column_width=True)

# Footer
st.markdown("---")
st.markdown("💡 **Tip:** Make sure your FastAPI backend is running before starting the stream!")
