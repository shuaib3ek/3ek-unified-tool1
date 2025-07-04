
import streamlit as st
from PIL import Image
import pathlib

st.title("📄 Course Outline Generator")

# Load logo
logo_path = pathlib.Path(__file__).resolve().parents[1] / "assets" / "logo.png"
if logo_path.exists():
    image = Image.open(logo_path)
    st.image(image, width=120)

course_name = st.text_input("Course Name")
duration = st.number_input("Duration (in days)", min_value=1)

if st.button("Generate Outline"):
    st.success(f"Generated outline for {course_name} ({duration} days)")
    # Placeholder logic for OpenAI + PDF
