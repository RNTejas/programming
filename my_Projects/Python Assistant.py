import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

MASTER = "Tejas"

print("Initializing Python Assistant")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

# this function will wish me
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    #
    if hour>=0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >=12 and hour < 18:
        speak("Good Afternoon" + MASTER )

    else:
        speak("Good Evening" + MASTER)
    speak("Welcome to Python Assistant. What would you like to search for....?")

# this function will takes command from mice
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Sorry, I was not able to Hear that! Please try again")
        speak("Sorry, I was not able to Hear that! Please try again")


# the main program starts from here
speak("Initializing Python Assistant...")
wishMe()
takeCommand()


