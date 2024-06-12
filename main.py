import streamlit as st
from image_app1 import app1 as image_app1
from image_app2 import app2 as image_app2
#from table_app1 import app1 as table_app1
#from table_app2 import app2 as table_app2

def main():
    st.sidebar.title("选择处理类型")
    process_type = st.sidebar.selectbox("选择处理类型", ["图片处理", "表格处理"])

    if process_type == "图片处理":
        st.sidebar.subheader("选择图片类型")
        image_type = st.sidebar.selectbox("选择图片类型", ["9宫格图片", "16宫格图片"])

        if image_type == "9宫格图片":
            image_app1()
        elif image_type == "16宫格图片":
            image_app2()
    #elif process_type == "表格处理":
        #st.sidebar.subheader("选择表格类型")
        #table_type = st.sidebar.selectbox("选择表格类型", ["表格处理1", "表格处理2"])

        #if table_type == "表格处理1":
            #table_app1()
        #elif table_type == "表格处理2":
            #table_app2()

if __name__ == "__main__":
    main()
