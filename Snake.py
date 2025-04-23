import random
import tkinter as tk
from tkinter import messagebox
from Snakeconfig import *


class SnakeGame:
    def __init__(self,root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="yellow")
        self.canvas.pack()
        self.menu_frame = tk.Frame(root)
        self.level = tk.StringVar(value='medium')
        self.score = 0
        self.running = False
        self.pause = False


if __name__ == '__main__':
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
