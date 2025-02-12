# Jarvis AI

Jarvis AI is a voice-controlled virtual assistant that can perform tasks like searching Google and Wikipedia, telling the time, and engaging in AI-powered conversations.

## Features
- Voice commands for opening websites (YouTube, Google, etc.)
- Wikipedia search
- Google search
- AI chat using OpenAI API
- Text-to-speech (TTS) responses
- Speech recognition for user input

## Installation

1.  **Clone the repository:**

    ```
    git clone https://github.com/rakshashetty66/AI_Desktop_Assistant.git
    cd AI_Desktop_Assistant
    ```
2.  **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```
3.  **Set up your OpenAI API key:**

    *   Create a `.env` file in the root directory of the project.
    *   Add the following line to the `.env` file, replacing `your_api_key_here` with your actual OpenAI API key:

        ```
        OPENAI_API_KEY=your_api_key_here
        ```

4.  **Run the program:**

    ```
    python main.py
    ```

## Usage

*   Speak commands such as "open YouTube", "search Wikipedia for Python", or "what is the time?".
*   To stop the assistant, say "exit" or "Jarvis quit".

## Dependencies

*   `speech_recognition`
*   `pyttsx3`
*   `wikipedia`
*   `openai`
*   `dotenv`
*   `datetime`
*   `webbrowser`

## Contributing

Feel free to fork this repository and contribute improvements. If you find any issues, please open a pull request.

## License

This project is open-source and available under the MIT License.
