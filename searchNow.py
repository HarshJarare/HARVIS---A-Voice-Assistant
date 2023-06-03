import pyttsx3
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser

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
        audio = r.listen(source,0,3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("harvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what i found on google sir...")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            print(result)
            speak(result)

        except:
            speak("No speakable output available...")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what i found on youtube...")
        query = query.replace("harvis", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("hope you will like it sir...")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia sir...")
        query = query.replace("harvis", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia...")
        print(results)
        speak(results)