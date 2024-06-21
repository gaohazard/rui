import streamlit as st
from gtts import gTTS 
import os

# 创建Streamlit应用
st.title("文本转语音")

# 上传文本文件
uploaded_file = st.file_uploader("上传文本文件", type=["txt"])

if uploaded_file is not None:
    # 读取上传的文本文件
    file_contents = uploaded_file.getvalue().decode("utf-8")

    # 将文本转换为语音
    speech = gTTS(text=file_contents, lang='en', slow=False)
    speech.save("voice.mp3")

    # 在Streamlit中播放语音
    audio_file = open('voice.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

    # 显示文本内容
    st.write(file_contents)

