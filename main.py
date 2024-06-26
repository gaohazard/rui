import streamlit as st
from image_app1 import app1 as image_app1
from image_app2 import app2 as image_app2
from image_app3 import app3 as image_app3
from datetime import datetime
import time
import pytz
#import cv2
from table_app1 import app1 as table_app1
#from table_app2 import app2 as table_app2
#from data_app1 import app1 as data_app1
#from data_app2 import app2 as data_app2
from utility_app1 import app1 as utility_app1
#from utility_app2 import app2 as utility_app2
from work_app1 import EstimateBaApp as work_app1
#from work_app2 import app2 as work_app2

# 实时显示时间和日期
def display_time():
    tz = pytz.timezone('Asia/Shanghai')  # 设置为北京时间
    placeholder = st.sidebar.empty()  # 创建一个可变的占位符
    while True:
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")  # 获取当前北京时间和日期
        with placeholder.container():
            st.markdown(f"**当前北京时间:** {current_time}")  # 显示当前北京时间和日期
        time.sleep(1)  # 每秒更新一次
    

def main():
    st.sidebar.title("选择处理类型")
    process_type = st.sidebar.selectbox("选择处理类型", ["图片处理", "表格处理","数据分析","实用工具","工作使用"])

    if process_type == "图片处理":
        st.sidebar.subheader("选择图片类型")
        image_type = st.sidebar.selectbox("选择图片类型", ["9宫格图片", "16宫格图片","修改照片格式"])

        if image_type == "9宫格图片":
            image_app1()
        elif image_type == "16宫格图片":
            image_app2()
        elif image_type == "修改照片格式":
            image_app3()
    elif process_type == "表格处理":
        st.sidebar.subheader("选择表格类型")
        table_type = st.sidebar.selectbox("选择表格类型", ["VLOOKUP工具", "表格处理2"])

        if table_type == "VLOOKUP工具":
            table_app1()
        #elif table_type == "表格处理2":
            #table_app2()
    #elif process_type == "数据分析":
        #st.sidebar.subheader("选择数据分析类型")
        #data_type = st.sidebar.selectbox("选择数据分析类型", ["数据分析1", "数据分析2"])

        #if data_type == "数据分析1":
            #data_app1()
        #elif data_type == "数据分析2":
            #data_app2()
    elif process_type == "实用工具":
        st.sidebar.subheader("选择实用工具类型")
        utility_type = st.sidebar.selectbox("选择实用工具类型", ["PDF转WORD", "实用工具2"])

        if utility_type == "PDF转WORD":
            utility_app1()
        #elif utility_type == "文字转语音":
            #utility_app2()
    elif process_type == "工作使用":
        st.sidebar.subheader("选择工作使用类型")
        work_type = st.sidebar.selectbox("选择工作使用类型", ["737飞机重量重心及停放中抗风能力测算工具", "工作使用2"])

        if work_type == "737飞机重量重心及停放中抗风能力测算工具":
            work_app1()
        #elif work_type == "工作使用2":
            #work_app2()
if __name__ == "__main__":
    main()
    display_time()

