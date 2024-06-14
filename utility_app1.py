import streamlit as st
import os
from pdf2docx import Converter

def pdf_to_word(pdf_file, word_file):
    # 初始化转换器
    cv = Converter(pdf_file)
    cv.convert(word_file, start=0, end=None)
    cv.close()

# Streamlit 应用
def app1():
    st.title("PDF 转 Word 批量转换工具")
    
    uploaded_file = st.file_uploader("上传一个或多个PDF文件", type="pdf", accept_multiple_files=True)
    
    if uploaded_file is not None:
        for pdf_file in uploaded_file:
            word_file = pdf_file.name.replace('.pdf', '.docx')
            pdf_to_word(pdf_file, word_file)
            st.write(f'Converted: {pdf_file.name}')
        
        st.success("转换完成！")

if __name__ == "__main__":
    app1()

