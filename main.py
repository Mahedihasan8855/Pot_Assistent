import pyttsx3
import datetime
import wikipedia
import webbrowser
import youtube_search
from youtubesearchpython.__future__ import VideosSearch
import speech_recognition as sr
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir")
    elif 12 < hour <= 15:
        speak("Good Noon Sir")
    elif 15 < hour <= 18:
        speak("Good Afternoon Sir")
    elif 18 < hour <= 20:
        speak("Good Evening Sir")
    else:
        speak("Goob Night Sir")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio)
        print(f"User said: \n{query}")
    except Exception as e:
        print("Sorry Sir, I didn't get it Say that again please....")
        speak("Sorry Sir, I didn't get it Say that again please....")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "what is your name" in query:
            speak("I am pothead How can I help you Sir?")

        elif "what's your name" in query:
            speak("My name is Pothead How can I help you Sir?")
        elif "who are you" in query:
            speak(
                "I am pothead 1.0.0. I am a virtual assistant  Programmed by- Maahedi Hassan. How can I help you Sir?"
            )

        elif 'wikipedia' in query:
            speak("Searching in wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia....")
            print(results)
            speak(results)
        elif 'hi' in query:
            speak("Hello")
        elif 'hello' in query:
            speak("Hello, How are you")
        elif 'how are you' in query:
            speak("I am fine")
        elif 'where are you' in query:
            speak("I am just in your device")

        elif "youtube" in query:
            speak("Searching in youtube.....")
            query = query.replace("youtube", "")
            webbrowser.open("https://www.youtube.com/results?search_query=" +
                            query)
        elif "play song" in query:
            speak("Searching in gaana.....")
            query = query.replace("play song", "")
            webbrowser.open("https://gaana.com/search/" + query)

        elif "google" in query:
            speak("Searching in google.....")
            query = query.replace("google", "")
            webbrowser.open("https://www.google.com/search?q=" + query)
        elif "open gmail" in query:
            speak("opening gmail.....")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        elif "open google" in query:
            webbrowser.open("https://www.google.com/")
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
        elif "open github" in query:
            webbrowser.open("https://www.github.com/")
        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com/")
        elif "open music" in query:
            webbrowser.open("https://gaana.com/")
        elif "open spotify" in query:
            os.startfile(
                "C:\\Users\\mahed\\AppData\\Roaming\\Spotify\\Spotify.exe")
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is now {time}")
            print(f"Sir the time is now {time}")

        elif "exit" in query:
            speak("Thank you sir for using me. Have a nice day Sir. Good Bye")
            print("Thank you sir for using me. Have a nice day Sir. Good Bye")
            break
