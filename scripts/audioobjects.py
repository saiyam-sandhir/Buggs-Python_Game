from pygame import mixer
import configparser

mixer.init()
config = configparser.ConfigParser()
config.read("settings.ini")

bg_music = mixer.Sound(".\\audio_assets\\bg_music.wav")
bg_music.set_volume(config.getfloat("audio_vol", "bg_music")/100)

on_click = mixer.Sound(".\\audio_assets\\hover.mp3")#Sound Effect from Pixabay
on_click.set_volume(config.getfloat("audio_vol", "on_click")/100)