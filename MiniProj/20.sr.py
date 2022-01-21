from datetime import datetime   
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break





'''# import required module
from playsound import playsound
  
# for playing note.wav file
playsound('/audio.mp3')
print('playing sound using  playsound')'''





'''import speech_recognition as sr
import portaudio
r=sr.Recognizer()
with sr.Microphone() as source:
  print('Speak Anything:')
  audio = r.listen(source)
  try:
      text=r.recognize_google(audio)
      print('you said: {}'.format(text))
  except:
      print('sorry could not recognize voice')'''