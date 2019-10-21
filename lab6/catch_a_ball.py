from tkinter import *
import random
import time
root = Tk()
root.geometry('800x600')

canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=1)

class Ball():
    def __init__(self):
        self.num = num
        self.y = random.randint(100, 500)
        self.x = random.randint(100, 700)
        self.r = random.randint(10, 30)
        colors = ['red', 'yellow', 'green', 'blue']
        self.color = random.choice(colors)
        self.ball = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.dx = random.randint(10, 20)
        self.dy = random.randint(10, 20)
        self.ax = random.randint(1, 5)
        self.ay = random.randint(1, 5)
        self.coords = canvas.coords(self.ball)
        self.x = (self.coords[0] + self.coords[2]) / 2
        self.y = (self.coords[1] + self.coords[3]) / 2
        self.points = 10

    def hit(self, ball2):
        if (self.x - ball2.x) ** 2 + (self.y - ball2.y) ** 2 <= (self.r + ball2.r) ** 2:
            self.dx *= -1
            self.dy *= -1
            ball2.dx *= -1
            ball2.dy *= -1

    def move_simple(self):
        self.points = 10 + (self.dx ** 2 + self.dy ** 2) / self.r ** 2
        if self.coords[3] + self.dy >= 600 or self.coords[1] + self.dy <= 0:
            self.dy *= -1
        if self.coords[2] + self.dx >= 800 or self.coords[0] + self.dx <= 0:
            self.dx *= -1
        for i in range(self.num + 1, 10):
            self.hit(ball[i])
        canvas.move(self.ball, self.dx, self.dy)
        self.coords = canvas.coords(self.ball)
        self.x = (self.coords[0] + self.coords[2]) / 2
        self.y = (self.coords[1] + self.coords[3]) / 2
        root.update()

    def move_with_acceleration(self):
        self.points = 20 + (self.dx ** 2 + self.dy ** 2) / self.r ** 2
        self.dx += self.ax * dt
        self.dy += self.ay * dt
        if self.coords[3] + self.dy >= 600 or self.coords[1] + self.dy <= 0:
            self.dy *= -1
        if self.coords[2] + self.dx >= 800 or self.coords[0] + self.dx <= 0:
            self.dx *= -1
        for i in range(self.num + 1, 10):
            self.hit(ball[i])
        canvas.move(self.ball, self.dx, self.dy)
        self.coords = canvas.coords(self.ball)
        self.x = (self.coords[0] + self.coords[2]) / 2
        self.y = (self.coords[1] + self.coords[3]) / 2
        root.update()

def click(event):
    global score
    x0 = event.x
    y0 = event.y
    for i in range(10):
        x = ball[i].x
        y = ball[i].y
        r = ball[i].r
        if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
            score += ball[i].points


canvas.bind('<Button-1>', click)
score = 0
ball = []
for i in range(10):
    num = i
    ball.append(Ball())
dt = .1
t = 0
while t < 20:
    ball[1].move_with_acceleration()
    ball[2].move_with_acceleration()
    ball[3].move_with_acceleration()
    ball[4].move_simple()
    ball[5].move_simple()
    ball[6].move_simple()
    ball[7].move_simple()
    ball[8].move_simple()
    ball[9].move_simple()
    ball[0].move_simple()
    time.sleep(dt)
    t += dt
l1 = Label(text="Game is over!\nYour score: " + str(int(score)))
l1.pack()
mainloop()