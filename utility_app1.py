import streamlit as st
import fitz  # PyMuPDF
from docx import Document
from io import BytesIO

def app1(pdf_file):
    pdf_document = fitz.open(pdf_file)
    doc = Document()

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text = page.get_text("text")
        image_list = page.get_pixmap()

        doc.add_paragraph(text)
        for image in image_list:
            image_bytes = image.image_to_png_bytes()
            image_stream = BytesIO(image_bytes)
            doc.add_picture(image_stream)

    return doc

st.title("PDF to Word Converter")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    st.write("PDF file uploaded successfully!")

    # Convert PDF to Word
    word_doc = pdf_to_word(uploaded_file)

    # Download the Word file
    word_stream = BytesIO()
    word_doc.save(word_stream)
    st.download_button(
        label="Download Word file",
        data=word_stream.getvalue(),
        file_name="converted_document.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


if __name__ == "__main__":
    app1()

