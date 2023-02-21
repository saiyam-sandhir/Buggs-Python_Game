import customtkinter as ctk
import tkinter as tk

import mainmenu, gamemenu, pausemenu 

class DiscDashGame(ctk.CTk):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        super().__init__()

        SCREEN_WIDTH, SCREEN_HEIGHT = self.winfo_screenwidth(), self.winfo_screenheight()
        WIN_XCOORD, WIN_YCOORD = (SCREEN_WIDTH // 2) - (WINDOW_WIDTH // 2), (SCREEN_HEIGHT // 2) - (WINDOW_HEIGHT // 2)

        self.title("Disc-Dash")
        self.after(201, lambda: [self.iconbitmap(".\\images\\icon.ico"), self.iconphoto(True, tk.PhotoImage(file=".\\images\\icon.png"))])
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WIN_XCOORD}+{WIN_YCOORD}")
        self.overrideredirect(True)
        self.attributes("-transparentcolor", "#000001")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.main_menu = mainmenu.Frame(self)
        self.game_menu = gamemenu.Frame(self)
        self.pause_menu = pausemenu.Frame(self)

        self.main_menu.show()

        self.mainloop()

if __name__ == "__main__":
    WINDOW_WIDTH, WINDOW_HEIGHT = 600, 700
    DiscDashGame(WINDOW_WIDTH, WINDOW_HEIGHT)