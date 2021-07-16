# Planetary System

# First version turtle

import turtle
import math
import astronomy.py

turtle.hideturtle()



class SolarSystem:
    def __init__(self):
        self.planets = dict()

    def add_planet(self):
        pass

    def draw_planet(self):
        pass


class Planet:
    def __init__(self, xpos, ypos,  radius, color, time, velocity=0, acceleration=0, mass=0):
        self.x = xpos
        self.y = ypos
        self.x_range = range(-self.x, self.x)
        self.y_range = range(-self.y, self.y)
        self.time = time
        self.v = velocity
        self.a = acceleration
        self.m = mass
        self.radius = radius
        self.color = color
        # Planet turtle
        self.t = turtle.Turtle()
        self.t.speed("fastest")
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.pos = self.t.pos()
        self.draw()
        # Orbit Turtle
        self.o = turtle.Turtle()
        self.o.speed("fastest")
        self.o.hideturtle()
        self.draw_orbit()

    def circle(self):
        circle_points = []
        for i, j in zip(self.x_range, self.y_range):
            res = math.sqrt(i**2 + j**2)
            circle_points.append(res)
        return circle_points

    def draw(self):
        self.t.pendown()
        self.t.fillcolor(self.color)
        self.t.begin_fill()
        self.t.circle(self.radius)
        self.t.end_fill()
        self.t.penup()

    def draw_orbit(self):
        while (self.x and self.y):
            pass

    def update(self):
        for time in range(0, self.time):
            self.t.clear()
            self.t.goto(self.pos[0] + time, self.pos[1] + time)
            self.pos = self.t.pos()
            self.draw()



earth = Planet(30, 5, 10, "green", 100)
earth.update()
turtle.Screen().exitonclick()