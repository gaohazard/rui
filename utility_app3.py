import streamlit as st
import speech_recognition as sr
import audioread
import wave
import os

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

def convert_to_wav(mp3_path):
    wav_path = "temp_audio_file.wav"
    with audioread.audio_open(mp3_path) as input_file:
        with wave.open(wav_path, "wb") as output_file:
            output_file.setnchannels(input_file.channels)
            output_file.setsampwidth(2)  # 16-bit samples
            output_file.setframerate(input_file.samplerate)

            for buffer in input_file:
                output_file.writeframes(buffer)

    return wav_path

def main():
    st.title("语音转文字转换器")

    uploaded_file = st.file_uploader("上传音频文件", type=["mp3"])

    if uploaded_file is not None:
        mp3_path = "temp_audio_file.mp3"
        
        # 将上传的 MP3 文件保存到磁盘
        with open(mp3_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 将 MP3 文件转换为 WAV 文件
        wav_file_path = convert_to_wav(mp3_path)

        # 识别 WAV 文件中的文本
        text = transcribe_audio(wav_file_path)

        # 显示转换后的文本
        st.write("转录的文本:")
        st.write(text)

        # 将文本保存到文件中
        with open('transcribed_text.txt', 'w', encoding='utf-8') as file:
            file.write(text)

        # 提供下载链接
        st.download_button("下载转录文本文件", data=text, file_name='transcribed_text.txt', mime='text/plain')

        # 清理临时文件
        os.remove(mp3_path)
        os.remove(wav_file_path)

if __name__ == '__main__':
    main()
