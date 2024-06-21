import streamlit as st
import pyaudio
import speech_recognition as sr
from googletrans import Translator

translator = Translator()

# 初始化语音识别器
r = sr.Recognizer()

# 创建PyAudio对象
audio = pyaudio.PyAudio()

# 打开麦克风流
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

st.title("Real-time Speech to Chinese Text Translator")

st.write("Listening...")

while True:
    data = stream.read(1024)
    text = r.recognize_google(data, key=None, language='en-US', show_all=False)
    
    if text:
        st.write(f"English: {text}")
        
        translation = translator.translate(text, dest='zh-cn')
        st.write(f"Chinese: {translation.text}")
