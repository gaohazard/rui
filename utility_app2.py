import streamlit as st
import pyttsx3

st.title("文本转语音")

# 获取用户输入的文本
text = st.text_area("请输入要转换为语音的文本", "")

# 初始化 pyttsx3 引擎
engine = pyttsx3.init()

# 将文本转换为语音
engine.save_to_file(text, 'output.mp3')

# 播放生成的语音
st.audio('output.mp3', format='audio/mp3')

