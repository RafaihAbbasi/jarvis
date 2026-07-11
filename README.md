# Jarvis - Python Voice Assistant

Jarvis is a lightweight Python voice assistant that uses speech recognition and text-to-speech to open websites hands-free. It uses a two-stage process: it waits until it hears the wake word "Jarvis" before listening for your actual command.

## 🚀 Features
* **Wake Word Activation:** Stays idle until you say "Jarvis", "Hey Jarvis", or "Hello Jarvis".
* **Voice Feedback:** Talks back to you using your system's text-to-speech engine.
* **Web Automation:** Automatically opens Google, YouTube, Facebook, and LinkedIn via voice.

## 🛠️ Installation & Setup

Before running the assistant, you need to install the required Python libraries.

### 1. Install dependencies
Open your terminal inside VS Code and run:

```bash
pip install SpeechRecognition pyttsx3
