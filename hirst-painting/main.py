#import colorgram as cg

#colors = cg.extract('image.jpg', 2 ** 32)
#color_palette = []

#for coloring in colors:
#    r = coloring.rgb.r
#    g = coloring.rgb.g
#    b = coloring.rgb.b
#    new_color = (r, g, b)
#    color_palette.append(new_color)

#print(color_palette)

color_list = [(246, 243, 239), (247, 241, 244), (202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212), (109, 123, 149), (173, 198, 205), (105, 136, 143), (72, 64, 55)]

import turtle as t
import random

t.colormode(255)

tim = t.Turtle()



def draw(distance, space, size):
    for i in range(space):
        for j in range(space):
            tim.dot(size, random.choice(color_list))
            tim.forward(distance)
        tim.backward(space*distance)
        tim.left(90)
        tim.forward(distance)
        tim.right(90)


t.title('Hirst Painting Project')
t.Screen().bgcolor("grey")
tim.penup()
tim.setpos(-180, -180)
tim.speed('fastest')
draw(50,10,25)
tim.hideturtle()
screen = t.Screen()
screen.exitonclick()