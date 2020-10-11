import pafy
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry('380x230')  #Size of the window
window.title("Audio Downloader") #Name of the Window
url_var = tk.StringVar()

#declare the function

def click():
    url = url_entry.get()
    audio = pafy.new(url)

    best_audio = audio.getbestaudio() #Select the best audio
    best_audio.download() #Download the audio

#Tkinter Front-end 

lbl = Label(window, text="Youtube", bg= "red", font=("Aerial Bold",30))
lbl.grid(column=0, row=0)

lbl1 = Label(window, text="Audio Downloader", bg="blue", font=("Aerial Bold",20))
lbl1.grid(column=0, row=1)

lbl2 = Label(window,text=" ")
lbl2.grid(column=0, row=2)

lbl3 = Label(window, text="Enter the link below", font=("Aerial Bold",10))
lbl3.grid(column=0, row=3)

url_entry = tk.Entry(window, textvariable = url_var, width=60)
url_entry.grid(column=0, row=4)

btn = Button(window, text="Download",bg="red", fg="white",command=click)
btn.grid(column=0,row=5)

lbl4 = Label(window, text="Created by Saiman", font=("Aerial Bold",10))
lbl4.grid(column= 0, row=6)

buttn = tk.Button(text= "Quit", command= window.quit)
buttn.grid(column=0, row=7)

window.mainloop()
