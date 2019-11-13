# NOTE: this example requires PyAudio because it uses the Microphone class
from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import time
import speech_recognition as sr

import argparse
import queue
import sys

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import threading

def func1(audio, r):
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        #t0 = time.time()
        text = r.recognize_google(audio)
        #t1 = time.time()

       # total = t1-t0

       # print(total)

        if("start") in text:
            keyDown(' ')
            time.sleep(0.5)
            keyUp(' ')
        if ("right" or "bright" or "rice") in  text:
            keyDown(';')
            #time.sleep(1)
            keyUp(';')
            #press(';')
        
        elif ("Celeste" or"left" or "set")  in  text:
            print("enter in left")
            keyDown('z')
            #time.sleep(1)
            keyUp('z')
            #press('z')

        print("Google Speech Recognition thinks you said " + text)
        
    except :
         pass

        #print("Google Speech Recognition could not understand audio")
    #except sr.RequestError as e:
    #    print("Could not request results from Google Speech Recognition service; {0}".format(e))

while True:

    
    r = sr.Recognizer()
    #r.energy_threshold = 2000;
    r.pause_threshold = 0.5
    with sr.Microphone(sample_rate=8000, chunk_size=256) as source:
        #print("Say something!")
        audio = r.listen(source,0,1)
        #print( audio.get_wav_data() )
        #print( audio )
    
    thread1 = threading.Thread(target = func1, args = (audio, r))
    thread1.start()
