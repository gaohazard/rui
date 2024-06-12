import streamlit as st
from image_processing import image_app1, image_app2
from table_processing import table_app1, table_app2
from data_analysis import data_app1, data_app2
from utility_tools import utility_app1, utility_app2

def main():
    st.title("多个小程序展示页面")

    # 在侧边栏展示不同分类的选项卡
    selected_category = st.sidebar.selectbox("选择分类", ["图片处理", "表格处理", "数据分析", "实用工具"])

    # 根据用户选择展示不同分类下的小程序内容
    if selected_category == "图片处理":
        st.subheader("图片处理小程序1")
        image_app1.run()

        st.subheader("图片处理小程序2")
        image_app2.run()

    elif selected_category == "表格处理":
        st.subheader("表格处理小程序1")
        table_app1.run()

        st.subheader("表格处理小程序2")
        table_app2.run()

    elif selected_category == "数据分析":
        st.subheader("数据分析小程序1")
        data_app1.run()

        st.subheader("数据分析小程序2")
        data_app2.run()

    elif selected_category == "实用工具":
        st.subheader("实用工具小程序1")
        utility_app1.run()

        st.subheader("实用工具小程序2")
        utility_app2.run()

if __name__ == "__main__":
    main()

