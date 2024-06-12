import streamlit as st
from app1 import app1
from app2 import app2

def main():
    st.title("图片处理")

    # 在侧边栏展示小程序选项
    app_choice = st.sidebar.selectbox("选择要展示的小程序", ["9宫格图片", "16宫格图片"])

    # 根据用户选择展示不同的小程序内容
    if app_choice == "9宫格图片":
        app1()
    elif app_choice == "16宫格图片":
        app2()

if __name__ == "__main__":
    main()
