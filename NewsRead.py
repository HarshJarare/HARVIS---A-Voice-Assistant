import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import webbrowser
import pyautogui
import random
import json

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 150
        audio = r.listen(source,0,4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query

def latestnews():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=009eeca105df4827b73779d3c79a5f97", 
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=009eeca105df4827b73779d3c79a5f97",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=009eeca105df4827b73779d3c79a5f97", 
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=009eeca105df4827b73779d3c79a5f97", 
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=009eeca105df4827b73779d3c79a5f97", 
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=009eeca105df4827b73779d3c79a5f97"}
    
    content = None
    url = None
    speak("Which field news do you want, [business], [science], [entertainment], [health], [sports], [technology]")
    field = input("Type field news that you want:")
    for key, value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("URL was found")
            break
        else:
            url = True
    if url is True:
                print("URL not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news sir...")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"For more info visit: {news_url}")

        a = input("[Press 1 to continue] and [Press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            speak("That's all sir...")
            break