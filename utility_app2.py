import streamlit as st
from gtts import gTTS 
import os

# 读取文本文件
file = open("abc.txt", "r").read()

# 将文本转换为语音
speech = gTTS(text=file, lang='en', slow=False)
speech.save("voice.mp3")

# 在Streamlit中播放语音
audio_file = open('voice.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')

# 显示文本内容
st.write(file)
