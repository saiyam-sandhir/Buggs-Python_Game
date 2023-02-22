import customtkinter as ctk
import random
import tkinter.font as tkFont
from PIL import Image

import baseframe
import audioobjects as audio

class RestartButton(ctk.CTkButton):
    def __init__(self, master):
        restartbutton_img_enter = ctk.CTkImage(light_image=Image.open(".\\images\\restartbutton_img_enter.png"), dark_image=Image.open(".\\images\\restartbutton_img_enter.png"), size=(185, 185))
        restartbutton_img_leave = ctk.CTkImage(light_image=Image.open(".\\images\\restartbutton_img_leave.png"), dark_image=Image.open(".\\images\\restartbutton_img_leave.png"), size=(185, 185))

        super().__init__(master=master, text="", image=restartbutton_img_leave, height=175, width=175, hover=False, bg_color="transparent", fg_color="transparent", corner_radius=20, command=self.restart_game)

        self.master = master

        self.bind("<Enter>", lambda e: self.configure(image=restartbutton_img_enter))
        self.bind("<Leave>", lambda e: self.configure(image=restartbutton_img_leave))

    def restart_game(self):
        audio.on_click.play(0)
        self.winfo_toplevel().game_menu.game_window.player.goto(random.randint(-147, 361), random.randint(-480, 55))
        self.master.hide()
        self.winfo_toplevel().game_menu.start_updating()

class Frame(baseframe.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.header = ctk.CTkLabel(self, text="Game Over", height=125, width=master.winfo_width() - 2 * self.cget("border_width"), fg_color="transparent", bg_color="transparent", text_color="brown", font=("Sareif", 100))
        self.header.pack(side=ctk.LEFT, fill=ctk.X, anchor=ctk.N, padx=10, pady=10)

        restart_button = RestartButton(self)
        restart_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)