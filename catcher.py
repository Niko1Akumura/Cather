from tkinter import Tk, Canvas
import random
from PIL import Image, ImageTk

class WildHuntGame:
    def __init__(self, window):
        self.window = window
        self.window.title('Wild Hunt')
        self.window.resizable(width=False, height=False)

        self.canvas = Canvas(self.window, width=720, height=420)
        self.canvas.pack()

        self.background_image = Image.open("img/background_game.jpg")
        self.background_image = ImageTk.PhotoImage(self.background_image)

        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image) 

        self.canvas.create_rectangle(0, 350, 720, 420, fill="gray")

        self.count = 0
        self.missed_count = 0
        self.balls_colors = ['#00FF00', '#FFFF00', '#0B610B', '#00FF80']

        self.levels = ['Beginner', 'Advanced', 'Master']
        self.game_over = False

        self.create_widgets()
        self.ball()

    def create_widgets(self):
        self.canvas.create_text(80, 370, font='Arial 15', text='Score => ')
        self.score_text = self.canvas.create_text(125, 370, font='Arial 16', text=str(self.count))

        self.canvas.create_text(80, 390, font='Arial 15', text='Your level = ')
        self.level_text = self.canvas.create_text(180, 390, font='Arial 15', text=self.levels[0])

    def ball(self):
        if not self.game_over:
            self.canvas.delete('balls')

            x = random.randint(60, 660)
            y = random.randint(80, 320)
            r = 15
            self.current_ball = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=random.choice(self.balls_colors), width=0, tags='balls')

            self.canvas.tag_bind(self.current_ball, '<Button-1>', self.click_on_circle)
            self.canvas.after(1500, self.ball)
            
            self.missed_count += 1
            if self.missed_count >= 4:
                self.game_over = True
                self.show_game_over()
    
    def click_on_circle(self, event):
        if not self.game_over:
            self.count += 1
            self.canvas.delete(self.current_ball)
            self.missed_count = 0
            self.update_score()
            self.update_level()
            
    def update_score(self):
        self.canvas.itemconfig(self.score_text, text=str(self.count))

    def update_level(self):
        level_index = 0
        if 0 < self.count <= 5:
            level_index = 0
        elif 5 < self.count <= 15:
            level_index = 1
        else:
            level_index = 2

        self.canvas.itemconfig(self.level_text, text=self.levels[level_index])
    
    def show_game_over(self):
        self.canvas.delete('balls')
        self.canvas.create_text(360, 200, font='Arial 30', text='Game Over', fill='red')

if __name__ == '__main__':
    window = Tk()
    game = WildHuntGame(window)
    window.mainloop()
