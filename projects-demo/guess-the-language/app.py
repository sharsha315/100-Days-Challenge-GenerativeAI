import streamlit as st
import whisper
import tempfile
import os
from st_audiorec import st_audiorec  # Audio recorder component

# Load Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("small")

model = load_model()

# Mapping language codes to full names
LANGUAGE_NAMES = {
    "en": "English",
    "fr": "French",
    "hi": "Hindi",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    # Add more if needed
}

# --- Streamlit App ---
#st.set_page_config(page_title="Guess The Language", page_icon="🎯")
st.title("🎯 Guess The Language")
st.markdown("Speak something and let the AI guess the language!")

# Record Audio
st.subheader("🎤 Record your voice:")
wav_audio_data = st_audiorec()

# If recording finished
if wav_audio_data is not None:
    st.success("✅ Recording stopped. Processing your audio...")
    
    with st.spinner("🔎 Detecting language..."):
        # Save the recorded audio to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(wav_audio_data)
            temp_audio_path = temp_audio.name

        # Run Whisper model
        result = model.transcribe(temp_audio_path, task="transcribe", language=None)

        detected_lang_code = result["language"]
        detected_lang_name = LANGUAGE_NAMES.get(detected_lang_code, detected_lang_code)

        # Clean up
        os.remove(temp_audio_path)

    # --- Results ---
    st.balloons()
    st.header(f"💡 Detected Language: {detected_lang_name}")
    
    if st.checkbox("Show Transcription", value=False):
        st.write(result["text"])

else:
    st.info("Click the start button above to start recording.")


