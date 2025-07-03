import sounddevice as sd
import wavio as wv

duration=10
freq=44100

print("start.......")
recording= sd.rec(int(duration*freq),samplerate=freq,channels=1,dtype='int16') 
sd.wait()
print("recorded")

wv.write("file1.wav",recording,freq,sampwidth=2)
print("stored it")

print("playing......")
from playsound import playsound 
file=playsound('file1.wav')

