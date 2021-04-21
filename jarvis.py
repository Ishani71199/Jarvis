import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import winshell
import subprocess
import time
import requests

engine = pyttsx3.init('sapi5')  # sapi5 take inbuild voice in windows
voices = engine.getProperty('voices')   #Two voices are inbuilt: female voice and male voice
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)  #taking the female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis. How can i help you")


def takeCommand():  #takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        # r.pause_threshold = 1 #if gap of 1sec is taken by user it ensure that it take the input after 1sec
        audio = r.listen(source)
    try:
        print('Recognizing')
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        print('Please say that again....')
        return 'None'
    return query


if __name__ == "__main__":
    greeting()

    while True:
        query = takeCommand().lower()
        #logic to execute task

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            webbrowser.open("https://youtu.be/_pLO4jFDeIc")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'date' in query:
            strDate = datetime.datetime.now().date()
            print(strDate)
            speak(f"Sir, the date is {strDate}")

        elif 'search' in query:
            webbrowser.open(f"{query}")

        elif 'empty recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")
            except Exception as e:
                speak("Already empty")

        elif "log off" in query or "sign out" in query or "log out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Ishani")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Ishani")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif 'quit' in query:
            speak("Thanks for giving me your time")
            exit()





