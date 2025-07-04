
import streamlit as st
from PIL import Image
import pathlib

st.title("🧑‍🏫 Trainer Profile Formatter")

# Load logo
logo_path = pathlib.Path(__file__).resolve().parents[1] / "assets" / "logo.png"
if logo_path.exists():
    image = Image.open(logo_path)
    st.image(image, width=120)

uploaded_file = st.file_uploader("Upload Trainer Profile (.docx)", type="docx")

if uploaded_file and st.button("Format Profile"):
    st.success("Profile formatted successfully")
    # Placeholder logic for PDF formatting
