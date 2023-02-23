import customtkinter as ctk
import tkinter as tk
import turtle
from PIL import Image
import random

import baseframe
import audioobjects as audio

class Enemy(turtle.RawTurtle):
    def __init__(self, screen, player):
        super().__init__(screen)

        self.player = player
        
        self.shape("circle")
        self.penup()
        self.speed = 7 #140px per sec
        self.acceleration = 0.00 #acceleration of 1px per sec^2
        self.setheading(int(random.randint(0, 360)))
        self.goto(random.randint(-147, 361), random.randint(-480, 55))
        while self.heading() in [0, 90, 180, 270, 360]:
            self.setheading(int(random.randint(0, 360)))

    def move(self, stop_updating_func):
        self.speed += self.acceleration

        if self.distance(self.player) <= 20:
            stop_updating_func(game_over=True)

        if self.xcor() >= 366.6499999999997 and self.ycor() >= 60:
            self.reset()

        elif self.xcor() >= 366.6499999999997 and self.ycor() <= -485:
            self.reset()

        if self.xcor() <= -152.89999999999992 and self.ycor() >= 60:
            self.reset()

        elif self.xcor() <= -152.89999999999992 and self.ycor() <= -485:
            self.reset()

        if self.xcor() >= 366.6499999999997:
            self.setheading(180 - self.heading())

        elif self.xcor() <= -152.89999999999992:
            self.setheading(180-self.heading())

        if self.ycor() >= 60:
            self.setheading(-self.heading())

        elif self.ycor() <= -485:
            self.setheading(-self.heading())

        self.forward(self.speed)

class Player(turtle.RawTurtle):
    def __init__(self, screen):
        super().__init__(screen)

        self.shape("circle")
        self.color("brown")
        self.penup()
        self.goto(random.randint(-147, 361), random.randint(-480, 55))
        self.speed = 7
        self.acceleration = 0.0

    def move(self):
        self.speed += self.acceleration

        if self.xcor() >= 366.6499999999997 and self.ycor() >= 60:
            self.reset()

        elif self.xcor() >= 366.6499999999997 and self.ycor() <= -485:
            self.reset()

        if self.xcor() <= -152.89999999999992 and self.ycor() >= 60:
            self.reset()

        elif self.xcor() <= -152.89999999999992 and self.ycor() <= -485:
            self.reset()

        if self.xcor() >= 366.6499999999997:
            self.setheading(180 - self.heading())

        elif self.xcor() <= -152.89999999999992:
            self.setheading(180-self.heading())

        if self.ycor() >= 60:
            self.setheading(-self.heading())

        elif self.ycor() <= -485:
            self.setheading(-self.heading())

        self.forward(self.speed)

    
class TurtleWindow(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, background="#eddbc7", highlightthickness=0)

        screen = turtle.TurtleScreen(self)
        screen.bgcolor("#eddbc7")
        screen.listen()

        self.player = Player(screen)
        screen.onkeypress(lambda: self.player.setheading(90), "w")
        screen.onkeypress(lambda: self.player.setheading(-90), "s")
        screen.onkeypress(lambda: self.player.setheading(180), "a")
        screen.onkeypress(lambda: self.player.setheading(0), "d")

        self.enemies = []
        for i in range(0, 20):
            self.enemies.append(Enemy(screen=screen, player=self.player))

        #---------- Walls ----------#
        x0, y0 = -165, -70
        x1, y1 = 380, 496

        self.create_arc(x0, y0, x0+40, y0+40, start=90, extent=90, style=tk.ARC, width=3)
        self.create_arc(x1-40, y0, x1, y0+40, start=0, extent=90, style=tk.ARC, width=3)
        self.create_arc(x1-40, y1-40, x1, y1, start=270, extent=90, style=tk.ARC, width=3)
        self.create_arc(x0, y1-40, x0+40, y1, start=180, extent=90, style=tk.ARC, width=3)
        self.create_line(x0+20, y0, x1-20, y0, width=3)
        self.create_line(x1, y0+20, x1, y1-20, width=3)
        self.create_line(x0+20, y1, x1-20, y1, width=3)
        self.create_line(x0, y0+20, x0, y1-20, width=3)

class PauseButton(ctk.CTkButton):
    def __init__(self, master):
        pausebutton_img_enter = ctk.CTkImage(light_image=Image.open(".\\images\\pausebutton_img_enter.png"), dark_image=Image.open(".\\images\\pausebutton_img_enter.png"), size=(50, 50))
        pausebutton_img_leave = ctk.CTkImage(light_image=Image.open(".\\images\\pausebutton_img_leave.png"), dark_image=Image.open(".\\images\\pausebutton_img_leave.png"), size=(50, 50))

        super().__init__(master=master, text="", height=55, width=55, hover=False, image=pausebutton_img_leave, bg_color="transparent", fg_color="transparent", command=lambda: [self.pause_game(), audio.on_click.play(0)])

        self.bind("<Enter>", lambda e: self.configure(image=pausebutton_img_enter))
        self.bind("<Leave>", lambda e: self.configure(image=pausebutton_img_leave))

    def pause_game(self):
        self.winfo_toplevel().game_menu.stop_updating()
        self.winfo_toplevel().game_menu.hide()
        self.winfo_toplevel().pause_menu.show()

class ScoreBoard(ctk.CTkFrame):
    def __init__(self, master):
        self.score_value = 0

        super().__init__(master=master, corner_radius=30, bg_color="transparent", fg_color="transparent")

        self.scorelabel = ctk.CTkLabel(self, text=f"Current Score: {self.score_value}", bg_color="transparent", fg_color="transparent", text_color="brown", font=("Freehand521 BT", 20, "bold"))
        self.scorelabel.pack(fill=tk.BOTH, expand=True)

    def update_score(self):
        self.score_value += 1
        self.scorelabel.configure(text=f"Current Score: {self.score_value}")

class Frame(baseframe.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.game_window = TurtleWindow(self)
        self.game_window.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=30)

        self.pause_button = PauseButton(self)
        self.pause_button.place(relx=0.075, rely=0.065, anchor=tk.CENTER)

        self.score_board = ScoreBoard(self)
        self.score_board.place(relx=0.5, rely=0.065, anchor=tk.CENTER)

    def update_frame(self):
        if self.keep_updating:
            self.game_window.player.move()
            for enemy in self.game_window.enemies:
                enemy.move(self.stop_updating)
            self.score_board.update_score()
            self.game_window.update_idletasks()

            self.winfo_toplevel().after(50, self.update_frame)

    def start_updating(self):
        self.keep_updating = True
        self.update_frame()

    def stop_updating(self, game_over=False):
        self.keep_updating = False

        if game_over == True:
            self.winfo_toplevel().restart_menu.show()
            self.score_board.score_value = 0

