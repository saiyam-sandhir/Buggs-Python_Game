# Copyright (c) 2023 Saiyam Jain

import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkFont
import math
from PIL import Image
import webbrowser

import baseframe
import audioobjects as audio
from settingswindow import SettingsWindow

class LevitatingLabel(ctk.CTkFrame):
    def __init__(self, master: baseframe.Frame, text: str, height: float, width: float, fg_color: str, bg_color: str, text_color: str, font: tuple, frequency: float):
        self.x = 0
        self.OFFSET = (((tkFont.Font(font=font).actual()["size"]) / 2) / height)
        self.FREQUENCY = frequency

        super().__init__(master=master, height=height, width=width, fg_color=fg_color, bg_color=bg_color)

        self.header_label = ctk.CTkLabel(self, text=text, fg_color=fg_color, bg_color=bg_color, text_color=text_color, font=font)

    def levitate_label(self):
        y = (((math.sin(self.x) + 1) / 2) * (1 - (2 * self.OFFSET)) + self.OFFSET)
        self.header_label.place(relx=0.5, rely=y, anchor=ctk.CENTER)
        self.x += ((2 * math.pi * self.FREQUENCY) / 1000)

class PlayButton(ctk.CTkButton):
    def __init__(self, master):
        playbutton_img_enter = ctk.CTkImage(light_image=Image.open(".\\images\\playbutton_img.png"), dark_image=Image.open(".\\images\\playbutton_img.png"), size=(185, 185))
        playbutton_img_leave = ctk.CTkImage(light_image=Image.open(".\\images\\playbutton_img.png"), dark_image=Image.open(".\\images\\playbutton_img.png"), size=(165, 165))

        super().__init__(master=master, text="", image=playbutton_img_leave, height=175, width=175, hover=False, bg_color="transparent", fg_color="transparent", corner_radius=20, command=lambda: [self.start_game(), audio.on_click.play(0)])

        self.bind("<Enter>", lambda e: self.configure(height=195, width=195, image=playbutton_img_enter))
        self.bind("<Leave>", lambda e: self.configure(height=175, width=175, image=playbutton_img_leave))
        self.winfo_toplevel().bind("<Return>", lambda e: self.start_game())

    def start_game(self):
        self.winfo_toplevel().main_menu.stop_updating()
        self.winfo_toplevel().game_menu.start_updating()
        self.winfo_toplevel().main_menu.hide()
        self.winfo_toplevel().game_menu.show()
        self.winfo_toplevel().bind("<Escape>", lambda e: self.winfo_toplevel().game_menu.pause_button.pause_game())
        self.winfo_toplevel().unbind("<Return>")

class QuitButton(ctk.CTkButton):
    def __init__(self, master):
        exitbutton_img_enter = ctk.CTkImage(light_image=Image.open(".\\images\\exitbutton_img.png"), dark_image=Image.open(".\\images\\exitbutton_img.png"), size=(70, 70))
        exitbutton_img_leave = ctk.CTkImage(light_image=Image.open(".\\images\\exitbutton_img.png"), dark_image=Image.open(".\\images\\exitbutton_img.png"), size=(50, 50))

        super().__init__(master=master, text="", height=80, width=80, hover=False, image=exitbutton_img_leave, bg_color="transparent", fg_color="transparent", corner_radius=20, command=lambda: [audio.on_click.play(0), self.quit_game()])

        self.bind("<Enter>", lambda e: self.configure(image=exitbutton_img_enter))
        self.bind("<Leave>", lambda e: self.configure(image=exitbutton_img_leave))
        self.winfo_toplevel().bind("<Escape>", lambda e: self.quit_game())

    def quit_game(self):
        if tk.messagebox.askyesno("Quit", "Are you sure you want to exit the game?", default="no"):
            self.winfo_toplevel().destroy()

class AboutButton(ctk.CTkButton):
    def __init__(self, master):
        aboutbutton_img_enter = ctk.CTkImage(light_image=Image.open(".\\images\\aboutbutton_img.png"), dark_image=Image.open(".\\images\\aboutbutton_img.png"), size=(50, 50))
        aboutbutton_img_leave = ctk.CTkImage(light_image=Image.open(".\\images\\aboutbutton_img.png"), dark_image=Image.open(".\\images\\aboutbutton_img.png"), size=(45, 45))

        super().__init__(master=master, text="", height=55, width=55, hover=False, image=aboutbutton_img_leave, bg_color="transparent", fg_color="transparent", command=lambda: [webbrowser.open("https://github.com/saiyam-sandhir/Disc_Dash-Game"), audio.on_click.play(0)])

        self.bind("<Enter>", lambda e: self.configure(image=aboutbutton_img_enter))
        self.bind("<Leave>", lambda e: self.configure(image=aboutbutton_img_leave))

class SettingsButton(ctk.CTkButton):
    def __init__(self, master):
        settingsbutton_img_enter = ctk.CTkImage(light_image=Image.open(".\\images\\settingsbutton_img.png"), dark_image=Image.open(".\\images\\settingsbutton_img.png"), size=(50, 50))
        settingsbutton_img_leave = ctk.CTkImage(light_image=Image.open(".\\images\\settingsbutton_img.png"), dark_image=Image.open(".\\images\\settingsbutton_img.png"), size=(45, 45))

        super().__init__(master=master, text="", height=55, width=55, hover=False, image=settingsbutton_img_leave, bg_color="transparent", fg_color="transparent", command=lambda: [audio.on_click.play(0), SettingsWindow(master=self.winfo_toplevel())])

        self.bind("<Enter>", lambda e: self.configure(image=settingsbutton_img_enter))
        self.bind("<Leave>", lambda e: self.configure(image=settingsbutton_img_leave))

class Frame(baseframe.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.header = LevitatingLabel(master=self, text="BUGGS", height=125, width=master.winfo_width() - 2 * self.cget("border_width"), fg_color="transparent", bg_color="transparent", text_color="brown", font=("Freehand521 BT", 115), frequency=1.25)
        self.header.place(relx=0.5, y=((self.header.cget("height") / 2) + self.cget("corner_radius")), anchor=ctk.CENTER)

        play_button = PlayButton(self)
        play_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        quit_button = QuitButton(self)
        quit_button.place(relx=0.51, rely=0.7, anchor=ctk.CENTER)

        about_button = AboutButton(self)
        about_button.place(relx=0.075, rely=0.925, anchor=ctk.CENTER)

        settings_button = SettingsButton(self)
        settings_button.place(relx=0.925, rely=0.925, anchor=ctk.CENTER)

        self.start_updating()

    def update_frame(self):
        if self.keep_updating:
            self.header.levitate_label()
            
            self.winfo_toplevel().after(1, self.update_frame)

    def start_updating(self):
        self.keep_updating = True
        self.update_frame()

    def stop_updating(self):
        self.keep_updating = False