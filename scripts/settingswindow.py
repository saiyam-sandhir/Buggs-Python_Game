# Copyright (c) 2023 Saiyam Jain

from tkinter import Toplevel
import customtkinter as ctk
from PIL import Image
import pygame
import configparser

import audioobjects as audio

class MusicVolumeControlLabel(ctk.CTkLabel):
    def __init__(self, master, color):
        self.musiclabel_on_img = ctk.CTkImage(light_image=Image.open(".\\images\\music_on_img.png"), dark_image=Image.open(".\\images\\music_on_img.png"), size=(50, 50))
        self.musiclabel_off_img = ctk.CTkImage(light_image=Image.open(".\\images\\music_off_img.png"), dark_image=Image.open(".\\images\\music_off_img.png"), size=(50, 50))

        super().__init__(master=master, text="", image=self.musiclabel_on_img, bg_color=color, fg_color=color, anchor=ctk.CENTER)

class MusicVolumeControlSlider(ctk.CTkSlider):
    def __init__(self, master):
        super().__init__(master=master, from_=0, to=100, height=30, command=self.change_volume)

        self.set(audio.bg_music.get_volume()*100)

    def change_volume(self, volume):
        audio.bg_music.set_volume(volume/100)

        if volume == 0:
            music_vol_ctrl_label = self.winfo_toplevel().music_vol_ctrl_label
            music_vol_ctrl_label.configure(image=music_vol_ctrl_label.musiclabel_off_img)

        else:
            music_vol_ctrl_label = self.winfo_toplevel().music_vol_ctrl_label
            music_vol_ctrl_label.configure(image=music_vol_ctrl_label.musiclabel_on_img)

class SoundVolumeControlLabel(ctk.CTkLabel):
    def __init__(self, master, color):
        self.soundlabel_on_img = ctk.CTkImage(light_image=Image.open(".\\images\\sound_on_img.png"), dark_image=Image.open(".\\images\\sound_on_img.png"), size=(50, 50))
        self.soundlabel_off_img = ctk.CTkImage(light_image=Image.open(".\\images\\sound_off_img.png"), dark_image=Image.open(".\\images\\sound_off_img.png"), size=(50,50))

        super().__init__(master=master, text="", image=self.soundlabel_on_img, bg_color=color, fg_color=color, anchor=ctk.CENTER)

class SoundVolumeControlSlider(ctk.CTkSlider):
    def __init__(self, master):
        super().__init__(master=master, from_=0, to=100, height=30, command=self.change_volume)

        self.set(audio.on_click.get_volume()*100)

    def change_volume(self, volume):
        audio.on_click.set_volume(volume/100)

        if volume == 0:
            sound_vol_ctrl_label = self.winfo_toplevel().sound_vol_ctrl_label
            sound_vol_ctrl_label.configure(image=sound_vol_ctrl_label.soundlabel_off_img)

        else:
            sound_vol_ctrl_label = self.winfo_toplevel().sound_vol_ctrl_label
            sound_vol_ctrl_label.configure(image=sound_vol_ctrl_label.soundlabel_on_img)

        pygame.time.delay(100)
        audio.on_click.play(0)

class OkButton(ctk.CTkButton):
    def __init__(self, master):
        super().__init__(master=master, text="OK", width=100, fg_color="brown", text_color="black", font=("Arial", 20), hover=False, height=50, corner_radius=30, command=lambda:[audio.on_click.play(), self.save_settings(), master.destroy()])

        self.bind("<Enter>", lambda e: [self.configure(fg_color="#a7727d")])
        self.bind("<Leave>", lambda e: [self.configure(fg_color="brown")])

    def save_settings(self):
        audio.config.set("audio_vol", "bg_music", str(audio.bg_music.get_volume() * 100))
        audio.config.set("audio_vol", "on_click", str(audio.on_click.get_volume() * 100))

        with open("settings.ini", "w") as configfile:
            audio.config.write(configfile)

class SettingsWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master=master, background=master.main_menu.cget("fg_color"))
        self.title("Settings")
        self.geometry("400x250")
        self.resizable(False, False)
        self.grab_set()

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.music_vol_ctrl_label = MusicVolumeControlLabel(master=self, color=master.main_menu.cget("fg_color"))
        self.music_vol_ctrl_label.grid(row=0, column=0, sticky=ctk.NSEW, padx=(50, 0))

        music_vol_ctrl_slider = MusicVolumeControlSlider(self)
        music_vol_ctrl_slider.grid(row=0, column=1)

        self.sound_vol_ctrl_label = SoundVolumeControlLabel(master=self, color=master.main_menu.cget("fg_color"))
        self.sound_vol_ctrl_label.grid(row=1, column=0, sticky=ctk.NSEW, padx=(50, 0))

        sound_vol_ctrl_slider = SoundVolumeControlSlider(self)
        sound_vol_ctrl_slider.grid(row=1, column=1)

        ok_btn = OkButton(self)
        ok_btn.grid(row=2, column=0, columnspan=2)

        self.protocol("WM_DELETE_WINDOW", lambda: [ok_btn.save_settings(), self.destroy()])



