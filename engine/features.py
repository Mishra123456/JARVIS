from shlex import quote
import struct
import subprocess
from playsound import playsound
import os
import eel
import pyaudio
import pyautogui
from engine.engine import *;
from engine.configure import ASSISTANT_NAME
from engine.helper import extract_yt_term, remove_words
import pywhatkit as kit
import re
import sqlite3
import webbrowser
import pvporcupine
from engine.db import con, cur
con=sqlite3.connect("jarvis.db")
cur=con.cursor()
@eel.expose
def playassistantSound():
    # Correct relative path
    music_dir = os.path.join('frontend', 'assets', 'audio', 'jar1.mp3')
    # Verify path exists
    if not os.path.exists(music_dir):
        print(f"Error: File not found at {os.path.abspath(music_dir)}")
        return
    
    try:
        playsound(music_dir)
    except Exception as e:
        print(f"Error playing sound: {e}")

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    app_name = query.strip()
    # if(query!=""):
    #     speak("opening" + query)
    #     os.system("start"+ query)
    # else:
    #     speak("not found")
    if app_name != "":

        try:
            cur.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cur.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cur.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cur.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

# def extract_yt_term(command):
#     # Define a regular expression pattern to capture the song name
#     pattern = r'play\s+(.*?)\s+on\s+youtube'
#     # Use re.search to find the match in the command
#     match = re.search(pattern, command, re.IGNORECASE)
#     # If a match is found, return the extracted song name; otherwise, return None
#     return match.group(1) if match else None

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j i.e virtually pressing not on keyboard
                
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
         
    except:
        traceback.print_exc() 
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
# used for hot word detection specially hey siri etc

def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)
    try:
        query = query.strip().lower()
        cur.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cur.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
def whatsApp(mobile_no, message, flag, name):
    

    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    # pyautogui.hotkey('ctrl', 'f')

    # for i in range(1, target_tab):
    #     pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)

