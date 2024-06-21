import streamlit as st
import speech_recognition as sr
import subprocess
import os
from io import BytesIO

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

def convert_to_wav(mp3_file):
    wav_file = "temp_audio_file.wav"
    command = ["ffmpeg", "-i", mp3_file, "-acodec", "pcm_s16le", "-ar", "16000", wav_file]
    subprocess.run(command, check=True)
    return wav_file

def main():
    st.title("语音转文字转换器")

    uploaded_file = st.file_uploader("上传音频文件", type=["mp3"])

    if uploaded_file is not None:
        # 使用 BytesIO 来处理上传的文件
        temp_mp3 = BytesIO(uploaded_file.getvalue())

        # 将 BytesIO 对象写入临时文件
        with open("temp_audio_file.mp3", "wb") as f:
            f.write(temp_mp3.getbuffer())

        # 转换 MP3 到 WAV
        wav_file = convert_to_wav("temp_audio_file.mp3")

        # 识别 WAV 文件中的文本
        text = transcribe_audio(wav_file)

        # 显示转换后的文本
        st.write("转录的文本:")
        st.write(text)

        # 将文本保存到文件中
        with open('transcribed_text.txt', 'w', encoding='utf-8') as file:
            file.write(text)

        # 提供下载链接
        st.download_button("下载转录文本文件", data=text, file_name='transcribed_text.txt', mime='text/plain')

if __name__ == '__main__':
    main()

