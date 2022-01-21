#Ref code-https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-120
# not working
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

if __name__=="__main__":
    speak("richa is amazing")