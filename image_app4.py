import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
from io import BytesIO
import tempfile

def crop_image(image, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    cropped_image = image.crop((x1, y1, x2, y2))
    return cropped_image

st.title("Image Cropping Tool")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Move the line to select the cropping area.")

    # Draw a line to represent the cropping area
    line_length = st.slider("Line Length", min_value=10, max_value=200, value=100)
    line_direction = st.radio("Line Direction", ["Horizontal", "Vertical"])

    if line_direction == "Horizontal":
        p1 = (0, image.height // 2)
        p2 = (line_length, image.height // 2)
    else:
        p1 = (image.width // 2, 0)
        p2 = (image.width // 2, line_length)

    draw = ImageDraw.Draw(image)
    draw.line([p1, p2], fill="red", width=2)

    cropped_image = crop_image(image, p1, p2)

    # Save the cropped image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        cropped_image.save(temp_file.name, format="PNG", quality=95)

        # Read the temporary file and display the cropped image
        with open(temp_file.name, "rb") as f:
            cropped_image_bytes = BytesIO(f.read())
            st.image(cropped_image_bytes, caption="Cropped Image", use_column_width=True)
