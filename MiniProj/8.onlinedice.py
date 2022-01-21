import random
from Tkinter import *
import Tkinter

# creating tkinter window
root=Tk()
# use multiplication original sign X not asterisk

# creating fixed geometry of the
# tkinter window with dimensions 700x450
root.geometry("700x450")
l1=Label(root,font=("times",200))

def roll():
      number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
      l1.config(text=f"{random.choice(number)}{random.choice(number)}")
      l1.pack()

 b1=Button(root,text ="let roll...", command=roll)
 b1.place(x=350,y=0)

# Execute Tkinter
root.mainloop()

#note line 16 syntax issue
#https://www.youtube.com/watch?v=8QdBZH1h5H8