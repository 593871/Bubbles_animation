import tkinter as tk
import random

class Bubbles:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.paint = canvas.create_oval(x, y, x+20, y+20, outline='grey')
        self.speed = random.randint(1, 3)
        
    def update(self):
        self.canvas.move(self.paint, 0, -self.speed)

class Windows:
    def __init__(self, win):
        self.win = win
        self.canvas = tk.Canvas(self.win, width=550, height=550)
        self.canvas.pack()
        
        self.lis = []
        
        for _ in range(10):
            x = random.randint(0, 500)
            y = random.randint(0, 500)
            bubble = Bubbles(self.canvas, x, y)
            self.lis.append(bubble)
        
        self.animate()
        
    def animate(self):
        for bubble in self.lis:
            bubble.update()
        self.win.after(50, self.animate)

if __name__ == '__main__':
    win = tk.Tk()
    win.title('Bubbles')
    Windows(win)
    win.mainloop()