import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from os import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("I am basu. I am Aditya's friend")


def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listining.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please")
        print("Say that again please...")
        return"None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adityapandey2088888888@gmail.com', '28k2@#96@-#')
    server.sendmail('adityapandey2088888888@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

       # Logic for executing tasks on query
        if 'wikipedia' in query:
            speak("Searching wikipedia.......")
            query = query.replace("wkipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'quit' in query:
            speak("quitting jarvis, good bye sir, have a beautiful day")
            sys.exit()

        elif'open youtube' in query:
            webbrowser.open("youtube.com")

        elif'open google' in query:
            webbrowser.open("google.com")

        elif'open facebook' in query:
            webbrowser.open("facebook.com")

        elif'open school' in query:
            webbrowser.open("ingrails.com/school/parents?token=1601192998")

        elif'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif'who is manish' in query:
            speak("manish is a boy with a cow hair")

        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, The time is{strTime}")

        elif'open code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening")
            os.startfile(codePath)

        elif'open opera' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            speak("opening")
            os.startfile(codePath)

        elif'who are you' in query:
            speak("""I am basu, Adityas's friend, I love helping people while working. You can 
            give me any command. I was created just few hours ago. I am in the learning phase, sir""")

        elif'thanks' in query:
            speak("my pleasure, Aditya")

        elif'hello' in query:
            speak(
                "Hi, it's my pleasure to meet you, please tell me your name, I will love to hear your name")

        elif'what can you do' in query:
            print(speak)
            speak("""
            1 I can send email
            2 I can open browsers you have specefied
            3 I can open visual studio code 
            4 I can response to your name
            5 I can tell time 
            6 I can response to your answer s you have specified
            """)

        elif'my name is' in query:
            speak("It's a beautiful name")

        elif'who is aditya ' in query:
            speak("He is my creatoR, He control me and develop my system")

        elif 'music 1' in query:
            speak("Playing musing.....")
            music_dir = 'C:\\Users\\Lenovo\\Music\\favourite music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'music ' in query:
            speak("Playing music.....")
            music_dir = 'C:\\Users\\Lenovo\\Music\\favourite music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'music 2' in query:
            speak("Playing musing.....")
            music_dir = 'C:\\Users\\Lenovo\\Music\\favourite music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'music 1' in query:
            speak("Playing musing.....")
            music_dir = 'C:\\Users\\Lenovo\\Music\\favourite music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif'send email to friend' in query:
            try:
                speak("What should I say")
                content = takecommand()
                to = "adityapandey2088888888@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                speak("Sorry, Aditya. I can't send email at the movement")