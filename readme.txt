https://drive.google.com/drive/folders/1FFUDqK2NAm_SZcz33_bdsIaM4BIf74Qt?usp=sharing




# Surveillance System

## Overview
The **Surveillance System** is an AI-powered security application that detects various safety violations in real-time using computer vision. It consists of separate **Streamlit-based frontends** for different detection tasks and a **FastAPI-powered backend** for processing video streams.

## Features
- **Helmet Detection** 🪖: Ensures workers wear helmets in restricted zones.
- **Mask Detection** 😷: Identifies if individuals are wearing face masks.
- **Weapon Detection** 🔫: Detects the presence of weapons in surveillance footage.
- **Tampering Detection** 🔧: Recognizes unauthorized tampering with cameras.

## Technologies Used
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Computer Vision**: OpenCV, YOLO (You Only Look Once)
- **Deep Learning**: PyTorch / TensorFlow


## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Git
- Virtualenv / Conda (optional but recommended)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/pratik-1818/Surveillance-System.git
   cd Surveillance-System
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run FastAPI Backend**
   ```bash
   uvicorn main:app --reload
   ```
5. **Run Streamlit Frontends**
   - Helmet Detection: `streamlit run frontend/helmet_streamlit.py`
   - Mask Detection: `streamlit run frontend/mask_streamlit.py`
   - Weapon Detection: `streamlit run frontend/weapon_streamlit.py`
   - Tampering Detection: `streamlit run frontend/tampering_streamlit.py`

## Usage
1. Start the **FastAPI backend** to process video streams.
2. Open the **Streamlit frontends** for different detection modules.
3. Upload a video or provide a live camera feed.
4. View real-time detections and alerts.

## Folder Structure
```
Surveillance-System/
│── backend/                # FastAPI backend
│   ├── helmet.py
│   ├── mask.py
│   ├── weapon.py
│── frontend/               # Streamlit frontends
│   ├── helmet_streamlit.py
│   ├── mask_streamlit.py
│   ├── weapon_streamlit.py
│   ├── tampering_streamlit.py
│── model/                  # Pretrained AI models
│── main.py                 # FastAPI entry point
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

## Contributing
Feel free to contribute by:
- Reporting issues
- Suggesting improvements
- Adding new features

## License
[MIT License](LICENSE)

## Contact
For questions or collaborations, contact **[Your Email or GitHub Profile]**.

