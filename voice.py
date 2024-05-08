import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess  # For opening external applications

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        # Use Google Web Speech API for recognition
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return "I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, there's an error with the recognition service."

# Main function to run the voice assistant
def voice_assistant():
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = recognize_speech()
        print(f"You said: {command}")

        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "how are you" in command:
            speak("I am fine, thank you! How can I assist you?")
        elif "time" in command:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M")
            speak(f"The current time is {current_time}.")
        elif "date" in command:
            today = datetime.date.today()
            speak(f"Today is {today.strftime('%A, %B %d, %Y')}.")
        elif "search" in command:
            search_term = command.replace("search", "").strip()
            if search_term:
                speak(f"Searching for {search_term}...")
                webbrowser.open(f"https://www.google.com/search?q={search_term}")
        elif "open notepad" in command:
            speak("Opening Notepad...")
            subprocess.Popen(["notepad.exe"])  # Open Notepad
        elif "open calculator" in command:
            speak("Opening Calculator...")
            subprocess.Popen(["calc.exe"])  # Open Calculator
        elif "open spotify" in command:
            speak("Opening Spotify...")
            subprocess.Popen(["spotify"])  # Open Spotify
        elif "stop" in command:
            speak("Thank you! Goodbye!")
            break
        else:
            speak("I didn't understand that. Can you please repeat it?")
            
# Run the voice assistant
voice_assistant()
