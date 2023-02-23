import customtkinter as ctk
import tkinter as tk
import webbrowser

import baseframe
import audioobjects as audio
from settingswindow import SettingsWindow

class BaseButton(ctk.CTkButton):
    def __init__(self, master, text, command):
        super().__init__(master=master, text=text, fg_color="transparent", text_color="brown", font=("Freehand521 BT", 90), hover=False, corner_radius=0, command=command)

        self.bind("<Enter>", lambda e: self.configure(text_color=master.cget("fg_color"), fg_color="brown"))
        self.bind("<Leave>", lambda e: self.configure(text_color="brown", fg_color="transparent"))

class ResumeButton(BaseButton):
    def __init__(self, master):
        super().__init__(master=master, text="Resume", command=lambda: [self.resume_game(), audio.on_click.play(0)])

    def resume_game(self):
        self.winfo_toplevel().pause_menu.hide()
        self.winfo_toplevel().game_menu.show()
        self.winfo_toplevel().game_menu.start_updating()

class SettingsButton(BaseButton):
    def __init__(self, master):
        super().__init__(master=master, text="Settings", command=lambda: [audio.on_click.play(0), SettingsWindow(master=self.winfo_toplevel())])

class AboutButton(BaseButton):
    def __init__(self, master):
        super().__init__(master=master, text="About", command=lambda: [webbrowser.open("https://github.com/saiyam-sandhir/Disc_Dash-Game"), audio.on_click.play(0)])

class QuitButton(BaseButton):
    def __init__(self, master):
        super().__init__(master=master, text="Quit", command=lambda: [audio.on_click.play(0), self.quit_game()])

    def quit_game(self):
        if tk.messagebox.askyesno("Quit", "Are you sure you want to exit the game?", default="no"):
            self.winfo_toplevel().destroy()

class Frame(baseframe.Frame):
    def __init__(self, master):
        super().__init__(master)

        BORDER_WIDTH = self.cget("border_width")

        header = ctk.CTkLabel(self, text="Paused", height=120, width=(((self.winfo_toplevel().winfo_width() - 2 * BORDER_WIDTH) / 2) + 20), bg_color="transparent", fg_color="brown", text_color="#eddbc7", font=("Freehand521 BT", 90), corner_radius=30)
        header.pack(pady=BORDER_WIDTH)

        resume_button = ResumeButton(self)
        resume_button.pack(fill=ctk.X, padx=BORDER_WIDTH, pady=4)

        settings_button = SettingsButton(self)
        settings_button.pack(fill=ctk.X, padx=BORDER_WIDTH, pady=4)

        about_button = AboutButton(self)
        about_button.pack(fill=ctk.X, padx=BORDER_WIDTH, pady=4)

        quit_button = QuitButton(self)
        quit_button.pack(fill=ctk.X, padx=BORDER_WIDTH, pady=4)
