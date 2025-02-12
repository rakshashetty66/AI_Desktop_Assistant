import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import wikipedia
import pyttsx3
from config import apikey

# Initialize OpenAI API key securely
openai.api_key = apikey

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speed
engine.setProperty("volume", 1.0)  # Set volume


def say(text):
    """Speaks the given text using text-to-speech."""
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Listens to user input and converts speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduces noise

        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return "I couldn't understand that."
        except sr.RequestError:
            return "Error connecting to speech recognition service."
        except Exception as e:
            print("Speech recognition error:", e)
            return "Some error occurred."

# Function to search Wikipedia
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        say(result)
    except wikipedia.exceptions.DisambiguationError:
        say("Multiple results found. Please be more specific.")
    except wikipedia.exceptions.PageError:
        say("I couldn't find any information on that topic.")

# Function to search Google
def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    say(f"Here are the results for {query}")


def chat(query):
    """Handles AI chat responses."""
    global chatStr
    chatStr += f"User: {query}\nJarvis: "

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response["choices"][0]["text"].strip()
        chatStr += f"{response_text}\n"
        say(response_text)
        return response_text
    except Exception as e:
        print("Error in OpenAI API call:", e)
        return "Sorry, I encountered an error."


def ai(prompt):
    """Generates AI-based responses and saves to a file."""
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response["choices"][0]["text"].strip()

        # Save response to a file
        os.makedirs("Openai", exist_ok=True)
        filename = f"Openai/{random.randint(1, 100000)}.txt"
        with open(filename, "w") as f:
            f.write(response_text)

        return response_text
    except Exception as e:
        print("Error in AI function:", e)
        return "Error in generating response."

# Main loop
if __name__ == "__main__":
    print("Welcome to Jarvis A.I")
    say("Welcome to Jarvis A.I")

    while True:
        query = takeCommand()

        if "open youtube" in query:
            say("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            say("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            say(f"Sir, the time is {current_time}")

        elif "search wikipedia for" in query:
            topic = query.replace("search wikipedia for", "").strip()
            search_wikipedia(topic)

        elif "search google for" in query:
            topic = query.replace("search google for", "").strip()
            search_google(topic)

        elif "using artificial intelligence" in query:
            response = chat(query)
            print(response)

        elif "exit" in query or "jarvis quit" in query:
            say("Goodbye!")
            break

        elif "reset chat" in query:
            chatStr = ""
            say("Chat history reset.")

        else:
            print("Chatting...")
            chat(query)
