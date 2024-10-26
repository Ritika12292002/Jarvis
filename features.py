import os
import re
import webbrowser
from playsound import playsound
import eel
import pywhatkit as kit
from engine.Command import speak
from engine.config import ASSISTANT_NAME


#Playing assistant sound function

@eel.expose()
def playAssistantSound():
    music_dir = "C:\\Jarvis\\www\\assets\\audio\\start_sound (1).mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
      speak("Opening "+query)
      os.system('start '+query)
    else:
      speak("not found")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(query):
    pattern = r"play\s+(.+?)\s+on\s+youtube"
    match = re.search(pattern, query, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return None