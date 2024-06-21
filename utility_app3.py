import streamlit as st
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from googletrans import Translator

translator = Translator()

# 初始化语音识别器
r = sr.Recognizer()

# 定义回调函数来处理音频数据
def callback(indata, frames, time, status):
    if status:
        print(status)
    text = r.recognize_google(indata, key=None, language='en-US', show_all=False)
    
    if text:
        st.write(f"English: {text}")
        
        translation = translator.translate(text, dest='zh-cn')
        st.write(f"Chinese: {translation.text}")

# 打开麦克风流
with sd.InputStream(callback=callback):
    st.title("Real-time Speech to Chinese Text Translator")
    st.write("Listening...")
    st.write("Press Ctrl+C to stop")
    st.text("Note: You may need to adjust the microphone volume for better recognition")
    st.text("Note: The translation may have a slight delay")
