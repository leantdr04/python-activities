# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("images.jpg", 48)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
color_list = [(162, 12, 37), (241, 224, 73), (172, 90, 37), (23, 40, 62), (205, 157, 19), (209, 170, 74), (45, 95, 157),
              (116, 161, 209), (143, 66, 99), (213, 122, 165), (37, 32, 23), (96, 12, 72), (29, 47, 42), (10, 58, 141),
              (60, 96, 83), (183, 184, 216), (179, 8, 4), (69, 177, 144), (100, 90, 185), (114, 174, 153),
              (231, 172, 192), (232, 66, 39), (174, 96, 133), (231, 218, 7), (42, 73, 77), (39, 78, 70),
              (242, 166, 155), (159, 210, 191), (70, 66, 57), (89, 139, 164)]
turtle_module.colormode(255)
turtle_module.speed("fastest")


# def draw_spirograph(gap):
#     for _ in range(int(360 / gap)):
#         tim.color(random.choice(color_list))
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap)
#
#
# draw_spirograph(5)


tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_dot = 100

for dot_count in range(1, num_dot + 1):
    tim.showturtle()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.fd(50)
    tim.pendown()

    if dot_count % 10 == 0:
        tim.hideturtle()
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()

screen = turtle_module.Screen()
screen.exitonclick()
