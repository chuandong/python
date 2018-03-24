import turtle
import time

def draw_turtle(draw):
    for i in range(1, 5):
        draw.forward(100)
        draw.right(90)

def draw_picture():
    window = turtle.Screen()
    window.bgcolor("yellow")
    brad = turtle.Turtle()
    brad.speed(2)
    for i in range(1, 37):
        turtle.fillcolor("red")
        turtle.pencolor("red")
        draw_turtle(brad)
        brad.right(10)
    window.exitonclick()

if __name__=="__main__":
    draw_picture()