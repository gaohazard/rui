import streamlit as st
import speech_recognition as sr

# 创建Streamlit应用
st.title("语音转文字")

# 上传语音文件
uploaded_file = st.file_uploader("上传语音文件", type=["wav", "mp3"])

if uploaded_file is not None:
    # 读取上传的语音文件
    audio_data = uploaded_file.read()

    # 使用SpeechRecognition库识别语音文件中的文本
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_data) as source:
        audio_text = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_text, language='en-US')
            st.write("识别结果：", text)
        except sr.UnknownValueError:
            st.write("无法识别语音")
        except sr.RequestError:
            st.write("无法连接到Google API")
