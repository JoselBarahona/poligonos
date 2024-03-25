from turtle import Turtle, Screen
import random

t=Turtle()
t. shape("turtle")
t.width(3)


def poligono (lado,n):
    for i in range(n):
        t.right(360/n)
        t.fd(lado)
        

def poligonos ():
    for i in range(3,11):
        poligono(100,i)
        t.color(random.random(),random.random(),random.random())
poligonos()









screen=Screen()
screen.exitonclick()