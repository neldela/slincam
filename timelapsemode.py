                                                            #TIMELAPSE MODE SETUP
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
from tkinter import HORIZONTAL
import threading
import time
import os
from gpiozero import Button

root = tk.Tk()

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

bgImage = tk.PhotoImage(file = '/home/pi/Documents/slincam/Assets/Graphics/layouttimelapse.png')
tk.Label(image = bgImage).place(x=-1, y=-1)

#--------------------------------------------------------------------------------
                                                                            #FONT
font1 = Font(size=15,weight="bold")
font2 = Font(size=18,weight="bold")
font3 = Font(size=8,weight="bold")
font4 = Font(size=35,weight="bold")

#--------------------------------------------------------------------------------
                                                                #CAMERA SETTINGS 
camera.resolution = (1920, 1080)

camera.sharpness = -40

camera.contrast = -15

camera.saturation = -15

camera.exposure_compensation = 0

camera.start_preview(fullscreen=False,window=(0,0,700,394))

image_denoise = False

video_denoise = False 

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


iso_slider = tk.Scale(root, from_=min(iso_values), to=max(iso_values),
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
  
    
str_slider = tk.Scale(root, from_=min(str_values), to=max(str_values),
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

        
wb_slider = tk.Scale(root, from_=min(wb_values), to=max(wb_values),
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
    
    
menu_btn = tk.Button(root, text="MENU", padx=23,pady=32,borderwidth=0,
                   highlightthickness = 0, fg="#292929", bg="#09f3e0",
                   activebackground="#292929", command=menu_clicked)
menu_btn['font'] = font1
menu_btn.place(x=688, y=392)
#--------------------------------------------------------------------------------
                                                                #INTERVALL BUTTON
def intervall_clicked():
    if intervall_btn.config('text')[-1] == '2':
        intervall_btn.config(text='5', padx=24,pady=6)
        
    elif intervall_btn.config('text')[-1] == '5':
        intervall_btn.config(text='10', padx=8,pady=6)
       
    else:
        intervall_btn.config(text='2', padx=24,pady=6)
        
        
        
intervall_btn = tk.Button(root, text="2", padx=24,pady=6,borderwidth=0,
                       highlightthickness = 0, fg="white", bg="#292929",
                       activebackground="#292929", command=intervall_clicked)

intervall_btn['font'] = font4
intervall_btn.place(x=712, y=168)

intervall_btn.invoke()

#---------------------------------------------------------------------------
                                                            #SCOPE BUTTON

#img = Image.open('/home/pi/Documents/slincam/Assets/Graphics/scope_overlay.png')

#pad = Image.new('RGB', (
       # ((img.size[0] + 31) // 32) * 32,
       # ((img.size[1] + 15) // 16) * 16,
       # ))

#pad.paste(img, (0, 0))

#o = camera.add_overlay(pad.tobytes(), size=img.size)

#o.alpha = 100
#o.layer = 5
        


        
duration_btn = tk.Button(root, text="STOP", padx=13,pady=0,borderwidth=0,
                       highlightthickness = 0, fg="white", bg="#292929",
                       activebackground="#292929")

duration_btn['font'] = font1
duration_btn.place(x=712, y=312)



#--------------------------------------------------------------------------------
                                                               #START/STOP BUTTON
   
def start_tl():
    if rec_btn['text'] == 'STOP':
        t.join(1)
        rec_btn.config(text='START', fg="red", bg="#292929")
        camera.close()
        root.destroy()
        menu.destroy()
        os.system('python3 /home/pi/Documents/slincam/slincam_menu.py')
        return

    if rec_btn['text'] == 'START':
        t.start()
        rec_btn.config(text='STOP', fg="#292929", bg="red", padx=20)
        return

def process_file():
    i = 1
    while rec_btn['text'] == 'STOP':
        i = i+1
        rec_btn.update()
        sleep(5)
        for filename in camera.capture_continuous('/media/root/FOOTAGE/Timelapse/tl_img{counter:03d}.jpg', use_video_port=True):
            sleep(int(intervall_btn.cget('text')))

    
             
rec_btn = tk.Button(root,text="START",
                          padx=11,pady=56,borderwidth=0,highlightthickness = 0,
                          fg="red",bg="#292929", command=lambda: start_tl())
rec_btn['font'] = font1
rec_btn.place(x=705, y=6)


t = threading.Thread(target=process_file)

#--------------------------------------------------------------------------------
                                                             #PHYSICAL REC. tk.Button
tl_capture_btn=Button(14)

running = True

tl_capture_btn.when_pressed = start_tl

#----------------------------------------------------------------------------------

#main loop    
root.mainloop()
