# import modules
import os
from tkinter import *

# improved rendering
import ctypes
from ctypes import windll

# importing custom
import customtkinter

# Other thing's
ctypes.windll.shcore.SetProcessDpiAwareness(True)
h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)
windll.user32.ShowWindow(h, 0)

# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.title("Account Login")
    main_screen.resizable(width=False, height=False)
    main_screen.iconbitmap('icons/panel-top-inactive.ico')

    ws = main_screen.winfo_screenwidth()  # width of the screen
    hs = main_screen.winfo_screenheight()  # height of the screen

    w = 350  # width for the Tk root
    h = 250  # height for the Tk root

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    main_screen.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Label(text="Select Your Choice", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    customtkinter.CTkButton(main_screen,
                            text="Login",
                            text_color="#1B1B1B",
                            height=40, width=200,
                            corner_radius=50,
                            hover_color="#D7D7D7",
                            fg_color="#E4E3E2",

    command=login).pack()
    Label(text="").pack()
    customtkinter.CTkButton(main_screen,
                            text="Register",
                            text_color="#1B1B1B",
                            height=40, width=200,
                            corner_radius=50,
                            hover_color="#D7D7D7",
                            fg_color="#E4E3E2",
    command=register).pack()

    main_screen.mainloop()


main_account_screen()
