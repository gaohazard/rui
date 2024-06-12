import streamlit as st
from image_app2 import app2 as image_app2_func
from image_app1 import app1 as image_app1_func
from table_app1 import app1 as table_app1_func
from table_app2 import app2 as table_app2_func
from data_app1 import app1 as data_app1_func
from data_app2 import app2 as data_app2_func
from utility_app1 import app1 as utility_app1_func
from utility_app2 import app2 as utility_app2_func

def main():
    st.title("多个小程序展示页面")

    selected_category = st.sidebar.selectbox("选择分类", ["图片处理", "表格处理", "数据分析", "实用工具"])

    if selected_category == "图片处理":
        st.subheader("图片处理小程序1")
        image_app1_func()

        st.subheader("图片处理小程序2")
        image_app2_func()

    #elif selected_category == "表格处理":
        #st.subheader("表格处理小程序1")
        #table_app1_func()

        #st.subheader("表格处理小程序2")
        #table_app2_func()

   # elif selected_category == "数据分析":
       # st.subheader("数据分析小程序1")
       # data_app1_func()

      #  st.subheader("数据分析小程序2")
      #  data_app2_func()

 #   elif selected_category == "实用工具":
      #  st.subheader("实用工具小程序1")
    #    utility_app1_func()

    #    st.subheader("实用工具小程序2")
    #    utility_app2_func()

if __name__ == "__main__":
    main()
