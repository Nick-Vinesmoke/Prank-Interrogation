from tkinter import *
import customtkinter as ct
import random as r


def WinProperties(win):
    win.geometry("600x300+540+240")
    win.title("Are you dumb?")  # win title
    win.resizable(False, False)  
    win.iconbitmap('1.ico')  # win icon

def Da():
    global button1
    global button
    global text
    global win
    button1.destroy()
    button.destroy()
    text.destroy()
    text = ct.CTkLabel(master=win, text='I knew it!!!', font=('Arial Rounded MT Bold', 64), text_color='#B4B6B9')
    text.place(relx=0.5, rely=0.5, anchor=CENTER)
    win.after(3000, win.destroy)


def fun(e):
    global button1
    x = r.uniform(0.15,0.85)
    y = r.uniform(0.15, 0.85)
    button1.place(relx=x, rely=y, anchor=CENTER)


win = ct.CTk()
def Quit():
    pass
win.protocol("WM_DELETE_WINDOW", Quit)
ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')
WinProperties(win)

text = ct.CTkLabel(master=win, text='Are you dumb?', font=('Arial Rounded MT Bold', 32), text_color='#B4B6B9')# in text input your quastion
button = ct.CTkButton(master=win, text='Yes', font=('Arial Rounded MT Bold', 18), text_color='#B4B6B9',command=Da)
button1 = ct.CTkButton(master=win, text='No', font=('Arial Rounded MT Bold', 18), text_color='#B4B6B9')
button1.bind("<Enter>", fun)
text.place(relx=0.5, rely=0.1, anchor=CENTER)
button.place(relx=0.3, rely=0.5, anchor=CENTER)
button1.place(relx=0.7, rely=0.5, anchor=CENTER)


win.mainloop()