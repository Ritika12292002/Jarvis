from winreg import QueryValue
import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index to select different voices
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:  # Correct usage of sr.Microphone
        print('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, timeout=10, phrase_time_limit=6)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(1)
        eel.ShowHood()
    except Exception as e:
       
        return ""
    
    return query.lower()

text = takecommand()
if text:
    speak(text)


@eel.expose
def Allcommand():
    
      query =  takecommand()
      print(query)

      if "open" in query:
       from engine.features import openCommand
       openCommand(query)
      elif "on youtube" in query:
       from engine.features import PlayYoutube
       PlayYoutube(query)
       
    
