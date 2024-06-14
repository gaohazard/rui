import streamlit as st
from docx import Document
import fitz  # PyMuPDF
import os

def convert_pdf_to_word(pdf_path, word_path):
    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)
    # 创建一个新的Word文档
    doc = Document()

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")
        doc.add_paragraph(text)

    # 保存Word文档
    doc.save(word_path)

# 主函数
def utility_app1():
    st.title("PDF 转 Word 批量转换工具")
    
    # 上传文件
    uploaded_files = st.file_uploader("选择一个或多个PDF文件", type="pdf", accept_multiple_files=True)
    
    if uploaded_files:
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for uploaded_file in uploaded_files:
            pdf_filename = uploaded_file.name
            word_filename = pdf_filename.replace('.pdf', '.docx')
            pdf_path = os.path.join(output_dir, pdf_filename)
            word_path = os.path.join(output_dir, word_filename)
            
            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            convert_pdf_to_word(pdf_path, word_path)
            
            st.success(f"转换成功: {word_filename}")
            with open(word_path, "rb") as f:
                st.download_button(f"下载 {word_filename}", f, file_name=word_filename)

if __name__ == "__main__":
    utility_app1()
