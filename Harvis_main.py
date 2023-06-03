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

if __name__=="__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()

                if "go to sleep" in query:
                    speak("Ok sir!, You can call me anytime...")
                    break

                elif "hello" in query or "hello harvis" in query or "hi" in query or "hi harvis" in query:
                    speak("Hello! sir, how are you?")

                elif "i am fine" in query or "i am good" in query or "i am fine harvis" in query or "i am good harvis" in query:
                    speak("That's great sir")

                elif "who are you" in query or "tell me about yourself" in query or "who developed you" in query or "who created you" in query:
                    speak("I am Harvis sir...my beloved master Harsh developed me...love you master Harsh...")
                
                elif "how are you" in query or "how are you harvis" in query or "what about you" in query or "what about you harvis" in query:
                    speak("I am always perfect sir, tell me how may i help you...")

                elif "thank you" in query or "okay" in query or "ok" in query or "thanks" in query or "thank you harvis" in query or "thanks harvis" in query or "thank" in query:
                    speak("You're always welcome sir...")

                elif "tired" in query or "not feeling well" in query or "play song" in query or "play a song" in query or "play music" in query or "play a music" in query:
                    speak("Playing your favourite songs sir...")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=WBzeTz_UpQ4")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=jjbyGOC-mek")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=adOrNn7o2x0&list=PLQa-raPykPzJ32uLJf_DKGnzgKkwIA87m&index=183")
                    elif b==4:
                        webbrowser.open("https://www.youtube.com/watch?v=442ewPgXHQ0")
                    elif b==5:
                        webbrowser.open("https://www.youtube.com/watch?v=KzDzZs4sWkc")
                    elif b==6:
                        webbrowser.open("https://www.youtube.com/watch?v=pHX9Zcflmac")
                    elif b==7:
                        webbrowser.open("https://www.youtube.com/watch?v=rxGMLnsXGII")
                    elif b==8:
                        webbrowser.open("https://www.youtube.com/watch?v=iwcoKO2Yp8c")
                    else:
                        speak("Hope you will like it...")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video is paused sir...")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played again sir...")   

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video is muted sir...")

                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Turning volume up sir...")
                    volumeup()
                    
                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Turning volume down sir...")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)

                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from CalculateNumbers import WolfRamAlpha
                    from CalculateNumbers import Calc
                    query = query.replace("calculate", "")
                    Calc(query)

                elif "temperature" in query:
                    search = "temperature in pooney city of maharashtra is"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "weather" in query:
                    search = "weather in pooney city of maharashtra is"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%I:%M:%p")
                    speak(f"Sir, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep sir...Thank you...")
                    exit()
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    speak("You told me"+rememberMessage)
                    remember = open("remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what do you remember" in query:
                    remember = open("remember.txt", "r")
                    speak("you told me" + remember.read())