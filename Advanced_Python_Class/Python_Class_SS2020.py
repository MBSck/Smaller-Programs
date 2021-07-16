# Start of the lecture 21.04.2020
# Bonuspoints will be given for finding errors, text and code errors

# ----Password for zip file---
    # PonteDiPietra2020
# ---------------
"""
str = "four plus two"
dic = {"four": 4, "two": 2}

print(str.split())

# Generators are useful to save memory and now script language is as fast as normal one
# don't allocate memory.
a = (i**2 for i in range(2000000))
print(a)

print(sum(a))

# if e.g. sum function is overwritten and you import module that uses sum function then it will be overwritten as well
# as python is not modular

# kill the kernel to reset functions

# can be called like this

listoflist = [[1,2,3], [1,2], [3,4,5]]
#call index of index
print(listoflist[1][1])

def f():
    def g():
        print("hello")
    return g
# assign parameter to first function and then to second
print(f()())

# make counting logger
# Everytime a decorator is called it creates a new function for the parameters input, thus there can be various loggers
def exec_counter(function):
    counter = 0
    def inner(*args):
        nonlocal counter
        counter += 1
        print("The function", function.__name__, "has been executed", counter, "times.")
        return function(args)
    return inner

sum = exec_counter(sum)
sum(10)
sum(5)
def hello(name):
    print(name)

hello = exec_counter(hello)
hello("günther")
# This function calls all the elements of the tuple "args" and the dictionary "kwargs", without the star it just calls the
# tuple and the dictionary
def f(*args,**kwargs):
    print(args, kwargs)

a = {"Hello", "Mister"}
# for example calling f(a) print whole set, butbut
f(*a)

# Challeging Exercise, run for various argument, for arbitrary argument cache
# Cache by definition doesnt call the function so dont use it for random functions and similar or functions that
# need to be called

# no typecheck in python, so you need to use decorator with annotation control
# function.__annotations__ is dictionary thus
def force_return_type(func):

    def inner(*args, **kwargs):
        print(func.__annotations__["return"])
        return func.__annotations__["return"](func(*args, **kwargs))

# one can attach parameters to functions
f.param = 5
print(f.param)
"""
"""
#Lecture 23.04

# data members of classes are self. in init
# difference between python and java and c++, there are no private data members and such, that can not be read
# and modified outside of the class

# self._paramters are meant to be private in python and if changed can maybe break class or do similar
# in python you cannot define individual symbols to do different things, multiplikation and such

# the normal comments with hashtag are completly ignored by the python interpreter, but the documentation strings
# with three quotes at the start are interpreted and will be shown in for example help()

# order of input for class should be the same as in __init__
# is better than function, as the object are stored inside the class when you define a function from it

import math

class NumericalDerivative:
    def __init__(self, f, eps):
        self.f = f
        self.eps = eps

    def __call__(self, x):
        return (self.f(x + self.eps) - self.f(x - self.eps))/(2 * self.eps)

derivative_sin = NumericalDerivative(math.sin, 1e-7)

print(derivative_sin(1))

# difference between derivative class and decorator is minute, but is hard to change parameters like epsilon, in the
# class this is easier

# Python has lots of flexibility due to classes and all but you pay the price for it with speed. If you need speed
# you have to go to lower level "C" or even "Machine Code"

# When defining a class valid definitions are

class Car:
    pass

# and

class Person:
    ...

# The dots mean that it is yet to be implemented
# The formating of strings can be done like this

def hello(name):
    return f"Hello my name is {name}"

print(hello("Marten"))
# The formating saves a lot of function calls, means less functions are being called, will call function only once and
# be faster thus if its called often.

# One can attach functions to a class from outside the class e.g.

class Human:
    def __init__(self, age, language):
        self.age = age
        self.language = language

    def say_person(self):
        print(f"His age is {self.age}, and he speaks {self.language}")


philipp = Human(19, "british")
philipp.say_person()

# Function to attach
def say_age(self):
    print(self.age)

#How not to attach function

philipp.say_age = say_age

philipp.say_age(philipp)

# however it needs to be attached to class and not to instance

Human.say_age = say_age

# Now instance needs to be updated, but not necessarily, as the class itself is changed and so it works.
# as python is dynamic language. In contrast to changing the instance only.

philipp = Human(19, "british")
philipp.say_age()

# Not recommended for use, if possible change class directly.

# This makes it possible to also decorate classes however.
def add_say_age(cls):
    def say_age(self):
        print(f"The age is {self.age}")
    cls.say_age = say_age
    return cls

@add_say_age # equal to -> Person = add_say_age(Person), like in normal decorators
class Human:
    def __init__(self, age, language):
        # Inheritance works, with *args, **kwargs, but if you want a new argument you have to add it before *args
        self.age = age
        self.language = language

    def say_person(self):
        print(f"His age is {self.age}, and he speaks {self.language}")

    def __str__(self):
        return f"The human is {self.age} and speaks {self.language}"

myself = Human(19, "english")
myself.say_age()

# In python there is no ontological difference between "number 19" and a "class". Because they are themselves objects
# From a class or similar. As it is a dynamical language we can do the above. Python converts everything into classes.

# With inheritance you can also overwrite arguments and add to them, like done in __str__

class Person(Human):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
    def __str__(self):
        return super().__str__() + f" and his name is {self.name}"

myself = Person("Marten", 24, "german")
print(myself)

# If you want to combine two subclasses both can be inherited by a dummy

class Student(Person):
    def __init__(self, subject, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.subject = subject

    def say_subject(self):
        print(f"I am studying {self.subject}")


class Sportsguy(Person):
    def __init__(self, sport, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sport = sport

    def say_sport(self):
        print(f"I am playing {self.sport}")

# If a dummy is inheriting both classes the diamond problem comes up (raute problem) one class splits into two and then
# again inherits from both, two initializers are called and not specified which one should be called

# Issue of OOP as it can happen without even realizing. There are programming languages that prohibit multiple inheritance
# In python the problem can be subverted in python with decorators and add to the class.

# Other possibility without leaving object oriented programming. Way to think about it, that e.g. person has
# several abilites so it can study when it is a student and do sports when it is a sport student.

# See this below, without inheritance

class Person:
    def __init__(self, name, age, activities):
        self.name = name
        self.age = age
        self.activities = activities

    def say_hello(self):
        print(f"Hello from {self.name}")

    def __str__(self):
        return f"Name: {self.name}"

    def do(self):
        for activity in self.activities:
            activity.do()

class StudentActivity:
    def __init__(self, subject):
        self.subject = subject

    def do(self):
        print("I am learning", self.subject)

class SporttActivity:
    def __init__(self, sport):
        self.sport = sport

    def do(self):
        print("I am playing", self.sport)


volley = SporttActivity("volley")
physics = StudentActivity("physics")

marten = Person("Marten", 24, [volley, physics])
marten.do()

# Compostition versus Inheritance, the above example is a composition

# Inheritance is often good for graphical user interfaces, e.g. button class and then variations of it. Only small changes
# Then it is natural to inherit.

# If you want to check the addition are both of the same class, use "isinstance" dont directly check the type
# as you would check the class. Then raise error if you add two different types.
import math

class Angle:
    def __init__(self, radians):
        self.radians = radians
        self.__degrees = 360 * radians /(2 * math.pi)


# "_degrees" can be used to declare private variable, but only shows that to other people, can be used to avoid
# to break class
# "__degrees" cannot be accessed in any way outside of the class
# can still be accessed by changing obfuscated variable

angle1 = Angle(3/4 * math.pi)
# the name of the variable changed
angle1._Angle__degrees = 50

# with a getter and a setter one can make a variable with the "property()" function

class Angle:
    def __init__(self, radians):
        self.radians = radians

    def getAngleDegrees(self):
        pass

    def setAngleDegrees(self):
        pass

    degrees = property(getAngleDegrees, setAngleDegrees)

# this is not going to break the class as it will set the radians correctly

class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"repr({self.x}, {self.y})"

    def __str__(self):
        return f"str({self.x}, {self.y})"

p = Test(2, 1)
print(p)

# __str__ is called when printing the class and __repr__ is a unique representation of the class not only used
# in printing or when string is needed
"""
"""
# yield functions can also be used outside of generators and then in for loops

def yield_func():
    yield "People"
    yield "stink"

for elem in yield_func():
    print(elem)

# Generator dont store the yield value it only uses one variable and consumes less memory and its only not being initialized only being called
"""
"""
# One can use the abc module in order to make an abstract class in python. Yields error when abstract class is
# instantiated

import abc


# so called interface, defines generic class and what the inherited class should do, but doesn't actually do anything.

class Shape(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass

# my_shape = Shape()


# It will also tell you when an abstract method is not yet defined even for other classes

class Square(Shape):
    pass

# my_square = Square()
"""
"""
# Important algorithms for machine learning are Mewton for finding zeroes and minima

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x*np.exp(-x**2)+1/4

# define derivative for newton method


def df(x):
    return np.exp(-x**2)-2*(x**2)*np.exp(-x**2)


x = np.arange(-0.75, 0.5, 0.01)

location_of_the_zero = 0.1 - f(0.1)/df(0.1)
print(location_of_the_zero, f(location_of_the_zero))

location_of_the_zero_second_iteration = location_of_the_zero - f(location_of_the_zero)/df(location_of_the_zero)
print(location_of_the_zero_second_iteration, f(location_of_the_zero_second_iteration))

# function can be simply called with this in plot if defined with numpy, so python will return a vector result and
# for loops withing the numpy arrays
plt.plot(x, f(x))
plt.plot(x, f(0.1)+df(0.1)*(x-0.1))
plt.plot(x, f(location_of_the_zero)+df(location_of_the_zero)*(x - location_of_the_zero), color="cyan")
plt.plot(x, f(location_of_the_zero_second_iteration)
         +df(location_of_the_zero_second_iteration)*(x-location_of_the_zero_second_iteration), color="blue")
plt.scatter([0.1, location_of_the_zero, location_of_the_zero_second_iteration], [f(0.1), f(location_of_the_zero),
                                                                                 f(location_of_the_zero_second_iteration)], color="green")
plt.axhline(y=0, color="red")
plt.ylim(-0.5, 0.5)
plt.savefig("newton_by_hand.png", dpi=600)

# Newton iteration has a problem, it will converge to the zeroes, but with a bad guess it will converge to nowhere
# Else it will converge quadratically to the zeroes.

 def newton_iteration(starting_point, f, n_steps=15):
    ...
    return x_final
"""
"""
# Minima and Maxima of function via second order newton

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x*np.exp(-x**2)+1/4


def df(x):
    return np.exp(-x**2)-2*(x**2)*np.exp(-x**2)


def df2(x):
    return -2*x*np.exp(-x**2)-4*x*np.exp(-x**2)+4*(x**3)*np.exp(-x**2)

# Use the Taylor approximation around a certain point


extremal_point = 0.3-df(0.3)/df2(0.3)
print(extremal_point)

x = np.arange(-3, 3, 0.01)
print(x)

plt.plot(x, f(x))
plt.plot(x, f(0.3)+df(0.3)*(x-0.3)+(1/2)*df2(0.3)*(x-0.3)**2)
plt.scatter([0.3], [f(0.3)], color="green")
plt.axhline(y=0, color="red")
plt.ylim(-0.5, 1.5)
plt.savefig("newton_by_hand_second_order.png", dpi=600)
plt.plot(x, x**3)
plt.show()

# second order approximation provides a approximation of the curvature around a point of the function
# find point where derivative of the function is zero, that is extrema point
# Always do a plot to see what the function does and start with doing by hand if doing an algorithm
# when you sure about what is written start doing it in a for or while loop and do it in a function
# from the function you can go over to expand it into classes and etc.
"""


# How do you ensure that you reach the minimum and not the maximum or saddle point.
# And even then how do you reach the absolute minimum and not local?
# Absolute minimum ensures an optimal neural network

# Tensorflow is important as it allows you to analytically derive the functions, Machine learning is based on
# derivatives and calculus.
'''
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x*np.exp(-x**2)+1/4


def df(x):
    return np.exp(-x**2)-2*(x**2)*np.exp(-x**2)

# Alternative to newton method, doesn't require second derivative, but arbitrary stepsize that has to be tuned
def gradient_minimum(f, df, x0, step, n_iterations=10):
    """The gradient algorithm goes to minimum, as first derivative is used and minus"""
    for i in range(n_iterations):
        x0 = x0 - df(x0)*step
    return x0


x = np.arange(-3, 3, 0.01)
minimum = gradient_minimum(f, df, 0.01, 0.3)

plt.plot(x, f(x))
plt.plot(x, f(0.1)+df(0.1)*(x-0.1))
plt.plot(x, f(minimum)+df(minimum)*(x-minimum))
plt.scatter([0.3, minimum], [f(0.3), f(minimum)], color="green")
plt.axhline(y=0, color="red")
plt.ylim(-0.5, 1.5)
plt.savefig("newton_by_hand_second_order.png", dpi=600)
plt.show()
'''

# The MNIST-database
"""
import matplotlib.pyplot as plt
import tensorflow as tf

# x_train is a picture
# y_train is the label of the picture

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


print(x_train.shape)
print(x_test.shape)

plt.imshow(x_train[12], cmap=plt.get_cmap("Greys"))
plt.show()

print(x_train[12])
print(y_train[12])

# nearest neighbor algorithm that compares pictures can be used.

# Other Method.
# Steps to analyze pictures, convert it into vectors.
# Now single array where one comes after the other, produces linear indices

x_train = x_train.reshape(60000, 28*28)
print(x_train[12])
# Number of pixel
print(28*28)
# Write function that takes input in number of pixels and outputs a number from zero to nine

# One method would be weight vector

w = ... # 28*28

# "w.x_train + constant" dot product of weight vector and number vector plus a constant

p = tf.random.uniform(shape=[28*28])
print(w)

# output is always to be floating point and not integer, we want to have an integer as floating point can be
# both one number and the other with rounding ambiguity
print(tf.reduce_sum(x_train[12]*p)+0.3)

# ask that output of the function is equal to label of the picture

# find where sum is minimal, that leads to minimal discrepancy between output of function and expected output
print(sum((tf.reduce_sum(x_train[i]*p)+0.3-y_train[i])**2 for i in range(60)))

# search of the minimum of the squared distance, and square is used for always positive (else maybe cancellation
# may occur)

# a*x+b
"""

# Differnt approach

"""Input is 28*28 picture
exptected output: 0-9 number
output: 10 numbers, each number between 0 and 1, each of the number is an output to the question:
Does the number represent the number i7"""

# What will happen if number is not 1?
# 0 0.95 0 0 0 0 0 0.8 0 0
# Tells about the possibility that the number is one of the with nonzero output
"""
import tensorflow as tf
import numpy as np
import math

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

y_train_extended = np.zeros(shape=(60000, 10), dtype=np.float32)
y_test_extended = np.zeros(shape=(10000, 10), dtype=np.float32)
# convert number into array, where 1 determines what the number is
# interesting numpy functions
for i in range(10):
    y_train_extended[np.where(y_train == i), i] = 1
    y_test_extended[np.where(y_test == i), i] = 1

print(y_train_extended[0])
print(y_train[0])


# as tensor is immutable you need to set them before and then use convert to tensor

y_train_extended = tf.convert_to_tensor(y_train_extended)
y_test_extended = tf.convert_to_tensor(y_test_extended)

# (tf.reduce_sum(x_train[12]*w[i])+b[i]-y_train[12][i])**2

# Weighted function: Each of the ten functions depends on the weight vector and the linear term
# L = w*x + b, we want output of all these functions between zero and one

# For that lets define new function called softmax
# softmax = e^{L_i}/sum(e^{L_n}), exponential of real number will always be positive -> We want positive number
# negative number doesnt have meaning to it. Then we divide by the sum of the exponential of all L_n


def softmax(L):
    sum_of_exp = sum(math.exp(elem) for elem in L)
    return [math.exp(elem)/sum_of_exp for elem in L]


print(softmax([-2, 1.4, 0.4, 0.2, -0.1, 0.9, 0.3, 0.6, 0.8, 0.7]))

# in tensorflow use tensorflow functions for normal modules. e.g. tf.math and similar

# variable is not python variable but tf.variable
x = tf.Variable(initial_value=1.3, dtype=tf.float64)

with tf.GradientTape() as g:
    g.watch(x)
    f = x*tf.math.exp(-x*x)+1/4

print(g.gradient(f, x))
# You look for the variable and you can watch many variables. Tensorflow will log all the operations with x
# Why use tensorflow?:
# Can use all of numpy and also use multithreading and differentiate analytically and more
# look into pytorch as well
"""







