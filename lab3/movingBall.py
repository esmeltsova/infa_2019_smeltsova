#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:44:15 2019

@author: student
"""

from graph import *
import math

time = 0
dt = 5
x = 0
y = 0
vx = 1
vy = 1

def draw_BG():
    width = 500
    height = 333
    windowSize(width, height)
    brushColor(255, 175, 128)
    rectangle(0, 0, width, height)


def ellipse(x0, y0, a, b, angle):
    penColor("black")
    brushColor("black")
    ellip =[]
    angle = angle * math.pi / 180
    points = 60
    for i in range(points):
        t = 2 * math.pi * i / points
        x = a * math.cos(t)
        y = b * math.sin(t)
        x1 = x0 + x * math.cos(angle) + y * math.sin(angle)
        y1 = y0 + y * math.cos(angle) - x * math.sin(angle)
        ellip.append((x1, y1))
    polygon(ellip)
    
def draw_Scene(time):
    global x
    global y
    global vx
    global vy
    if (0 < x + vx * dt < 500):
        x += vx * dt
    else:
        vx *= -1
        x += vx * dt
    if (0 < y + vy * dt < 333):
        y += vy * dt
    else:
        vy *= -1
        y += vy * dt   
    ellipse(x, y, 30, 30, 0)
    

def func():
    global time
    draw_BG()
    draw_Scene(time)
    time += dt
    
onTimer(func, 10*dt)
run()