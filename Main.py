from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import time

#import sounddevice as sd
# import soundfile as sf

#fs = 44100
#print(sd.query_devices())
#data, fs = sf.read('19_noBreathing.wav', dtype='float32')
#sd.play(data, fs)
#sd.wait()
while True:
    keyDown('z')
    keyDown('m')
    time.sleep(1)
    keyUp('z')
    keyUp('m')
    time.sleep(1)
    #myarray = sd.rec(int(2 * fs), samplerate=fs, channels=2)
    #sd.wait()
    #sd.play(myarray, fs)
    #sd.wait()