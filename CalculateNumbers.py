import wolframalpha
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import webbrowser
import pyautogui
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "U8PP6E-4HQW65K2UY"
    requester = wolframalpha.Client(apikey)
    requested = requester.query()

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable...sir")

def Calc(query):
    Term = str(query)
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("divide", "/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable...sir")
    