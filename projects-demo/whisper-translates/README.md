# Whisper Translates
- Translate your voice into English instantly!
- Built using OpenAI Whisper model + Streamlit with a clean chat-like interface.

## 🎨 **Features**
- Record your voice directly inside the app
- Automatic language detection
- Real-time translation into English
- Simple and beautiful chat interface
- Lightweight, fast, and fully in-browser (no server needed)
- Temporary audio files (auto-managed)

## Tech Stack
- Streamlit — For frontend + interaction
- OpenAI Whisper — For transcription and translation
- st_audiorec — For audio recording in Streamlit
- Tempfile — To handle temporary file storage securely

## 📥 Installation

1. **Clone the Repository**
```bash
git clone https://github.com/sharsha315/100-Days-Challenge-GenerativeAI.git
```

2. **Create a Virtual Environment (Recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. **Install Required Packages**
- **requirements.txt** file:
```bash
streamlit
st_audiorec
openai-whisper
pydub
```

```bash
pip install -r projects-demo/whisper-translates/requirements.txt
```
4. **(Important) Make sure you have ffmpeg installed:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
sudo apt-get install libgbm1

sudo apt --fix-broken install # use this, if encountered errors
```

## 📜 Usage
1. Change the directory:
```bash
cd projects-demo/whisper-translates
```
2. Run the app:
```bash
streamlit run app.py
```

## 🎯 How it Works
1. Click Start to begin recording your voice.
2. Click Stop once done.
3. The app automatically processes your speech:
   - Detects spoken language
   - Translates it into English
4. The original audio and the translation are shown as a chat conversation.

## 💡 How Whisper Translation Works
- task="translate" automatically:
    - Detects the spoken language
    - Translates the content into English
- No need for manual language detection or external translator APIs!

## 🙏 Acknowledgements
- OpenAI for the amazing Whisper model
- Streamlit community
- st_audiorec open-source maintainers

## Contributions:
Contributions to this folder are welcome! If you have any improvements, bug fixes, or new examples, feel free to submit a pull request.

## 📜 License:
This project is open-source and available under the **MIT License**.

## Author:
[Harsha S](https://www.x.com/sharsha315)

Love this project? 🚀
Follow me for more AI x Streamlit project ideas!


