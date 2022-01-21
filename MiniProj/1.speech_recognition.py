import pyttsx3 as p
import speech_recognition as sr
import portaudio

#import datetime

engine = p.init()
rate = engine.getProperty('rate') #speed of talking
engine.setProperty('rate',160) #change speed of talking
voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[3].id)# set your voice to voices[0] in array

#print(voices) #to check voices avialable in your system

#engine.say("hello  Richa, I am Silky. How are You")
 
engine.runAndWait()

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

    '''
def speak(audio):
 engine.say(audio) 
 engine.runAndWait() #Without this command, speech will not be audible to us.
def wishme():
    hour = int(datetime.datetime.now().hour)
    #print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
       speak("Good Evening!")
       speak("I am Silky sir. Please tell me how may i help you")
    if __name__=="__main__" :
      wishme()    
'''
 