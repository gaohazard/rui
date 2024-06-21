import streamlit as st
import speech_recognition as sr

st.title("语音转文本")

# 上传音频文件
audio_data = st.file_uploader("上传音频文件", type=["wav", "mp3", "ogg"])

if audio_data is not None:
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_data) as source:
        audio = recognizer.record(source)
        
    text = recognizer.recognize_google(audio)
    
    st.write("转换后的文本:")
    st.write(text)

