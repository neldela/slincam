                                                                #PHOTOMODE SETUP

#Tkinter Import
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
import os


root = Tk()
root.configure(background='black')

#Fullscreen
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)

   
#Pi Camera Import
from time import sleep
from picamera import PiCamera
camera = PiCamera()

#--------------------------------------------------------------------------------

bgImage = PhotoImage(file = '/home/pi/Documents/slincam/Assets/Graphics/layoutphoto.png')
Label(image = bgImage).place(x=-1, y=-1)

#--------------------------------------------------------------------------------
                                                                            #FONT
font1 = Font(size=15,weight="bold")
font2 = Font(size=18,weight="bold")
font3 = Font(size=8,weight="bold")

#--------------------------------------------------------------------------------
                                                                #CAMERA SETTINGS 
camera.resolution = (3600, 2400)

camera.sharpness = -15

camera.contrast = -15

camera.saturation = -15

camera.exposure_compensation = 0

camera.start_preview(fullscreen=False,window=(0,0,600,400))

#--------------------------------------------------------------------------------
                                                                      #ISO SLIDER 
iso_values = {
    0: "ISO AUTO",
    1: "ISO 100",
    2: "ISO 200",
    3: "ISO 300",
    4: "ISO 400",
    5: "ISO 500",
    6: "ISO 600",
    7: "ISO 700",
    8: "ISO 800"
}

iso_modes = {
    0: 0,
    1: 100,
    2: 200,
    3: 300,
    4: 400,
    5: 500,
    6: 600,
    7: 700,
    8: 800
}

def iso_get():
    camera.iso = iso_modes[iso_slider.get()]

def iso_values_label(value):
    iso_slider.config(label=iso_values[int(value)])
    iso_get()    


iso_slider = Scale(root, from_=min(iso_values), to=max(iso_values),
             showvalue=False, orient=HORIZONTAL,
             borderwidth=0,highlightthickness=0,
             bg="#292929", fg="white", troughcolor="grey", font="font1",
             length=200, width=30,
             command=iso_values_label)

iso_slider.set(1)

iso_slider.place(x=16, y=405)

#--------------------------------------------------------------------------------
                                                             #SHUTTERSPEED SLIDER
str_values = {
    0: "1/50",
    1: "1/60",
    2: "1/80",
    3: "1/100",
    4: "1/125",
    5: "1/160",
    6: "1/200"
}

str_modes = {
    0: 20000,
    1: 16666,
    2: 12500,
    3: 10000,
    4: 8000,
    5: 6250,
    6: 5000
}

def str_get():
    camera.shutter_speed = str_modes[str_slider.get()]

def str_values_label(value):
    str_slider.config(label=str_values[int(value)])
    str_get()    
  
    
str_slider = Scale(root, from_=min(str_values), to=max(str_values),
             showvalue=False, orient=HORIZONTAL,
             borderwidth=0,highlightthickness=0,
             bg="#292929", fg="white", troughcolor="grey", font="font1",
             length=200, width=30,
             command=str_values_label)

str_slider.set(1)

str_slider.place(x=245, y=405)

#--------------------------------------------------------------------------------
                                                            #WHITE BALANCE SLIDER
wb_values = {
    0: "AWB",
    1: "sunlight",
    2: "cloudy",
    3: "shade",
    4: "tungsten",
    5: "fluorescent",
    6: "incandescent",
    7: "flash",
    8: "horizon"
}


wb_modes = {
    0: "auto",
    1: "sunlight",
    2: "cloudy",
    3: "shade",
    4: "tungsten",
    5: "fluorescent",
    6: "incandescent",
    7: "flash",
    8: "horizon"
}

def wb_get():
    camera.awb_mode = wb_modes[wb_slider.get()]

def wb_values_label(value):
    wb_slider.config(label=wb_values[int(value)])
    wb_get()    

        
wb_slider = Scale(root, from_=min(wb_values), to=max(wb_values),
                  orient=HORIZONTAL, showvalue=False, command=wb_values_label)                  

wb_slider.configure(borderwidth=0,highlightthickness=0,
             bg="#292929", fg="white", troughcolor="grey", font="font1",
             length=200, width=30)

wb_slider.set(1)

wb_slider.place(x=470, y=405)

#--------------------------------------------------------------------------------
                                                                     #MENU BUTTON
def menu_clicked():
    camera.close()
    root.destroy()
    menu.destroy()
    os.system('python3 /home/pi/Documents/slincam/slincam_menu.py')
    
    
menu_btn = Button(root, text="MENU", padx=23,pady=32,borderwidth=0,
                   highlightthickness = 0, fg="#292929", bg="#f30924",
                   command=menu_clicked)
menu_btn['font'] = font1
menu_btn.place(x=688, y=392)

#---------------------------------------------------------------------------
                                                               #STABILIZER BUTTON
def stab_on():
    camera.video_stabilization = True
    
def stab_off():
    camera.video_stabilization = False
    
    
def stabl_btn_clicked():
    if stabl_btn['text'] == "~ OFF":
        stab_on()
        stabl_btn.configure(text="~ ON")
        
    
    else:
        stab_off()
        stabl_btn.configure(text="~ OFF")
        
        


stabl_btn = Button(root, text="~ OFF", padx=18,pady=31,borderwidth=0,
                   highlightthickness = 0, fg="white", bg="#292929",
                   command=stabl_btn_clicked)
stabl_btn['font'] = font1
stabl_btn.place(x=630, y=149)

#---------------------------------------------------------------------------
                                                               #Capture BUTTON
def take_pic():
    camera.capture('/home/pi/Desktop/pic.jpg', quality=100)

capture_btn = Button(root, text="shutter", padx=30,pady=40,borderwidth=0,
                   highlightthickness = 0, fg="white", bg="#292929",
                   command=take_pic)
capture_btn['font'] = font1
capture_btn.place(x=630, y=20)
#----------------------------------------------------------------------------------

#main loop    
root.mainloop()
