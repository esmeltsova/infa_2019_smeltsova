from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 0
        self.ax = 0
        self.color = choice(['blue', 'green', 'yellow', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, сил трения и гравитации, действующих на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.ax = -0.04*self.vx
        self.ay = -0.04*self.vy + 1
        if self.x >= 800 - self.r or self.x <= self.r:
            self.vx *= -1
        if self.y >= 600 - self.r:
            self.ay -= 1
            self.vy *= -0.8
            if -0.2 <= self.vy <= 0.2:
                self.ay = 0
                self.vy = 0
        if self.y <= self.r:
            self.vy *= -1

        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)
        if -0.5 <= self.vx <= 0.5 and self.vy == 0:
            canv.coords(self.id, -10, -10, -10, -10)



    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 3
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def remove(self):
        canv.itemconfig(self.id, fill='white')

class target():
    def __init__(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(10, 50)
        self.color = 'red'
        self.id = canv.create_oval(0, 0, 0, 0)
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)
        self.vy = rnd(-5, -1)
        self.points = 10
        self.live = 1

    def move_target(self):
        if self.y >= 600 - self.r:
            self.vy = rnd(-5, -1)
        if self.y <= self.r:
            self.vy = rnd(1, 5)
        self.y += self.vy
        canv.move(self.id, 0, self.vy)

    def hit(self):
        """Попадание шарика в цель."""
        self.points = int(10*self.vy/self.r)^2
        canv.coords(self.id, -10, -10, -10, -10)




def new_game(event=''):
    global g1, screen1, balls, bullet, score
    t1 = target()
    t2 = target()
    bullet = 0
    balls = []
    canv.itemconfig(g1, fill='black')
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    while balls or t1.live or t2.live:
        t1.move_target()
        t2.move_target()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                if bullet / 10 % 10 != 0 and bullet % 10 == 1:
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрел')
                elif bullet / 10 % 10 != 0 and 2 <= bullet % 10 <= 4:
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрела')
                else:
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                score += max(t1.points - bullet, 1)
                canv.itemconfig(screen2, text=score)
                root.after(1000, del_text)
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                if bullet / 10 % 10 != 1 and bullet % 10 == 1:
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрел')
                elif bullet / 10 % 10 != 1 and 2 <= bullet % 10 <= 4:
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрела')
                else:
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                score += max(t1.points - bullet, 1)
                canv.itemconfig(screen2, text=score)
                root.after(1000, del_text)
            if t2.live == 0 and t1.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.bind('<Motion>', '')
                for bb in balls:
                    canv.delete(bb.id)
                balls = []
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    time.sleep(1.5)
    del_text()
    g1.remove()
    canv.itemconfig(end_screen, text="Ваш результат: " + str(score), font='28')
    b1.config(text="Играть дальше", font='28')
    b1.config(command=play_button)
    b1.place(x=300, y=320)
    b2.config(text="Новая игра")
    b2.config(command=new_game_button, font='28')
    b2.place(x=300, y=360)
def del_text():
    canv.itemconfig(screen1, text='')


def play_button():
    global b1, b2
    b1.config(command=b1.place_forget())
    b2.config(command=b2.place_forget())
    canv.itemconfig(end_screen, text='')
    new_game()


def new_game_button():
    global score
    score = 0
    global b1, b2
    b1.config(command=b1.place_forget())
    b2.config(command=b2.place_forget())
    canv.itemconfig(screen2, text=score)
    canv.itemconfig(end_screen, text='')
    new_game()

screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
score = 0
screen2 = canv.create_text(30, 30, text=score, font='28')
end_screen = canv.create_text(350, 290, text='')
b1 = tk.Button(text='')
b2 = tk.Button(text='')
new_game()

tk.mainloop()

