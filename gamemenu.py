import customtkinter as ctk
import tkinter as tk
import turtle
from PIL import Image

import baseframe

class TurtleWindow(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, background="#eddbc7", highlightthickness=0)

        screen = turtle.TurtleScreen(self)
        screen.bgcolor("#eddbc7")#eddbc7

class PauseButton(ctk.CTkButton):
    def __init__(self, master):
        pausebutton_img_enter = ctk.CTkImage(light_image=Image.open(".\\images\\pausebutton_img_enter.png"), dark_image=Image.open(".\\images\\pausebutton_img_enter.png"), size=(50, 50))
        pausebutton_img_leave = ctk.CTkImage(light_image=Image.open(".\\images\\pausebutton_img_leave.png"), dark_image=Image.open(".\\images\\pausebutton_img_leave.png"), size=(50, 50))

        super().__init__(master=master, text="", height=55, width=55, hover=False, image=pausebutton_img_leave, bg_color="transparent", fg_color="transparent", command=self.pause_game)

        self.bind("<Enter>", lambda e: self.configure(image=pausebutton_img_enter))
        self.bind("<Leave>", lambda e: self.configure(image=pausebutton_img_leave))

    def pause_game(self):
        self.winfo_toplevel().game_menu.stop_updating()
        self.winfo_toplevel().game_menu.hide()
        self.winfo_toplevel().pause_menu.show()

class ScoreBoard(ctk.CTkFrame):
    def __init__(self, master):
        self.score = 0
        self.high_score = 0

        super().__init__(master=master, corner_radius=30, bg_color="transparent", fg_color="transparent")

        curr_score = ctk.CTkLabel(self, text=f"Current Score: {self.score}", bg_color="transparent", fg_color="transparent", text_color="brown", font=("Freehand521 BT", 20, "bold"))
        curr_score.pack(fill=tk.BOTH, expand=True)

        high_score = ctk.CTkLabel(self, text=f"High Score: {self.score}", bg_color="transparent", fg_color="transparent", text_color="brown", font=("Freehand521 BT", 20, "bold"))
        high_score.pack(fill=tk.BOTH, expand=True)

class Frame(baseframe.Frame):
    def __init__(self, master):
        super().__init__(master)

        game_window = TurtleWindow(self)
        game_window.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=30)

        self.pause_button = PauseButton(self)
        self.pause_button.place(relx=0.075, rely=0.065, anchor=tk.CENTER)

        score_board = ScoreBoard(self)
        score_board.place(relx=0.5, rely=0.065, anchor=tk.CENTER)

    def update_frame(self):
        if self.keep_updating:
            self.winfo_toplevel().after(50, self.update_frame)

    def start_updating(self):
        self.keep_updating = True
        self.update_frame()

    def stop_updating(self):
        self.keep_updating = False
