import streamlit as st
from PIL import Image
import os
def get_image_size(image):
    # 获取图像的尺寸大小（KB）
    image_size = os.path.getsize(image.fp.name) / 1024
    return image_size

def modify_image(image, resolution_dpi, new_width, new_height):
    # 修改分辨率
    resolution = (int(image.size[0] * resolution_dpi / 25.4), int(image.size[1] * resolution_dpi / 25.4))
    image = image.resize(resolution)

    # 修改像素宽高
    image = image.resize((new_width, new_height))

    # 保存尺寸大小
    image = image.resize((new_width, new_height))
    
    return image

def app3():
    st.title("Image Modifier")
    
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        resolution_dpi = st.sidebar.slider("Resolution (DPI)", 50, 500, 150)
        new_width = st.sidebar.slider("New Width", 100, 1000, 400)
        new_height = st.sidebar.slider("New Height", 100, 1000, 300)

        modified_image = modify_image(image, resolution_dpi, new_width, new_height)

        st.image(modified_image, caption="Modified Image", use_column_width=True)

        if st.button("Save Image"):
            image_size = get_image_size(modified_image)
           if image_size > 0:  # 检查图像尺寸是否大于 0
                modified_image.save("modified_image.jpg")
                st.success("Image saved successfully.")
            else:
                st.error("Failed to save image. Please try again.")

if __name__ == "__main__":
    app3()
