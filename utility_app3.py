import streamlit as st
import speech_recognition as sr
import subprocess

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text

def convert_to_wav(mp3_file):
    wav_file = "temp_audio_file.wav"
    command = f"ffmpeg -i {mp3_file} -acodec pcm_s16le -ar 16000 {wav_file}"
    subprocess.call(command, shell=True)
    return wav_file

def main():
    st.title("Speech-to-Text Converter")

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3"])

    if uploaded_file is not None:
        with open("temp_audio_file.mp3", "wb") as f:
            f.write(uploaded_file.getbuffer())

        wav_file = convert_to_wav("temp_audio_file.mp3")
        text = transcribe_audio(wav_file)

        st.write("Transcribed text:")
        st.write(text)

        with open('transcribed_text.txt', 'w') as file:
            file.write(text)

        st.write("Transcribed text saved to transcribed_text.txt")

if __name__ == '__main__':
    main()
