#status 7 videos done.
#https://www.youtube.com/watch?v=4HmfVduvbh8

def unmutemusic():
    root.unmuteButton.grid_remove()
    root.muteButton.grid()

def mutemusic():
    root.muteButton.grid_remove()
    root.unmuteButton.grid()

   
def resumemusic():
   root.ResumeButton.grid_remove()
   root.PauseButton.grid()
   mixer.music.unpause()
   AudioStatusLabel.configure(text ='playing.....')
   

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100
    

def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text ='stopped.....')

def pausemusic():
   mixer.music.pause()
   root.PauseButton.grid_remove()
   root.ResumeButton.grid()
   AudioStatusLabel.configure(text ='stopped.....')

def playmusic():
    ad = audiotrack.get()
    print(ad)
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.muteButton.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    AudioStatusLabel.configure(text ='playing.....')
   

def musicurl():
    dd = filedialog.askopenfilename()
    audiotrack.set(dd)
'''
issue -issue with dir path name video6- https://www.youtube.com/watch?v=3BAY42Zn0ws
 try:
    dd = filedialog.askopenfilename(initialdir='home/linux/Documents/python/taunt.wav',
                                 title = 'Select Audio File',
                                 filetype=(('MP3','*.mp3'),('Wav','*.wav')))
 except:
    dd = filedialog.askopenfilename(title = 'Select Audio File',
                                 filetype=(('MP3','*.mp3'),('Wav','*.wav')))                              
 audiotrack.set(dd)
  #print(dd)
'''
def createwidthes():
####################################################
 global AudioStatusLabel ,ProgressbarLabel,ProgressbarVolumeLabel,ProgressbarVolume

#################################################### Labels
 TrackLabel = Label(root,text='Select Audio Track:',background='lightskyblue',font=('arial',15,'italic bold'))
 TrackLabel.grid(row=0,column=0,padx=20,pady=20)

 AudioStatusLabel = Label(root,text='paused',background='lightskyblue',font=('arial',15,'italic bold'), width = 20)
 AudioStatusLabel.grid(row=2,column=1)

 ######################################################################## Entry Box ##########################################
 TrackLabelEntry = Entry(root,font= ('arial',16,'italic bold'),width=35,textvariable=audiotrack)
 TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

#######################################################################Buttons##############################################

 BrowseButton = Button(root,text='Search',bg='deeppink',font=('arial',13,'italic bold'),width=20,bd=5,activebackground='purple4', command = musicurl)
 BrowseButton.grid(row=0,column=2,padx=20,pady=20)

 PlayButton = Button(root,text='Play',bg='green2',font=('arial',13,'italic bold'), width=20,bd=5,activebackground='purple4',command = playmusic)
 PlayButton.grid(row=1,column=0,padx=20,pady=20)

 root.PauseButton = Button(root,text='Pause',bg='yellow',font=('arial',13,'italic bold'), width=20,bd=5,activebackground='purple4',command = pausemusic)
 root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

 root.ResumeButton = Button(root,text='Resume',bg='yellow',font=('arial',13,'italic bold'), bd=5,activebackground='purple4',command = resumemusic)
 root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
 root.ResumeButton.grid_remove()

 root.muteButton = Button(root,text='Mute',bg='yellow',font=('arial',13,'italic bold'), width=7,bd=5,activebackground='purple4',
 command = mutemusic)
 root.muteButton.grid(row=3,column=3)
 root.muteButton.grid_remove()

 root.unmuteButton = Button(root,text='Unmute',bg='yellow',font=('arial',13,'italic bold'), width=7,bd=5,activebackground='purple4',
  command = unmutemusic)
 root.unmuteButton.grid(row=3,column=3)
 root.unmuteButton.grid_remove()

 
 VolumeUpButton = Button(root,text='VolumeUp',bg='blue',font=('arial',13,'italic bold') ,width=20,bd=5,activebackground='purple4',command = volumedown) 
 VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)

 StopButton = Button(root,text='Stop',bg='red',font=('arial',13,'italic bold'), width=20,bd=5,activebackground='purple4',command = stopmusic)
 StopButton.grid(row=2,column=0,padx=20,pady=20)


 VolumeDownButton = Button(root,text='VolumeDown',bg='blue',font=('arial',13,'italic bold') ,width=20,bd=5,activebackground='purple4',command=volumeup)
 VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

########################################################### Progressbar Volume
 ProgressbarLabel = Label(root,text='',bg='red')
 ProgressbarLabel.grid(row=0,column=3,rowspan =3,padx=20,pady=20)
 ProgressbarLabel.grid_remove()

 ProgressbarVolume = Progressbar(ProgressbarLabel,orient= VERTICAL,mode='determinate',value= 0,
 length=190)
 ProgressbarVolume.grid(row=0,column=0,ipadx=5)

 ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
 ProgressbarVolumeLabel.grid(row=0,column=0)

from tkinter import*
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar

root = Tk()

root.geometry('1100x500+200+50')
root.title('Music Player')
root.resizable(False,False)
root.configure(bg='lightSkyblue')
#################################### Global Variable
audiotrack= StringVar()
currentvol = 0
pvalue = 0.4
####################################create Slider
ss ='Developed by Richa Patil'
count = 0
text = ''
SliderLabel = Label(root,text=ss,bg='lightskyblue',font=('arial',40,'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3) 

def IntroLabelTrick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text =''
        SliderLabel.configure(text=text)
    else:
        text =text+ss[count]
        SliderLabel.configure(text=text)
    count +=1
    SliderLabel.after(200,IntroLabelTrick)

IntroLabelTrick()
createwidthes()
mixer.init()
root.mainloop()

#status- images not written on button video 3, 10 mins onwards