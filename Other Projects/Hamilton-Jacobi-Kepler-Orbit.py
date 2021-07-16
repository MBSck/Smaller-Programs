from math import sqrt, cos, sin, pi
from turtle import Screen, Turtle


class Star(Turtle):
    def __init__(self, colour):
        super().__init__(shape='circle')

        self.color(colour)


class Planet(Turtle):
    def __init__(self, colour, mass, energy, gravitational_potential, alpha_phi, return_point):
        super().__init__(shape='circle')

        self.color(colour)

        self.alpha_phi = alpha_phi
        self.mass = mass
        self.energy = energy
        self.gravitational_potential = gravitational_potential
        self.return_point = return_point / (2*pi)

        self.t = 0
        self.speed('fastest')
        self.shapesize(0.25)

        self.penup()
        self.orbit()
        self.pendown()

    @property
    def semi_lactus_rectum(self):
        return 2*(self.alpha_phi**2)/self.gravitational_potential

    @property
    def eccentricity(self):
        return (1/self.gravitational_potential)*\
               sqrt(self.gravitational_potential**2+8*self.mass*self.energy*(self.alpha_phi**2))

    @property
    def major_axis_a(self):
        return self.semi_lactus_rectum/(1-self.eccentricity**2)

    @property
    def minor_axis_b(self):
        return sqrt(self.major_axis_a*self.semi_lactus_rectum)

    def orbit(self):
        angle = self.t / (2 * pi)

        self.goto(self.major_axis_a*cos(angle-self.return_point), self.minor_axis_b*sin(angle)-self.return_point)

        self.t += 1
        screen.ontimer(self.orbit)


if __name__ == "__main__":
    screen = Screen()

    sun = Star('orange')
    earth = Planet('blue', mass=1, energy=-1, gravitational_potential=-1000, alpha_phi=-50, return_point=0)

    screen.mainloop()



