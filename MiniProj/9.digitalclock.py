#https://www.youtube.com/watch?v=at7rpdT8FeI


from Tkinter import *
import ttk
from time import strftime


root = Tk()
root.title("Clock")

def time():
     string = strftime('%H:%M:%S %p')
     label.config(text=string)
     label.after(1000,time)

label = Label(root, font =("ds-digital",80), background = "black", foreground ="cyan")
label.pack(anchor ='center')
time()
mainloop()