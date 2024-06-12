import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageOps

def remove_background(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    markers = cv2.watershed(img, sure_bg)
    img[markers == -1] = [255, 0, 0]
    return img

def modify_image(image, resolution, new_width, new_height, save_size, background_color, crop_params):
    # 背景抠图
    image = remove_background(image)

    # 修改分辨率
    image = cv2.resize(image, resolution)

    # 修改像素宽高
    image = cv2.resize(image, (new_width, new_height))

    # 修改背景颜色
    image[np.where((image == [255, 0, 0]).all(axis=2))] = background_color

    # 剪切图片
    top, bottom, left, right = crop_params
    image = image[top:-bottom, left:-right]

    # 转换为PIL图像
    image = Image.fromarray(image)

    # 保存尺寸大小
    image = image.resize(save_size)

    return image

def app3():
    st.title("Image Editor")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        resolution = st.sidebar.slider("Resolution", 100, 2000, (800, 600))
        new_width = st.sidebar.slider("New Width", 100, 1000, 400)
        new_height = st.sidebar.slider("New Height", 100, 1000, 300)
        save_width = st.sidebar.slider("Save Width", 50, 500, 200)
        save_height = st.sidebar.slider("Save Height", 50, 500, 150)
        background_color = st.sidebar.color_picker("Background Color", "#ffffff")
        top_crop = st.sidebar.slider("Top Crop", 0, 100, 0)
        bottom_crop = st.sidebar.slider("Bottom Crop", 0, 100, 0)
        left_crop = st.sidebar.slider("Left Crop", 0, 100, 0)
        right_crop = st.sidebar.slider("Right Crop", 0, 100, 0)

        crop_params = (top_crop, bottom_crop, left_crop, right_crop)

        modified_image = modify_image(image, resolution, new_width, new_height, (save_width, save_height), background_color, crop_params)

        st.image(modified_image, caption="Modified Image", use_column_width=True)

        if st.button("Save Image"):
            modified_image.save("modified_image.jpg")
            st.success("Image saved successfully.")

if __name__ == "__main__":
    app3()

