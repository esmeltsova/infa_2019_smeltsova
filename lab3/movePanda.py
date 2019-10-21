from graph import *
import math

time = 0
dt = 5

def draw_BG():
    width = 500
    height = 333
    windowSize(width, height)
    brushColor(255, 175, 128)
    rectangle(0, 0, width, height)


def ellipse (x0, y0, a, b, angle):
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

def bambuk (x0, y0, h, w): #h width, w height
    penColor(0, 104, 55) #x0 + h(x - 74) = x0 - 74 h + hx
    brushColor(0, 104, 55)
    penSize(5*w)
    line (74 * h + x0 - 74 * h, 229 * w + y0 - 229 * w, 74 * h + x0 - 74 * h, 197 * w + y0 - 229 * w)
    line (74 * h + x0 - 74 * h, 193 * w + y0 - 229 * w, 74 * h + x0 - 74 * h, 157 * w + y0 - 229 * w)
    penSize(3*w)
    line (69 * h + x0 - 74 * h, 151 * w + y0 - 229 * w, 72 * h + x0 - 74 * h, 131 * w + y0 - 229 * w)
    penSize(2*w)
    line (70 * h + x0 - 74 * h, 126 * w + y0 - 229 * w, 76 * h + x0 - 74 * h, 97 * w + y0 - 229 * w)
    branch1 = [(66 * h + x0 - 74 * h, 175 * w + y0 - 229 * w), (64 * h + x0 - 74 * h, 170 * w + y0 - 229 * w), \
               (60 * h + x0 - 74 * h, 164 * w + y0 - 229 * w), (55 * h + x0 - 74 * h, 158 * w + y0 - 229 * w), \
               (52 * h + x0 - 74 * h, 156 * w + y0 - 229 * w), (50 * h + x0 - 74 * h, 155 * w + y0 - 229 * w), \
               (45 * h + x0 - 74 * h, 154 * w + y0 - 229 * w), (41 * h + x0 - 74 * h, 155 * w + y0 - 229 * w), \
               (37 * h + x0 - 74 * h, 156 * w + y0 - 229 * w)]
    branch2 = [(76 * h + x0 - 74 * h, 162 * w + y0 - 229 * w), (80 * h + x0 - 74 * h, 152 * w + y0 - 229 * w), \
               (84 * h + x0 - 74 * h, 145 * w + y0 - 229 * w), (88 * h + x0 - 74 * h, 141 * w + y0 - 229 * w), \
               (94 * h + x0 - 74 * h, 139 * w + y0 - 229 * w), (102 * h + x0 - 74 * h, 141 * w + y0 - 229 * w)]
    branch3 = [(64 * h + x0 - 74 * h, 143 * w + y0 - 229 * w), (57 * h + x0 - 74 * h, 131 * w + y0 - 229 * w), \
               (48 * h + x0 - 74 * h, 123 * w + y0 - 229 * w), (38 * h + x0 - 74 * h, 116 * w + y0 - 229 * w), \
               (29 * h + x0 - 74 * h, 112 * w + y0 - 229 * w), (16 * h + x0 - 74 * h, 110 * w + y0 - 229 * w)]
    branch4 = [(78 * h + x0 - 74 * h, 127 * w + y0 - 229 * w), (83 * h + x0 - 74 * h, 119 * w + y0 - 229 * w), \
               (91 * h + x0 - 74 * h, 109 * w + y0 - 229 * w), (98 * h + x0 - 74 * h, 103 * w + y0 - 229 * w), \
               (106 * h + x0 - 74 * h, 98 * w + y0 - 229 * w), (119 * h + x0 - 74 * h, 95 * w + y0 - 229 * w)]
    penSize(1)
    polyline(branch1)
    ellipse(39 * h + x0 - 74 * h, 163 * w + y0 - 229 * w, 1 * h, 6 * w, 350)
    ellipse(45 * h + x0 - 74 * h, 163 * w + y0 - 229 * w, 1 * h, 6 * w, 350)
    ellipse(51 * h + x0 - 74 * h, 168 * w + y0 - 229 * w, 1 * h, 6 * w, 350)

    polyline(branch2)
    ellipse(90 * h + x0 - 74 * h, 153 * w + y0 - 229 * w, 1 * h, 6 * w, 10)
    ellipse(95 * h + x0 - 74 * h, 150 * w + y0 - 229 * w, 1 * h, 6 * w, 10)
    ellipse(100 * h + x0 - 74 * h, 148 * w + y0 - 229 * w, 1 * h, 6 * w, 10)

    polyline(branch3)
    ellipse(19 * h + x0 - 74 * h, 120 * w + y0 - 229 * w, 1 * h, 6 * w, 350)
    ellipse(23 * h + x0 - 74 * h, 120 * w + y0 - 229 * w, 1 * h, 6 * w, 350)
    ellipse(27 * h + x0 - 74 * h, 123 * w + y0 - 229 * w, 1 * h, 6 * w, 350)
    ellipse(32 * h + x0 - 74 * h, 126 * w + y0 - 229 * w, 1 * h, 6 * w, 350)
    ellipse(39 * h + x0 - 74 * h, 128 * w + y0 - 229 * w, 1 * h, 6 * w, 350)

    polyline(branch4)
    ellipse(100 * h + x0 - 74 * h, 115 * w + y0 - 229 * w, 1 * h, 6 * w, 10)
    ellipse(106 * h + x0 - 74 * h, 112 * w + y0 - 229 * w, 1 * h, 6 * w, 10)
    ellipse(110 * h + x0 - 74 * h, 109 * w + y0 - 229 * w, 1 * h, 6 * w, 10)
    ellipse(113 * h + x0 - 74 * h, 105 * w + y0 - 229 * w, 1 * h, 6 * w, 10)
    ellipse(117 * h + x0 - 74 * h, 104 * w + y0 - 229 * w, 1 * h, 6 * w, 10)

def panda (x0, y0, size):
    penColor("white")
    brushColor("white")
    ellipse(360 * size + x0 - size * 360, 190 * size + y0 - size * 190, 55 * size, 30 * size, 0)
    penColor("black")
    brushColor("black")
    paw1 = [(403 * size + x0 - size * 360, 187 * size + y0 - size * 190), (408 * size + x0 - size * 360, 190 * size + y0 - size * 190), \
            (411 * size + x0 - size * 360, 197 * size + y0 - size * 190), (410 * size + x0 - size * 360, 224 * size + y0 - size * 190), \
            (407 * size + x0 - size * 360, 236 * size + y0 - size * 190), (403 * size + x0 - size * 360, 247 * size + y0 - size * 190), \
            (397 * size + x0 - size * 360, 257 * size + y0 - size * 190), (389 * size + x0 - size * 360, 266 * size + y0 - size * 190), \
            (378 * size + x0 - size * 360, 275 * size + y0 - size * 190), (367 * size + x0 - size * 360, 273 * size + y0 - size * 190), \
            (350 * size + x0 - size * 360, 255 * size + y0 - size * 190), (384 * size + x0 - size * 360, 204 * size + y0 - size * 190), \
            (395 * size + x0 - size * 360, 191 * size + y0 - size * 190), (400 * size + x0 - size * 360, 188 * size + y0 - size * 190)]
    paw2 = [(364 * size + x0 - size * 360, 145 * size + y0 - size * 190), (364 * size + x0 - size * 360, 222 * size + y0 - size * 190), \
            (357 * size + x0 - size * 360, 268 * size + y0 - size * 190), (333 * size + x0 - size * 360, 288 * size + y0 - size * 190), \
            (323 * size + x0 - size * 360, 288 * size + y0 - size * 190), (303 * size + x0 - size * 360, 278 * size + y0 - size * 190), \
            (303 * size + x0 - size * 360, 268 * size + y0 - size * 190), (321 * size + x0 - size * 360, 249 * size + y0 - size * 190),\
            (334 * size + x0 - size * 360, 215 * size + y0 - size * 190)]
    paw3 = [(310 * size + x0 - size * 360, 160 * size + y0 - size * 190), (321 * size + x0 - size * 360, 242 * size + y0 - size * 190), \
            (300 * size + x0 - size * 360, 270 * size + y0 - size * 190), (278 * size + x0 - size * 360, 258 * size + y0 - size * 190), \
            (275 * size + x0 - size * 360, 254 * size + y0 - size * 190), (274 * size + x0 - size * 360, 244 * size + y0 - size * 190), \
            (278 * size + x0 - size * 360, 189 * size + y0 - size * 190)]
    polygon(paw1)
    polygon(paw2)
    polygon(paw3)
    penColor("white")
    brushColor("white")
    head = [(357 * size + x0 - size * 360, 198 * size + y0 - size * 190), (347 * size + x0 - size * 360, 207 * size + y0 - size * 190), \
            (334 * size + x0 - size * 360, 214 * size + y0 - size * 190), (313 * size + x0 - size * 360, 220 * size + y0 - size * 190), \
            (299 * size + x0 - size * 360, 220 * size + y0 - size * 190), (284 * size + x0 - size * 360, 209 * size + y0 - size * 190), \
            (281 * size + x0 - size * 360, 203 * size + y0 - size * 190), (279 * size + x0 - size * 360, 194 * size + y0 - size * 190), \
            (279 * size + x0 - size * 360, 145 * size + y0 - size * 190), (315 * size + x0 - size * 360, 122 * size + y0 - size * 190), \
            (324 * size + x0 - size * 360, 122 * size + y0 - size * 190), (329 * size + x0 - size * 360, 125 * size + y0 - size * 190), \
            (357 * size + x0 - size * 360, 147 * size + y0 - size * 190)]
    polygon(head)
    penColor("black")
    brushColor("black")
    ellipse(290 * size + x0 - size * 360, 215 * size + y0 - size * 190, 11 * size, 6 * size, 0)
    ellipse(285 * size + x0 - size * 360, 185 * size + y0 - size * 190, 10 * size, 13 * size, 0)
    ellipse(318 * size + x0 - size * 360, 192 * size + y0 - size * 190, 13 * size, 13 * size, 0)
    left_ear = [(275 * size + x0 - size * 360, 157 * size + y0 - size * 190), (270 * size + x0 - size * 360, 153 * size + y0 - size * 190), \
                (269 * size + x0 - size * 360, 148 * size + y0 - size * 190), (270 * size + x0 - size * 360, 142 * size + y0 - size * 190), \
                (273 * size + x0 - size * 360, 135 * size + y0 - size * 190), (279 * size + x0 - size * 360, 127 * size + y0 - size * 190), \
                (288 * size + x0 - size * 360, 122 * size + y0 - size * 190), (291 * size + x0 - size * 360, 121 * size + y0 - size * 190), \
                (296 * size + x0 - size * 360, 121 * size + y0 - size * 190), (300 * size + x0 - size * 360, 123 * size + y0 - size * 190), \
                (303 * size + x0 - size * 360, 126 * size + y0 - size * 190), (302 * size + x0 - size * 360, 131 * size + y0 - size * 190)]
    right_ear = [(339 * size + x0 - size * 360, 132 * size + y0 - size * 190), (343 * size + x0 - size * 360, 130 * size + y0 - size * 190), \
                 (348 * size + x0 - size * 360, 130 * size + y0 - size * 190), (354 * size + x0 - size * 360, 134 * size + y0 - size * 190), \
                 (361 * size + x0 - size * 360, 143 * size + y0 - size * 190), (363 * size + x0 - size * 360, 154 * size + y0 - size * 190), \
                 (362 * size + x0 - size * 360, 165 * size + y0 - size * 190), (358 * size + x0 - size * 360, 170 * size + y0 - size * 190), \
                 (355 * size + x0 - size * 360, 171 * size + y0 - size * 190), (352 * size + x0 - size * 360, 171 * size + y0 - size * 190), \
                 (348 * size + x0 - size * 360, 167 * size + y0 - size * 190)]
    polygon(left_ear)
    polygon(right_ear)
    
def draw_Scene(time):
    bambuk(74, 229, 1, 1)
    bambuk(173, 231, 1, 5/4 + time / 1000)
    bambuk(248, 223, 3/2, 3/2)
    bambuk(440, 215, 1, 9/8)
    panda(360, 190, 1)
    xSmall = 250 - time
    ySmall = 260 + 0.001 * time * time
    sizeSmall = 2/5 + time/300
    panda(xSmall, ySmall, sizeSmall)
    

def func():
    global time
    draw_BG()
    draw_Scene(time)
    time += dt
    
onTimer(func, dt*10)
run()
   