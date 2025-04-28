import streamlit as st
import whisper
import tempfile
from st_audiorec import st_audiorec
import time

# Load Whisper Model
@st.cache_resource
def load_model():
    return whisper.load_model("small")

model = load_model()

# Streamlit App
st.title("🎤 Whisper Translates")
st.caption("Real-time Voice Translator. Speak in any language — get translation instantly!")

# Audio Recorder
wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(wav_audio_data)
        temp_audio_path = temp_audio.name

    with st.spinner('Translating... Please wait'):
        result = model.transcribe(temp_audio_path, task="translate")
        english_text = result["text"].strip()
        detected_lang = result["language"]

        # Simulate slight delay for better UX
        time.sleep(1)

    # Chat style UI
    with st.chat_message("user"):
        st.audio(wav_audio_data, format="audio/wav")
        st.write("🧑‍🎤 You spoke:")

    with st.chat_message("assistant"):
        st.write(f"🌐 Detected Language: `{detected_lang}`")
        st.write(f"💬 English Translation: **{english_text}**")

else:
    st.info("🎤 Click 'Start' to record your voice!")

