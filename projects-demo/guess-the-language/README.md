# 🎯 Guess The Language

> Speak anything — let AI guess what language you're speaking! 🗣️✨

---

## 📚 Project Overview

**Guess The Language** is a fun, interactive app where you record your voice, and OpenAI's Whisper model detects which language you spoke.  
Built with **Python**, **Streamlit**, and **Whisper**, it delivers real-time results with a simple and beautiful UI.

---

## 🛠️ Tech Stack

| Tech | Description |
|:----|:-------------|
| 🐍 Python | Programming language |
| 🎨 Streamlit | Frontend and backend for the app |
| 🧠 OpenAI Whisper | Speech-to-text and language detection |
| 🎧 st_audiorec | Streamlit component for recording audio |

---

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
pip install -r requirements.txt
```
4. **(Important) Make sure you have ffmpeg installed:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
sudo apt-get install libgbm1

sudo apt --fix-broken install # use this, if encountered errors
```

📜 **Usage**
1. Change the directory:
```bash
cd projects-demo/guess-the-language
```
2. Run the app:
```bash
streamlit run app.py
```
3. Speak into the microphone after clicking the **Record** button.
4. Click **Stop** — the app will **immediately detect** and display the language you spoke.
5. (Optional) View the **transcribed text**.

🎨 **Features**
- Real-time voice recording.
- Language detection using AI (OpenAI Whisper).
- Instant results after recording stops.
- Clean and beautiful Streamlit UI.
- Fun balloons animation after successful detection.
- Option to view detailed transcription.

💡 **Future Improvements**
- Allow uploading audio files instead of only recording.
- Detect dialects/regional variations.
- Option to choose different Whisper model sizes (tiny, small, medium, etc.).
- Deploy online via Streamlit Cloud or Huggingface Spaces.


**Contributions:**
Contributions to this folder are welcome! If you have any improvements, bug fixes, or new examples, feel free to submit a pull request.

**📜 License:**
This project is open-source and available under the **MIT License**.

**Author:** 
[Harsha S](https://www.x.com/sharsha315)

Happy Coding! 🚀💡