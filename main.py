#eel module is to use html,css,js with python
import os
import eel
from engine.features import *
from engine.engine import *;
def start():
    playassistantSound()
    eel.init("frontend")
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html',mode=None,host='localhost',block=True)
#now we will do multithreading so it should be in function
#now make run.py file for multithreading
#we do multithreading as we want both start and hotword to run simultaneously
