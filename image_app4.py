import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
from io import BytesIO

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

    st.write("Click on the image to select two points for cropping.")

    image_width, image_height = image.size
    image_array = np.array(image)

    if st.button("Clear Points"):
        st.experimental_rerun()

    if "cropped_p1" not in st.session_state:
        st.session_state.cropped_p1 = None
    if "cropped_p2" not in st.session_state:
        st.session_state.cropped_p2 = None

    if st.session_state.cropped_p1 is not None and st.session_state.cropped_p2 is not None:
        cropped_image = crop_image(image, st.session_state.cropped_p1, st.session_state.cropped_p2)
        st.image(cropped_image, caption="Cropped Image", use_column_width=True)

    clicked_point = st.image(image_array, use_column_width=True, clamp=True)
    draw = ImageDraw.Draw(image)

    if clicked_point is not None:
        x, y = st.session_state.mouse_click_data[clicked_point.key]["x"], st.session_state.mouse_click_data[clicked_point.key]["y"]
        st.write(f"Clicked Point: ({x}, {y})")

        if st.session_state.cropped_p1 is None:
            st.session_state.cropped_p1 = (x, y)
            draw.rectangle([x, y, x + 5, y + 5], outline="red", width=2)
        elif st.session_state.cropped_p2 is None:
            st.session_state.cropped_p2 = (x, y)
            draw.rectangle([x, y, x + 5, y + 5], outline="blue", width=2)

    new_image = Image.fromarray(image_array)
    buffered = BytesIO()
    new_image.save(buffered, format="PNG")
    st.image(buffered, use_column_width=True, clamp=True)

