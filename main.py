#eel module is to use html,css,js with python
import os
import eel
from engine.features import *;
playassistantSound()
eel.init("frontend")
os.system('start msedge.exe --app="http://localhost:8000/index.html"')
eel.start('index.html',mode=None,host='localhost',block=True)