import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text

def convert_to_wav(mp3_file):
    sound = AudioSegment.from_mp3(mp3_file)
    wav_file = "temp_audio_file.wav"
    sound.export(wav_file, format="wav")
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

if __name__ == '__main__':
    main()
