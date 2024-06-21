import streamlit as st
import speech_recognition as sr
from mutagen.mp3 import MP3
import wave
import numpy as np
from io import BytesIO

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

def convert_to_wav(mp3_bytes):
    mp3_audio = MP3(BytesIO(mp3_bytes))

    # 获取音频数据段
    audio_data = mp3_audio.get_audio_segment()

    # 创建一个 BytesIO 对象来保存 WAV 文件
    wav_io = BytesIO()
    with wave.open(wav_io, "wb") as wav_file:
        wav_file.setnchannels(mp3_audio.info.channels)
        wav_file.setsampwidth(2)  # 16-bit samples
        wav_file.setframerate(mp3_audio.info.sample_rate)
        wav_file.writeframes(np.array(audio_data).tobytes())
    wav_io.seek(0)
    
    # 将 WAV 数据保存到临时文件
    temp_wav_file = "temp_audio_file.wav"
    with open(temp_wav_file, "wb") as f:
        f.write(wav_io.read())
    
    return temp_wav_file

def main():
    st.title("语音转文字转换器")

    uploaded_file = st.file_uploader("上传音频文件", type=["mp3"])

    if uploaded_file is not None:
        # 将上传的 MP3 文件转换为 WAV 文件
        wav_file = convert_to_wav(uploaded_file.getvalue())

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
