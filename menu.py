from tkinter import Tk, Button, Label
from PIL import Image, ImageTk
import subprocess

class Menu:
    def __init__(self, window):
        self.window = window
        self.window.title('Wild Hunt')
        self.window.geometry('720x420')
        self.window.configure(bg='#173B0B')  # Установка цвета фона для всего окна

        self.background_image = Image.open("img/background_menu.jpg")
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = Label(self.window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.title_label = Label(self.window, text="Wild Hunt", font=("Arial", 40), bg='#173B0B', fg='white')  
        self.title_label.pack(pady=50)

        self.start_button = Button(self.window, text="Start Game", width=20, height=2, font=("Arial", 20), bg='#173B0B', fg='white', command=self.start_game)
        self.start_button.pack(pady=30)

        self.quit_button = Button(self.window, text="Quit", width=20, height=2, font=("Arial", 20), bg='#173B0B', fg='white', command=self.window.quit)
        self.quit_button.pack(pady=5)

    def start_game(self):
        self.window.withdraw()
        process = subprocess.Popen('python catcher.py', shell=True)
        process.wait()
        self.window.deiconify()

if __name__ == '__main__':
    main_window = Tk()
    menu = Menu(main_window)
    main_window.mainloop()
