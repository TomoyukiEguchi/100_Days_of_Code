# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


from turtle import Turtle, Screen
import random
import turtle

color_list = [(57, 106, 148), (224, 201, 110), (133, 85, 59), (222, 142, 65), (196, 145, 171), (234, 225, 203),
              (144, 179, 203), (138, 82, 105), (210, 91, 67), (187, 79, 120), (134, 182, 136), (69, 104, 89),
              (236, 223, 231), (65, 155, 90), (133, 133, 75), (49, 155, 194), (183, 192, 201), (214, 178, 191),
              (22, 68, 112), (21, 59, 95), (175, 202, 181), (114, 124, 150), (227, 176, 167), (158, 205, 214),
              (70, 59, 48), (72, 65, 53), (124, 45, 40), (110, 48, 58)
              ]

timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
timmy.hideturtle()
turtle.colormode(255)


def draw_hirst_painting():
    for i in range(10):
        color = random.choice(color_list)
        timmy.dot(20, color)
        if i == 9:
            timmy.left(90)
            timmy.forward(50)
            timmy.left(90)
        else:
            timmy.forward(50)

    for i in range(10):
        color = random.choice(color_list)
        timmy.dot(20, color)
        if i == 9:
            timmy.right(90)
            timmy.forward(50)
            timmy.right(90)
        else:
            timmy.forward(50)


num = 5
for _ in range(num):
    draw_hirst_painting()


screen = Screen()
screen.exitonclick()
