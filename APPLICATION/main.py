import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import time
from tkinter import messagebox
import mysql.connector

# window theme =============================================================================================================================================================================
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
# window theme ==============================================================================================================================================================================

# splash screen ==============================================================================================================================================================================

splash_root=Tk()
width_of_window = 427
height_of_window = 250
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
splash_root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
splash_root.overrideredirect(1)

Frame(splash_root, width=427, height=250, bg='#242424').place(x=0,y=0)
label1=Label(splash_root, text='ATTENDANCE', fg='white', bg='#242424')
label1.configure(font=("Game Of Squids", 30 , "bold","italic"))
label1.place(x=50,y=90)

label2=Label(splash_root, text='Loading...', fg='white', bg='#242424')
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

# animation -----------------------------------------------------------------------------

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))

for i in range(1):
    # reverse----------------------------------------------------------------------
    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=0, y=85)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=85)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=85)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=85)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=85)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=85)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=85)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=85)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=85)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=85)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=85)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=85)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=85)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=85)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=85)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=85)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=85)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=85)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=85)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=85)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=85)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=85)
    splash_root.update_idletasks()
    time.sleep(0.070)
    # reverse end--------------------------------------------------------------------------



    # forward---------------------------------------------------------------------------
    l1=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=0, y=145)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=20, y=145)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=40, y=145)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=60, y=145)
    l5=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=80, y=145)
    l6=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=100, y=145)
    l7=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=145)
    l8=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=145)
    l9=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=145)
    l10=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l11=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l12=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l13=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l14=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l15=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    l16=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=300, y=145)
    l17=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=320, y=145)
    l18=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=340, y=145)
    l19=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=360, y=145)
    l20=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=380, y=145)
    l21=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=400, y=145)
    l22=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=420, y=145)
    splash_root.update_idletasks()
    time.sleep(0.070)
    # forward end-----------------------------------------------------------------------

# animation end -------------------------------------------------------------------------

# splash screen end ========================================================================================================================================================================


# login window =============================================================================================================================================================================
def main():
    splash_root.destroy()
    win = customtkinter.CTk()
    app=login_window(win)
    win.mainloop()



class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance")
        width_of_window = 500
        height_of_window = 460
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        self.root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

        self.var_username=customtkinter.StringVar()
        self.var_password=customtkinter.StringVar()

        self.bg=customtkinter.CTkImage(Image.open('pattern.png'),size=(1280,730))
        lbl_bg = customtkinter.CTkLabel(self.root,image=self.bg,text='')
        lbl_bg.pack()

        frame = customtkinter.CTkLabel(self.root, width = 320, height = 360, corner_radius = 15, text='')
        frame.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        header = customtkinter.CTkLabel(master = frame, text = 'Log into your Account ', font = ('Century Gothic',20))
        header.place(x = 50, y = 45)

        self.username_entry = customtkinter.CTkEntry(master = frame, width = 220, placeholder_text="Username")
        self.username_entry.place(x = 50, y = 110)

        self.pass_entry = customtkinter.CTkEntry(master = frame, width = 220, placeholder_text = "Password", show = '*')
        self.pass_entry.place(x = 50, y = 165)

        def visible():
            show_button.configure(command = hidden)
            self.pass_entry.configure(show = '')

        def hidden():
            show_button.configure(command = visible)
            self.pass_entry.configure(show = '*')

        show_button = customtkinter.CTkButton(master=frame,text='SHOW',font = ('Century Gothic',10), command = visible,cursor='hand2' ,width=20,height=10, fg_color="transparent",text_color="grey39")
        show_button.place(x = 270, y = 170)

        forgot_button = customtkinter.CTkButton (master=frame, text = "Forgot Password?", font =('Century Gothic',12), cursor='hand2',width=10,fg_color="transparent",text_color="grey39")
        forgot_button.place(x = 155, y = 195)

        # def button_function():
        #     self.root.destroy()
        #     import mainscreen

        login_button = customtkinter.CTkButton(master = frame, width = 220, text = 'Login', command =self.login, corner_radius = 30)
        login_button.place(x = 50, y = 240)


        google_img = customtkinter.CTkImage(Image.open("Google__G__Logo.svg.webp").resize((20,20), Image.Resampling.LANCZOS))
        facebook_img= customtkinter.CTkImage(Image.open("124010.png").resize((20,20), Image.Resampling.LANCZOS))

        google_button = customtkinter.CTkButton(master = frame, image = google_img, text = "Google", width = 100, height = 20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF' )
        google_button.place(x = 50, y = 290)

        facebook_button = customtkinter.CTkButton(master = frame, image = facebook_img, text = "Facebook", width = 100, height = 20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        facebook_button.place(x = 170, y = 290)

        signup_label = customtkinter.CTkLabel(master=frame, text= "Don't have an Account?", font =('Century Gothic',12))
        signup_label.place(x = 50, y = 320)

        # def signupcmd():
        #     self.root.destroy()
        #     import signup

        signup_button = customtkinter.CTkButton(master= frame, text = "Sign Up", font =('Century Gothic',12), cursor='hand2', command= self.signup_window,width=30,fg_color="transparent",text_color="grey39")
        signup_button.place(x = 200, y = 320)

    def signup_window(self):
        self.new_window=customtkinter.CTkToplevel(self.root)
        self.app= Signup(self.new_window)

    def login(self):
        if self.username_entry.get()=="" or self.pass_entry.get()=="":
            messagebox.showerror("Error","All Fields Are Required!")

        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from credentials where username=%s and password=%s",(
                                                                                            self.var_username.get(),
                                                                                            self.var_password.get()
                                                                                            ))

            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("","Continue?")
                if open_main>0:
                    self.new_window=customtkinter.CTkToplevel(self.root)
                    self.app = mainscreen(self.new_window)
                    # self.root.destroy()
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close

# login window end ====================================================================================================================================================================



# signup window ========================================================================================================================================================================

class Signup:
    def __init__(self1,root):
        self1.root=root
        width_of_window = 600
        height_of_window = 460
        screen_width = self1.root.winfo_screenwidth()
        screen_height = self1.root.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        self1.root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        self1.root.title('Attendance')

        self1.var_email=customtkinter.StringVar()
        self1.var_username=customtkinter.StringVar()
        self1.var_password=customtkinter.StringVar()
        self1.var_confpass=customtkinter.StringVar()


        self1.bg = customtkinter.CTkImage(Image.open("pattern2.png"),size=(1280,730))
        lbl_img = customtkinter.CTkLabel(master = self1.root, image = self1.bg, text='')
        lbl_img.pack()

        frame = customtkinter.CTkLabel(master = lbl_img, width = 320, height = 450, corner_radius = 15)
        frame.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        header = customtkinter.CTkLabel(master = frame, text = 'Create a new Account ', font = ('Century Gothic',20, 'bold'))
        header.place(x = 50, y = 45)

        email_lb = customtkinter.CTkLabel(master=frame, text='Email ID',font = ('Century Gothic',12, 'bold'))
        email_lb.place(x = 50 , y = 90)

        email_entry = customtkinter.CTkEntry(master = frame, width = 220,placeholder_text="Email ID", textvariable = self1.var_email)
        email_entry.place(x = 50, y = 110)

        username_lb = customtkinter.CTkLabel(master=frame, text='Username',font = ('Century Gothic',12, 'bold'))
        username_lb.place(x = 50 , y = 140)

        username_entry = customtkinter.CTkEntry(master = frame, width = 220, placeholder_text="Username", textvariable = self1.var_username)
        username_entry.place(x = 50, y = 160)

        pass1_lb = customtkinter.CTkLabel(master=frame, text='Password',font = ('Century Gothic',12, 'bold'))
        pass1_lb.place(x = 50 , y = 190)

        password1_entry = customtkinter.CTkEntry(master = frame, width = 220, placeholder_text="Password", textvariable = self1.var_password)
        password1_entry.place(x = 50, y = 210)

        pass2_lb = customtkinter.CTkLabel(master=frame, text='Confirm Password',font = ('Century Gothic',12, 'bold'))
        pass2_lb.place(x = 50 , y = 240)

        password2_entry = customtkinter.CTkEntry(master = frame, width = 220, placeholder_text="Confirm Password", textvariable = self1.var_confpass)
        password2_entry.place(x = 50, y = 260)

        register_button = customtkinter.CTkButton(master = frame, width = 220, text = 'Register', corner_radius = 30, command=self1.register_data)
        register_button.place(x = 50, y = 340)

        login_label = customtkinter.CTkLabel(master=frame, text= "Already have an Account?", font =('Century Gothic',12))
        login_label.place(x = 50, y = 380)

        def login_page():
            self1.root.destroy()


        login_button = customtkinter.CTkButton(master= frame, text = "Login", font =('Century Gothic',12), cursor='hand2', command= login_page, fg_color="transparent",text_color="grey39",width=20)
        login_button.place(x = 215, y = 380)

    def register_data(self1):

        if self1.var_username.get()=="" or self1.var_password.get()=="" or self1.var_email.get()=="" or self1.var_confpass.get()=="":
            messagebox.showerror("Error", "All Fields Are Required!")

        elif self1.var_password.get()!=self1.var_confpass.get():
            messagebox.showerror("Error","Both Passwords Should Match!")

        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
            my_cursor=conn.cursor()
            query = ("select * from credentials where email=%s")
            value =(self1.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User With This Email ID Already Exists!")
            else:
                my_cursor.execute("insert into credentials values(%s,%s,%s,%s)",(
                                                                                self1.var_email.get(),
                                                                                self1.var_username.get(),
                                                                                self1.var_password.get(),
                                                                                self1.var_confpass.get()
                                                                                ))

            conn.commit()
            conn.close()
        messagebox.showinfo("Registered","Successfully Registered")

# signup window end ====================================================================================================================================================================================



# mainscreen window =================================================================================================================================================================================

class mainscreen:
    def __init__(self,win):
        # win = customtkinter.CTk()
        win.title("Attendance")
        win.geometry(f"{1100}x{580}")

        win.iconbitmap("icon.ico")


        # configure grid layout (4x4)
        win.grid_columnconfigure(1, weight=1)
        win.grid_columnconfigure((2, 3), weight=0)
        win.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        win.sidebar_frame = customtkinter.CTkFrame(win, width=140, corner_radius=0)
        win.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        win.sidebar_frame.grid_rowconfigure(7, weight=1)
        win.logo_label = customtkinter.CTkLabel(win.sidebar_frame, text="Attendance Manager", font=('Century Gothic',25, "bold"))
        win.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # 1st button-------------------------------------------------------------------------------------------------------------------
        def bscit_button():
            win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='Please Select A Year For B.Sc.IT',font=('Century Gothic',30))
            win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

            #radiobutton frame---------------------------------------------------------------------------------------------------------
            win.right_frame = customtkinter.CTkFrame(win)
            win.right_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

            win.radiobutton_frame = customtkinter.CTkFrame(win.right_frame)
            win.radiobutton_frame.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")

            win.radio_var = customtkinter.IntVar(value=0)

            win.rf_radio_group = customtkinter.CTkLabel(master=win.radiobutton_frame, text="Select Year:",font=('Century Gothic',20,'bold'))
            win.rf_radio_group.grid(row=0 , column=3, padx=20, pady=20, sticky="nsew")

            def bscit_1yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR BSCIT 1ST YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")

                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into bscit1yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BSCIT" and students.ACADEMICYEAR = "FY"
                                     and students.ROLLNO NOT IN (select ROLLNO from bscit1yr)
                                     """)

                my_cursor.execute("select * from bscit1yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_1yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='1st Year',variable=win.radio_var, value=0, command=bscit_1yr)
            win.button_1yr.grid(row=1, column=3, padx=20,pady=20, sticky="nsew")

            def bscit_2yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR BSCIT 2ND YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into bscit2yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BSCIT" and students.ACADEMICYEAR = "SY"
                                     and students.ROLLNO NOT IN (select ROLLNO from bscit2yr)
                                     """)

                my_cursor.execute("select * from bscit2yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_2yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='2nd Year',variable=win.radio_var, value=1, command=bscit_2yr)
            win.button_2yr.grid(row=2, column=3, padx=20,pady=20, sticky="nsew")

            def bscit_3yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR BSCIT 3RD YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into bscit3yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BSCIT" and students.ACADEMICYEAR = "TY"
                                     and students.ROLLNO NOT IN (select ROLLNO from bscit3yr)
                                     """)

                my_cursor.execute("select * from bscit3yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_3yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='3rd Year',variable=win.radio_var, value=2, command=bscit_3yr)
            win.button_3yr.grid(row=3, column=3, padx=20,pady=20, sticky="nsew")
            #radiobutton frame end-----------------------------------------------------------------------------------------------------

        win.sidebar_button_1 = customtkinter.CTkButton(win.sidebar_frame,text='B.Sc.IT',height=40, command=bscit_button)
        win.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        # 1st button end----------------------------------------------------------------------------------------------------------------






        # 2nd button--------------------------------------------------------------------------------------------------------------------
        def baf_button():
            win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='Please Select A Year For B.A.F',font=('Century Gothic',30))
            win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

            #radiobutton frame----------------------------------------------------------------------------------------------------------
            win.right_frame = customtkinter.CTkFrame(win)
            win.right_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

            win.radiobutton_frame = customtkinter.CTkFrame(win.right_frame)
            win.radiobutton_frame.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")

            win.radio_var = customtkinter.IntVar(value=0)

            win.rf_radio_group = customtkinter.CTkLabel(master=win.radiobutton_frame, text="Select Year:",font=('Century Gothic',20,'bold'))
            win.rf_radio_group.grid(row=0 , column=3, padx=20, pady=20, sticky="nsew")

            def baf_1yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.A.F 1ST YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into baf1yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BAF" and students.ACADEMICYEAR = "FY"
                                     and students.ROLLNO NOT IN (select ROLLNO from baf1yr)
                                     """)

                my_cursor.execute("select * from baf1yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_1yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='1st Year',variable=win.radio_var, value=0, command=baf_1yr)
            win.button_1yr.grid(row=1, column=3, padx=20,pady=20, sticky="nsew")

            def baf_2yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.A.F 2ND YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into baf2yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BAF" and students.ACADEMICYEAR = "SY"
                                     and students.ROLLNO NOT IN (select ROLLNO from baf2yr)
                                     """)

                my_cursor.execute("select * from baf2yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_2yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='2nd Year',variable=win.radio_var, value=1, command=baf_2yr)
            win.button_2yr.grid(row=2, column=3, padx=20,pady=20, sticky="nsew")

            def baf_3yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.A.F 3RD YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into baf3yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BAF" and students.ACADEMICYEAR = "TY"
                                     and students.ROLLNO NOT IN (select ROLLNO from baf3yr)
                                     """)

                my_cursor.execute("select * from baf3yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_3yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='3rd Year',variable=win.radio_var, value=2, command=baf_3yr)
            win.button_3yr.grid(row=3, column=3, padx=20,pady=20, sticky="nsew")
            #radiobutton frame end-----------------------------------------------------------------------------------------------------

        win.sidebar_button_2 = customtkinter.CTkButton(win.sidebar_frame,text='B.A.F',height=40, command=baf_button)
        win.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        # 2nd button end----------------------------------------------------------------------------------------------------------------






        # 3rd button--------------------------------------------------------------------------------------------------------------------
        def bmm_button():
            win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='Please Select A Year For B.M.M',font=('Century Gothic',30))
            win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

            #radiobutton frame---------------------------------------------------------------------------------------------------------
            win.right_frame = customtkinter.CTkFrame(win)
            win.right_frame.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")

            win.radiobutton_frame = customtkinter.CTkFrame(win.right_frame)
            win.radiobutton_frame.grid(row=0, column=3, padx=(15, 15), pady=(15, 15), sticky="nsew")

            win.radio_var = customtkinter.IntVar(value=0)

            win.rf_radio_group = customtkinter.CTkLabel(master=win.radiobutton_frame, text="Select Year:",font=('Century Gothic',20,'bold'))
            win.rf_radio_group.grid(row=0 , column=3, padx=20, pady=20, sticky="nsew")

            def bmm_1yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.M.M 1ST YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into bmm1yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BMM" and students.ACADEMICYEAR = "FY"
                                     and students.ROLLNO NOT IN (select ROLLNO from bmm1yr)
                                     """)

                my_cursor.execute("select * from bmm1yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_1yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='1st Year',variable=win.radio_var, value=0, command=bmm_1yr)
            win.button_1yr.grid(row=1, column=3, padx=20,pady=20, sticky="nsew")

            def bmm_2yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.M.M 2ND YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into bmm2yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BMM" and students.ACADEMICYEAR = "SY"
                                     and students.ROLLNO NOT IN (select ROLLNO from bmm2yr)
                                     """)

                my_cursor.execute("select * from bmm2yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_2yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='2nd Year',variable=win.radio_var, value=1, command=bmm_2yr)
            win.button_2yr.grid(row=2, column=3, padx=20,pady=20, sticky="nsew")

            def bmm_3yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.M.M 3RD YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into bmm3yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BMM" and students.ACADEMICYEAR = "TY"
                                     and students.ROLLNO NOT IN (select ROLLNO from bmm3yr)
                                     """)

                my_cursor.execute("select * from bmm3yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_3yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='3rd Year',variable=win.radio_var, value=2, command=bmm_3yr)
            win.button_3yr.grid(row=3, column=3, padx=20,pady=20, sticky="nsew")
            #radiobutton frame end-----------------------------------------------------------------------------------------------------

        win.sidebar_button_3 = customtkinter.CTkButton(win.sidebar_frame,text='B.M.M',height=40, command=bmm_button)
        win.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        # 3rd button end----------------------------------------------------------------------------------------------------------------






        # 4th button--------------------------------------------------------------------------------------------------------------------
        def bms_button():
            win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='Please Select A Year For B.M.S',font=('Century Gothic',30))
            win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

            #radiobutton frame---------------------------------------------------------------------------------------------------------
            win.right_frame = customtkinter.CTkFrame(win)
            win.right_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

            win.radiobutton_frame = customtkinter.CTkFrame(win.right_frame)
            win.radiobutton_frame.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")

            win.radio_var = customtkinter.IntVar(value=0)

            win.rf_radio_group = customtkinter.CTkLabel(master=win.radiobutton_frame, text="Select Year:",font=('Century Gothic',20,'bold'))
            win.rf_radio_group.grid(row=0 , column=3, padx=20, pady=20, sticky="nsew")

            def bms_1yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.M.S 1ST YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into bms1yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BMS" and students.ACADEMICYEAR = "FY"
                                     and students.ROLLNO NOT IN (select ROLLNO from bms1yr)
                                     """)

                my_cursor.execute("select * from bms1yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_1yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='1st Year',variable=win.radio_var, value=0, command=bms_1yr)
            win.button_1yr.grid(row=1, column=3, padx=20,pady=20, sticky="nsew")

            def bms_2yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.M.M 2ND YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into bms2yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BMS" and students.ACADEMICYEAR = "SY"
                                     and students.ROLLNO NOT IN (select ROLLNO from bms2yr)
                                     """)

                my_cursor.execute("select * from bms2yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_2yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='2nd Year',variable=win.radio_var, value=1, command=bms_2yr)
            win.button_2yr.grid(row=2, column=3, padx=20,pady=20, sticky="nsew")

            def bms_3yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.M.M 3RD YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into bms3yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BMS" and students.ACADEMICYEAR = "TY"
                                     and students.ROLLNO NOT IN (select ROLLNO from bms3yr)
                                     """)

                my_cursor.execute("select * from bms3yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_3yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='3rd Year',variable=win.radio_var, value=2, command=bms_3yr)
            win.button_3yr.grid(row=3, column=3, padx=20,pady=20, sticky="nsew")
            #radiobutton frame end-----------------------------------------------------------------------------------------------------

        win.sidebar_button_4 = customtkinter.CTkButton(win.sidebar_frame,text='B.M.S',height=40, command=bms_button )
        win.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        # 4th button end----------------------------------------------------------------------------------------------------------------






        # 5th button--------------------------------------------------------------------------------------------------------------------
        def ba_button():
            win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='Please Select A Year For B.A',font=('Century Gothic',30))
            win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

            #radiobutton frame----------------------------------------------------------------------------------------------------------
            win.right_frame = customtkinter.CTkFrame(win)
            win.right_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

            win.radiobutton_frame = customtkinter.CTkFrame(win.right_frame)
            win.radiobutton_frame.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")

            win.radio_var = customtkinter.IntVar(value=0)

            win.rf_radio_group = customtkinter.CTkLabel(master=win.radiobutton_frame, text="Select Year:",font=('Century Gothic',20,'bold'))
            win.rf_radio_group.grid(row=0 , column=3, padx=20, pady=20, sticky="nsew")

            def ba_1yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.A 1ST YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into ba1yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BA" and students.ACADEMICYEAR = "FY"
                                     and students.ROLLNO NOT IN (select ROLLNO from ba1yr)
                                     """)

                my_cursor.execute("select * from ba1yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_1yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='1st Year',variable=win.radio_var, value=0, command=ba_1yr)
            win.button_1yr.grid(row=1, column=3, padx=20,pady=20, sticky="nsew")

            def ba_2yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.A 2ND YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into ba2yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BA" and students.ACADEMICYEAR = "SY"
                                     and students.ROLLNO NOT IN (select ROLLNO from ba2yr)
                                     """)

                my_cursor.execute("select * from ba2yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_2yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='2nd Year',variable=win.radio_var, value=1, command=ba_2yr)
            win.button_2yr.grid(row=2, column=3, padx=20,pady=20, sticky="nsew")

            def ba_3yr():
                win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='RECORDS FOR B.A 3RD YEAR',font=('Century Gothic',30))
                win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                win.rightsearch = customtkinter.CTkEntry(win.right_frame, placeholder_text='Search by Student Name')
                win.rightsearch.grid(row=1,column=3,padx=(15,5), pady=(15,5), sticky="nsew")

                win.searchbutton = customtkinter.CTkButton(win.right_frame, text="Search")
                win.searchbutton.grid(row=2, column=3,padx=(15,15),pady=(5,30),sticky="nsew")


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview",
                             background = "white",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "white")

                style.map ('Treeview',
                           background = [('selected',"#347083")])

                # Tree_frame = Frame(win.centerframe)
                # Tree_frame.grid(row=0,column=1,pady = 10)

                Tree_scroll = Scrollbar(win.centerframe)
                Tree_scroll.grid(row=0,column=0)

                my_tree = ttk.Treeview(win.centerframe, yscrollcommand = Tree_scroll.set, selectmode="extended")
                my_tree.grid(row=0,column=0, sticky = "nswe", padx = 0, pady = 0)

                Tree_scroll.configure(command=my_tree.yview)

                my_tree['columns'] = ("Roll No", "Student Name", "Date", "Time")

                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Roll No", anchor=W, width=100)
                my_tree.column("Student Name", anchor=W, width=140)
                # my_tree.column("Attendance", anchor=CENTER, width=140)
                my_tree.column("Date", anchor=CENTER, width=140)
                my_tree.column("Time", anchor=CENTER, width=140)

                style.configure("Treeview.Heading", font=('Century Gothic', 20))

                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Roll No", text="Roll No", anchor=W)
                my_tree.heading("Student Name", text="Student Name", anchor=W)
                # my_tree.heading("Attendance", text="Attendance", anchor=CENTER)
                my_tree.heading("Time", text="Date", anchor=CENTER)
                my_tree.heading("Date", text="Time", anchor=CENTER)


                my_tree.tag_configure("oddrow", background="white")
                my_tree.tag_configure("evenrow", background="lightblue")

                conn=mysql.connector.connect(host='localhost',user='root',password='',database='attendance')
                my_cursor=conn.cursor()

                my_cursor.execute("""
                                     insert ignore into ba3yr
                                     select students.ROLLNO, students.SNAME, detected.TIMING, detected.RDATE
                                     from detected
                                     inner join students on detected.SNAME = students.SNAME
                                     where students.DEPARTMENT = "BA" and students.ACADEMICYEAR = "TY"
                                     and students.ROLLNO NOT IN (select ROLLNO from ba3yr)
                                     """)

                my_cursor.execute("select * from ba3yr")

                records = my_cursor.fetchall()

                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("evenrow",))
                    else:
                        my_tree.insert(parent='', index = 'end', iid=count, text="",values=(record[0],record[1],record[2],record[3]), tags=("oddrow",))

                    count += 1

                conn.commit()
                conn.close()

            win.button_3yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='3rd Year',variable=win.radio_var, value=2, command=ba_3yr)
            win.button_3yr.grid(row=3, column=3, padx=20,pady=20, sticky="nsew")
            #radiobutton frame end-----------------------------------------------------------------------------------------------------

        win.sidebar_button_5 = customtkinter.CTkButton(win.sidebar_frame,text='B.A',height=40, command=ba_button)
        win.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        # 5th button end----------------------------------------------------------------------------------------------------------------

        def sidebar_accbutton_event():
            win.destroy()


        logout_img = customtkinter.CTkImage(Image.open("logout.png").resize((20,20), Image.Resampling.LANCZOS))
        win.account_button = customtkinter.CTkButton(win.sidebar_frame, text='Log Out', image= logout_img, compound='left',height=40,command=sidebar_accbutton_event)
        win.account_button.grid(row=6, column=0, padx=20, pady=30)


        win.appearance_mode_label = customtkinter.CTkLabel(win.sidebar_frame, text="Appearance Mode:")
        win.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        def change_appearance_mode_event(new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)

        win.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(win.sidebar_frame, values=["Light", "Dark", "System"], command=change_appearance_mode_event)
        win.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

        win.appearance_mode_optionemenu.set("Dark")

        win.fix_label = customtkinter.CTkLabel(win.sidebar_frame, text="", anchor="w")
        win.fix_label.grid(row=9, column=0, padx=20, pady=(10, 0))


        # create textbox
        win.centerframe = customtkinter.CTkLabel(win, width=250,height=550,fg_color='white',corner_radius=7,text='Select A Course',font=('Century Gothic',30,'bold'))
        win.centerframe.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create radiobutton frame
        win.right_frame = customtkinter.CTkFrame(win)
        win.right_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # win.radiobutton_frame = customtkinter.CTkFrame(win.right_frame)
        # win.radiobutton_frame.grid(row=0, column=3, padx=(15, 15), pady=(15, 15), sticky="nsew")

        # win.radio_var = customtkinter.IntVar(value=0)

        # win.rf_radio_group = customtkinter.CTkLabel(master=win.radiobutton_frame, text="Select Year:",font=('Century Gothic',20,'bold'))
        # win.rf_radio_group.grid(row=0 , column=3, padx=20, pady=20, sticky="nsew")

        # win.button_1yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='1st Year',variable=win.radio_var, value=0)
        # win.button_1yr.grid(row=1, column=3, padx=20,pady=20, sticky="nsew")

        # win.button_2yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='2nd Year',variable=win.radio_var, value=1)
        # win.button_2yr.grid(row=2, column=3, padx=20,pady=20, sticky="nsew")

        # win.button_3yr = customtkinter.CTkRadioButton(win.radiobutton_frame, text='3rd Year',variable=win.radio_var, value=2)
        # win.button_3yr.grid(row=3, column=3, padx=20,pady=20, sticky="nsew")

# mainscreen window end ====================================================================================================================================================================


if __name__ == "__main__":
    main()
