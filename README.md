# Jarvis AI Assistant

## 📌 Overview

Jarvis is an AI-powered voice assistant capable of performing various tasks, including searching the web, answering queries using OpenAI's API, fetching information from Wikipedia, and performing voice-based interactions using speech recognition and text-to-speech.

## 🚀 Features

-  🎤 Voice Command Recognition: Listens and converts speech to text.
-  🔊 Text-to-Speech: Uses pyttsx3 for vocal responses.
-  🔍 Web Search: Searches Google and Wikipedia.
-  🕒 Time Inquiry: Tells the current time.
-  🤖 AI Chatbot: Responds to user queries with OpenAI's GPT model.
-  📂 AI Response Saving: Stores AI-generated responses as text files
-  🌐 Automated Web Access: Opens YouTube, Google, and other websites on command.

## 🛠️ Tech Stack

-  **Python** 🐍
-  **OpenAI GPT-3 (API-powered AI responses)**
-  **SpeechRecognition 🎙️**
-  **Pyttsx3 (Text-to-Speech Engine) 🔊**
-  **Wikipedia API 📚**
-  **Webbrowser Module 🌐**

## 📦 Installation & Setup

1.  **Clone the repository:**
```sh
git clone https://github.com/rakshashetty66/jarvis-ai.git
cd jarvis-ai
```
2.  **Install dependencies:**
```sh
pip install speechrecognition openai pyttsx3 wikipedia
```
3.  **Set up OpenAI API Key:**

-  Open config.py and add your OpenAI API key:
```sh
apikey = "your-openai-api-key"
```

4.  **Run the script:**
```sh
python main.py
```

## 🔧 How It Works

The assistant listens for commands using the microphone.

Based on the command, it performs actions such as:

- Searching the web
- Fetching Wikipedia summaries
- Responding using OpenAI's GPT-3
- Opening websites
- Speaking back the response

If a chat-based request is made, it maintains the conversation context.

🔍 Example Commands

- "Open YouTube"
- "Search Google for Python programming"
- "Search Wikipedia for machine learning"
- "What is the time?"
- "Tell me a joke using artificial intelligence"
- "Jarvis quit" (Exits the assistant)

## 📜 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

Developed by Raksha Shetty
📧 Email: raksharshetty64@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/rshetty64/
💻 GitHub: github.com/rakshashetty66
