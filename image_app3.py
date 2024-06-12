import streamlit as st
from PIL import Image, ImageOps

def modify_image(image, resolution, new_width, new_height, save_size, background_color):
    # 修改分辨率
    image = image.resize(resolution)

    # 修改像素宽高
    image = image.resize((new_width, new_height))

    # 调整照片的背景颜色
    if background_color:
        image = ImageOps.expand(image, border=10, fill=background_color)

    # 保存尺寸大小
    image = image.resize(save_size)
    
    return image

def app3():
    st.title("Image Modifier")
    
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        resolution = (800, 600)  # 分辨率
        new_width = 400  # 新宽度
        new_height = 300  # 新高度
        save_size = (200, 150)  # 保存尺寸大小
        background_color = (255, 255, 255)  # 背景颜色

        modified_image = modify_image(image, resolution, new_width, new_height, save_size, background_color)

        st.image(modified_image, caption="Modified Image", use_column_width=True)

        if st.button("Save Image"):
            modified_image.save("modified_image.jpg")
            st.success("Image saved successfully.")

if __name__ == "__main__":
    app3()
