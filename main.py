#This code is to import tkinter libraries remeber to do py install tk!
#This code is under the license of Creative Commons Zero v1.0 Universal
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("My Awesome Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)
#To make the clock format 12 hrs. Simply change the strftime('%H:%M:%S %p') to strftime('%I:%M:%S %p').    
label = Label(root, font = "ds-digital 100", background = "white", foreground = "black")
label.pack(anchor = "center")

time()

mainloop()
