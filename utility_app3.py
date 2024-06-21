import streamlit as st
import speech_recognition as sr

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text

def main():
    st.title("Speech-to-Text Converter")

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        with open("temp_audio_file.mp3", "wb") as f:
            f.write(uploaded_file.getbuffer())

        text = transcribe_audio("temp_audio_file.mp3")

        st.write("Transcribed text:")
        st.write(text)

        with open('transcribed_text.txt', 'w') as file:
            file.write(text)

        st.write("Transcribed text saved to transcribed_text.txt")

if __name__ == '__main__':
    main()
