from cProfile import label
from logging import root
from tkinter.font import BOLD,ITALIC
from unittest import result
from pytube import YouTube
import sys
import time
from tkinter import *

link = ""

root = Tk()

root.title("you tube video saver")

root.configure(background="#33ccff")

l1 = Label(root,padx=180,pady=10,background="#33ccff")
l1.grid(row=1,column=1)

title = Label(root,text="youtube video saver",font = ("ALGERIAN",40,BOLD), foreground="red",background="black",padx=80,pady=5)
title.grid(row=1,column=2)

l1 = Label(root,padx=180,pady=20,background="#33ccff")
l1.grid(row=2,column=2)

photo = PhotoImage(file="C:\\Users\\USER\\Downloads\\download.png")
l_ima = Label(root,image=photo)
l_ima.grid(row=3,column=2)

l1 = Label(root,padx=180,pady=20,background="#33ccff")
l1.grid(row=4,column=2)

label_paste = Label(root,text="paste youtube video link here",font = ("ALGERIAN",30,ITALIC),padx=100,pady=10,background="#33ccff")
label_paste.grid(row=5,column=2)


text_result = Text(root,width=100,height=2,foreground="#6960EC")
text_result.grid(row=6,column=2)


def main():
    
    link = str(text_result.get(1.0,END))
    yt = YouTube(link)
    stearm = yt.streams.get_highest_resolution()
    stearm.download()

button_translate = Button(root,padx=50,text="download", foreground="red",background="#33ff33",font = ("ALGERIAN",20,ITALIC),pady=10,command=main)
button_translate.grid(row=7,column=2)
 
print("successfully completed")

root.mainloop()



# print("""
#        _______
#       | -   - |
#       |___=___|
#   ()_____[|]_____()
#          [|]
#       ___[|]___
#       |       |
#      _|_     _|_    
      
#       """)