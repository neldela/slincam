from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.font import Font
import os
from time import time, sleep

menu = Tk()


menu.attributes('-fullscreen',True)
menu.configure(background="#292929")

bgImage = PhotoImage(file = '/home/pi/Documents/slincam/Assets/Graphics/menulayout.png')
Label(image = bgImage).place(x=-1, y=-1)

font2 = Font(size=18,weight="bold")

#----------------------------------------------------------------------------------
                                                                #VIDEO BUTTON
def videomode_clicked():
    os.system('python3 /home/pi/Documents/slincam/Assets/videomode.py')

videomode_btn = Button(menu, text="VIDEO",borderwidth=0, highlightthickness=0,
                       padx=40,pady=68,fg="white", bg="#141414",
                       activebackground="#e2ca03",
                       command=videomode_clicked)
videomode_btn['font'] = font2
videomode_btn.place(x=317, y=157)

#----------------------------------------------------------------------------------
                                                                #Photo BUTTON
def photomode_clicked():
    os.system('python3 /home/pi/Documents/slincam/Assets/photomode.py')

photomode_btn = Button(menu, text="PHOTO",borderwidth=0, highlightthickness=0,
                       padx=35,pady=68,fg="white", bg="#141414",
                       activebackground="#f30924",
                       command=photomode_clicked)
photomode_btn['font'] = font2
photomode_btn.place(x=84, y=157)

#----------------------------------------------------------------------------------
                                                             #TIMELAPSE BUTTON
def tlmode_clicked():
    os.system('python3 /home/pi/Documents/slincam/Assets/timelapsemode.py')

tl_btn = Button(menu, text="TIMELAPSE",borderwidth=0, highlightthickness=0,
                       padx=7,pady=68,fg="white", bg="#141414",
                       activebackground="#09f3e0",
                       command=tlmode_clicked)
tl_btn['font'] = font2
tl_btn.place(x=550, y=157)

#----------------------------------------------------------------------------------
                                                             #QUIT BUTTON
def quitmenu():
    menu.destroy()
    

quit_btn = Button(menu, text=quitmenu, fg="#141414", bg="#141414",
                  borderwidth=0, highlightthickness=0, command=quitmenu)
quit_btn.place(x=640, y=440)
#----------------------------------------------------------------------------------

mainloop()