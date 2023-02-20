import customtkinter as ctk
import baseframe

class Frame(baseframe.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text="pause menu", text_color="black")
        self.label.pack()
