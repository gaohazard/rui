import streamlit as st
from PIL import Image, ImageOps

def modify_image(image, resolution, new_width, new_height, save_size, crop_params):
    # 修改分辨率
    image = image.resize(resolution)

    # 修改像素宽高
    image = image.resize((new_width, new_height))

    # 裁剪图像边缘
    if crop_params:
        image = image.crop(crop_params)

    # 保存尺寸大小
    image = image.resize(save_size)
    
    return image

def app3():
    st.title("Image Modifier")
    
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        resolution = st.sidebar.slider("Resolution", 100, 2000, (800, 600))
        new_width = st.sidebar.slider("New Width", 100, 1000, 400)
        new_height = st.sidebar.slider("New Height", 100, 1000, 300)
        save_width = st.sidebar.slider("Save Width", 50, 500, 200)
        save_height = st.sidebar.slider("Save Height", 50, 500, 150)
        
        crop_left = st.sidebar.slider("Crop Left", 0, image.width, 0)
        crop_top = st.sidebar.slider("Crop Top", 0, image.height, 0)
        crop_right = st.sidebar.slider("Crop Right", 0, image.width, image.width)
        crop_bottom = st.sidebar.slider("Crop Bottom", 0, image.height, image.height)
        crop_params = (crop_left, crop_top, crop_right, crop_bottom)

        modified_image = modify_image(image, resolution, new_width, new_height, (save_width, save_height), background_color, crop_params)

        st.image(modified_image, caption="Modified Image", use_column_width=True)

        if st.button("Save Image"):
            modified_image.save("modified_image.jpg")
            st.success("Image saved successfully.")

if __name__ == "__main__":
    app3()

