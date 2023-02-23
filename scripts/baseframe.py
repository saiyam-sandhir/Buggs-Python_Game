# Copyright (c) 2023 Saiyam Jain

import customtkinter as ctk

class Frame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk):
        super().__init__(master, height=master.winfo_height(), width=master.winfo_width(), fg_color="#eddbc7", border_width=5, border_color="orange", background_corner_colors = ("#000001", "#000001", "#000001", "#000001"), corner_radius=30)

    def show(self):
        self.grid(row=0, column=0, sticky=ctk.NSEW)

    def hide(self):
        self.grid_forget()