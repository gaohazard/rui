import streamlit as st
from PIL import Image, ImageChops, ImageOps, ImageSequence
import os

import streamlit as st

def app1():
    st.title("9宫格图片")
    import streamlit as st
    st.write("这是9宫格图片的内容")


def trim(image):
    bg = Image.new(image.mode, image.size, image.getpixel((0,0)))
    diff = ImageChops.difference(image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return image.crop(bbox)

def main():
    st.title("16宫格图片处理")

    uploaded_file = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="上传的图片", use_column_width=True)

        # 添加填写框和参数选择框
        left_margin = st.number_input("左边距", value=5)
        top_margin = st.number_input("上边距", value=5)
        right_margin = st.number_input("右边距", value=5)
        bottom_margin = st.number_input("下边距", value=40)
        duration = st.number_input("动图持续时间 (ms)", value=300)
        output_size = st.selectbox("输出图像像素大小", [120, 240, 360])

        # 进行图片处理
        st.subheader("处理后的16宫格图片")

        # 去除大图的白边
        large_image_trimmed = trim(image)

        # 获取去除白边后的图像尺寸
        width, height = large_image_trimmed.size

        # 计算每个小图的宽度和高度
        small_width = width // 4
        small_height = height // 4

        # 初始化最小尺寸
        min_width = small_width
        min_height = small_height

        # 保存裁剪后的16张小图到指定路径
        save_path = "output_images"
        os.makedirs(save_path, exist_ok=True)
        images = []
        for i in range(4):
            for j in range(4):
                # 计算裁剪区域
                left = j * small_width
                top = i * small_height
                right = left + small_width
                bottom = top + small_height

                # 裁剪图像
                small_image = large_image_trimmed.crop((left, top, right, bottom))

                # 再次去除小图的白边
                small_image_trimmed = trim(small_image)

                # 更新最小尺寸
                min_width = min(min_width, small_image_trimmed.width)
                min_height = min(min_height, small_image_trimmed.height)

                images.append(small_image_trimmed)

        # 统一调整每张图片的大小并添加边距
        padding = 2
        for i in range(16):
            images[i] = ImageOps.expand(images[i].resize((min_width, min_height)), border=padding, fill='white')

        # 保存裁剪后的小图到指定路径
        for i in range(16):
            images[i].save(os.path.join(save_path, f"cropped_image_{i+1}.jpg"))

        st.success("处理完成！")

        # 在网页上显示生成的 GIF 图像
        st.subheader("处理后的GIF动图")
        for i in range(16):
            st.image(images[i], caption=f"小图{i+1}", use_column_width=True)

if __name__ == "__main__":
    main()
