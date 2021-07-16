# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 00:04:03 2019

@author: Marten
"""

# -----  Excercise 1 -------
# Excercise 1.1
# .as_integer_ratio() gives the integers of a float
"""
a = 5./3.
b = 11111.258 + 5./3. - 11111.258
c = 0.058 + 5./3 - 0.058
d = 5./3. + 11111.258 - 11111.258
e = 11111.258 - 11111.258 + 5./3.

liste = [a,b,c,d,e]

for i in liste:
    print(i.as_integer_ratio(), end=",")
"""
"""
Explanation: 
"""

# Excercise 1.2
#import antigravity #funny code

# Excercise 1.3
# Argand diagram. Compute the distance from the origin point (7,3) without using the square root function
"""
import cmath

z = complex(7,3)
help(cmath) 
"""

# Excercise 1.4
# Explain why 5 == 4 is not True, is False despite the fact that 5 != 4

# Excercise 1.5
# Guessing a Number game
"""
import random
inp = int(input("I have just generated a random number between 1 and 6.\nCould you guess it? Try: "))
rnd = random.randint(1,6)

if inp == rnd:
    print("You guessed correctly!")
else:
    print("Wrong, it was", rnd, "!")
"""
# Excercise 1.6
# Fibonacci Sequence, where each number is the sum of the previous two
"""
a, b = 0, 1
start = 0

while start < 9:
    start += 1
    a, b = b, a+b
    print(a)
"""
# Excercise 1.7
# Using turtle module and While loop write a program that draws a regular heptagon
"""
import turtle
def n_gon(color, corners=7, degree=51, length=100, width=10):
    loop = 0
    turtle.color(color)
    turtle.width(width)
    while loop < corners:
        loop += 1
        turtle.forward(length)
        turtle.right(degree)
    turtle.done()
    turtle.bye()
turtle.bgcolor("black")
n_gon("red")
"""
# Excercise 1.8
# The St. Petersburg game coin tossing game
"""
import random
coin = ["heads", "tails"]

rndtoss = ""
bet = ""
def cointoss():
    loop = 1
    active = True
    bet = int(input("I am going to toss a coin many times."
                    "\nYou are going to win 2**k if no head appears after k throws."
                    "\nHow many ducats do you want to bet?"
                    ))
    while active:
        rndtoss = random.choice(coin)
        if rndtoss == "heads":
            active = False
            break
        else:
            loop += 1
    if 2**loop < bet:
        print("Bad, a head came out after", loop, 
              "throws.\nYou get only", 2**loop,
              "ducats and you have lost", bet - 2**loop)
    else:
        print("Good, a head came out after", loop, 
              "throws.\nYou get", 2**loop, 
              "ducats. You win", 2**loop - bet, "ducats.")
cointoss()
"""

# Excercise 1.9
# write a code so that a file is only written if it does not exist
"""
import os

path = os.path.exists("C:/Users/Marten/Desktop/Stick Daten/Python/my_file.txt")

if path == False:
    with open("my_file.txt", "w") as f:
        f.write("Hello world\nfrom python!")
        f.write("!!!")
else:
    print(None)

print(f.closed)
"""
# -----  Excercise 2 -------
# Excercise 2.1
# Write a function that computes factorials of a pos integer, use for-loop code
"""
def factorial():
    inp = int(input("What number do you want to know the factorial of: "))
    result = 0
    n = 1
    if inp >= 0:
        for i in range(1,inp + 1):
            n = n * i
            print(n)
factorial()

import math
print(math.gamma(5+1))
"""

# Excercise 2.2
# generate list of prime numbers with for loop up to 1000 with sieve of erasthones

# prime numbers without sieve
"""
prime_list = []
for num in range(1,1001):    
    i = 2
    while i <= num//2:
        if num % i == 0:
            break
        i += 1
    else:
        prime_list.append(num)
print(prime_list)
"""
# written with the Sieve of Erasthones
"""
a_list = [2,3,5]
for i in range(1,1001):
    if ((i % 2 == 0) or
        (i % 3 == 0) or
        (i % 5 == 0)):
        None
    else:
        a_list.append(i)

print(a_list)
"""
# Excercise 2.3
# Count all the names with the Counter() function and then sort them into the right order up to down
"""
import collections
names = """"""Christian Mathias Johannes Benedikt Lukas Markus Andre Felix Maria Chris-tian Georg
          Luca Niklas Pauline Simon Teresa Robert Muriel Corinna Christina Johannes Daniel Patrick
          Dominik Fabian Florian Urs Benedikt Christoph Cas-par Alexander Thomas Birgit Leonard
          Joachim Carina Lisa Daniel Christina Sabrina Lea Verena Denise Marlene Vincent Maximilian Daniel
          Niklas Martin Maximilian Enrico Michael Barbara Jakob Luis Ronja Elena Alex Stefano Andriy
          Valentina Katharina Eva Veronika Kenneth Rudolf Elisabeth Christoph Laurin Daniel Johannes Simon
          Florian Maximilian Patrick Sebastian Fabian Anastasia Stefan Stefan Jonathan Nico Juliane Niklas
          Martino Jonas Markus Maximilian Adrian Stefan Jannis Verena Emily Simon Alexander Kilian Tina Viola""""""
name_list = names.split()
cnt = collections.Counter()
cnt_all = 0
for word in name_list:
    cnt[word] += 1
    cnt_all += 1
print("There are", cnt_all, "unique names:")
for i in sorted(cnt.items(), key = lambda x: x[1], reverse = True):
    print(i)
#one can sort the keys, with .keys(), and the rest can be done with lambda and top to bottom with reverse
"""
# Excercise 2.4
# Use list comprehension to create a list of N entries where, starting
# from zero, each entry n is equal to the minimal number of bits required to store the integer number n.
# Test the code forN = 200 and N = 1000.


# Excercise 2.5
# Use list comprehension to create a list of N entries where, starting from zero, each entry n is equal to the number of
# different digits of n itself (forinstance equal to 3 for 1315 or 2 for 1212). Test the code for N= 300 and N= 1000.
"""
print([[str(i for i in range(0,301))]])
"""
# Excercise 2.6
# Cellular automata are discrete models defined by deterministic rules evolving a K-dimensional state vector v from the time t to t+ 1.
# The entries of the vector are called cells, and can have different states. The simplest one-dimensional cellular automata,
# often called elementary automata, is described by a vector of length N where each entry is either zero or one, corresponding to a cell
# being in the states “dead” or “alive”, or “on” and “off”. A new vector v_t+1 is generatedfrom the previous v_t accordingly to a rule that
# takes into account for each cellonly its nearest neighbors, i.e. the new v_t+1[i]-entry depends on the old entries v_t[i+ 1],
# v_t[i] and v_t[i−1]. Periodic boundary conditions are typically chosen:the left neighbor0−1of the cell zero corresponds to the last
# entry N−1, whilethe entryNcorresponds to the first entry. As the model and the vector entriesare discrete, the number of all
# possible elementary cellular automata is finite and equal to 28 = 256. Although simple and deterministic, cellular automata can
# exhibit an apparently random chaotic behavior [6, 7, 8].
# alive state is 1, dead state is 0
"""
def start():
    cond = True
    n = int(input("Define the state of the first cell: "))
    while cond:
        if n == 0 or n == 1:
            cond = False
            break
        else:
            print("Can only be 0 for dead or 1 for alive")
            n = int(input("Define the state of the first cell: "))
    vector = []
    vector.append(inp)

start()
"""
# -----  Excercise 3 -------
# Excercise 3.1
# write a function that returns area of a circle and document what it is supposed to be doing
"""
import math
import dis
def circle_area(radius):
    """"""This function takes the radius of a circle and returns its area""""""
    return math.pi *(radius**2)
print(circle_area(1))
"""
# Excercise 3.2
# use the function dis to get a readable code of the compiled bytecode of the previous excercise
"""
dis.dis(circle_area)
"""

# Exercise 3.3
# Write the "Midnight Formula" in code as a function
"""
import math

def quadratic_roots(a,b,c):
    midnight_root = math.sqrt(b**2-4*a*c)
    print("This function returns the postive and negative root of a quadratic polynom: ")
    return -b - midnight_root, -b + midnight_root
print(quadratic_roots(1,3,2))
"""
# Exercise 3.4
# Consider the following code and say what message will be printed in the end
"""
def shout(message):
    message = message.upper()
    print(message)
message = "stop it!"
shout(message)
print(message)
#The last message will be printed in lower Case as it is taken from the global variable and not the local variable of the shout() function
"""
# Excercis 3.5
# Can you provide as input parameter of a function a module


# Excercise 3.6
# Example class list has a function sort, which can have an optional argument key to specify the function
# they should use in sorting, for instance decreasing order
"""
a_list = [2,5,1,-5,6]

a_list.sort()
print(a_list)

a_list.sort(key = lambda x: -x)
print(a_list)
"""

"""
#Use lambda expression to sort list of two elements according to second entry
list_1 = [[1,9],[-2,1],[3,5]]
list_1.sort(key=lambda x:x[1])
print(list_1)

#use to sort to first sort the list in increasing order after the second and then the first entry
list_2 = [[12,3],[7,9],[8,9],[7,11]]
list_2.sort(key=lambda x:x[0])
list_2.sort(key=lambda x:x[1])
print(list_2)
"""
# Excercise 4.1
# Chessboard of rice you double the amount of cents each chessfield you put it on
"""
def chess_func(n):
    if n == 1:
        return 1
    elif n <= 1:
        return None
    else:
        return 2**n + chess_func(n-1)
print(chess_func(64))
"""
# Excercise 4.2
# Fibonnaci sequence with recursion
"""
def fib_seq(n):
    if n <= 1 and n >= 0:
        return n
    elif n < 0:
        return None
    else:   
        return fib_seq(n-1) + fib_seq(n-2)
print(fib_seq(12))
"""

# Excercise 4.4
# Write a function that sorts a list of integers numbers of arbitrary length by increasing absolute value using recursion
# implementing the algorithm merge sort

# Excercise 4.5
# Following the same strategy of binary search, write a function "insert(sorted_list, elem)" that inserts a new elem
# into a list of integers by increasing value in such a way that after the insertion the list is still sorted
# Note that scanning and accessing all elements of the sorted list is not required, even in the worst case where the elem
# is larger than all inserted elements



# -----  Excercise 5 -------
#FINISHED ALL EXERCISES IN 5
# --------------------------
# Exercise 5.1
# Write a sphere class with attributes radius and position. With methods surface and volume and is_intersecting
# to return area of surface, volume and to test wheather a sphere is intersecting with another.
# What is the type is_intersecting should return?
"""
import math

class sphere():
    def __init__(self, radius, position):
        self.radius = radius
        self.position = position
    def area_surface(self):
        return 4*math.pi*self.radius**2
    def volume(self):
        return (4/3)*math.pi*self.radius**3
    def is_intersecting(self, sphere2):
        if (math.sqrt((self.position - sphere2.position)**2) <=  sphere2.radius 
        or math.sqrt((self.position - sphere2.position)**2) <= self.radius):
            return True
        else:
            return False
sphere1 = sphere(3,3)
sphere2 = sphere(3,0)
print(sphere1.is_intersecting(sphere2))

#The intersecting function should return a boolean (True or False)
"""

# Excercise 5.2
# write a PolarComplex that stores a complex number in polar coordinates
# using the data members p and phi as pexpphi with member functions
# __abs__ for the absolute value, __mul__ to multiply another polar complex number and return the result
# __truediv__ to divide by another polar and return the result and __str__ to return a string representing the polar complex
"""
import math

class PolarComplex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = math.sqrt(self.x**2 + self.y**2)
        self.psi = math.degrees(math.acos(self.x/self.r))
    def __abs__(self):
        return PolarComplex(self.x**2, 0)
    def __mul__(self, other):
        return PolarComplex(self.r * other.r,
                            self.psi + other.psi)
    def __truediv__(self, other):
        return PolarComplex(self.r / other.r,
                            self.psi - other.psi)
    def __str__(self):
        if self.psi == 0:
            return "("+str(self.r)+")"
        else:
            return "("+str(self.r)+"*exp("+str(self.psi)+"j)"+")"
polar_a = PolarComplex(2,0)
polar_b = PolarComplex(4,0)
print(polar_a * polar_b)
"""
# Excercise 5.3
# Extend the build-in class "dict" to implement a home-made class "defaultdic", so that if a key is accessed but not present in a dictionary
# it is automatically set to a default value
"""
class Defaultdict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __getitem__(self, key):
        if self.get(key) == None:
            self.__setitem__(key, "default")
        else:
            self.get(key)

dict_1 = Defaultdict({1:"Ten"})
dict_2 = dict({1:"Ten"})
print(dict_1[10])
print(dict_1)
print(dict_2)
"""
# Excercise 5.4
# Use functors to compute an approximation of the Riemann zeta function as defined from the infinite sum
"""
import scipy.special as sc_sp

class Riemann_Zeta:
    def __init__(self, power):
        self.s = power
    def __call__(self, N):
        result = 0
        for i in range(1, N+1):
            result += 1/(i**self.s)
        return result


riemann = Riemann_Zeta(1.15)

print(riemann(10000000))
print(sc_sp.zeta(1.15,1))
"""
# Exercise 5.5
# Write a functor Cache that stores a function f of one variable and implements a method "__call__" that calls and stores the output
# of the function f, so that if the function is called twice with the same argument, the stored output is returned without calling again f.
# Test your functor on a recursive function implementing the Fibonnaci numbers
"""
class Cache:
    def __init__(self, function):
        self.func = function
        self.call_map = dict()
    def __call__(self, *args):
        if args not in self.call_map:
            self.call_map[args] = self.func(*args)
        return self.call_map[args]

#can also be done directly with decorators
@Cache
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Can be done this way (exactly as you would with decorators)
#fibonacci = Cache(fibonacci)
print(fibonacci(300))
"""


# Excercise 5.6
# Write a class like Vector2D, but for n-dimensions and add scalar product and the element wise multiplication of two vectors
# What should happen if the user tries to sum to vectors of different dimensions?
"""
#Good way to understand the usage of args
class VectorND:
    def __init__(self, *args):
        self.args = []
        self.result = 0
        for num in args:
            self.args.append(num)
        self.length = len(self.args)
        self.new_vector = []
        for i in range(self.length):
            self.new_vector.append(0)
    def norm(self):
        result = 0
        for num in self.args:
            result += num**2
        return result
    def scalar(self, other):
        for i in range(self.length):
            self.result += self.args[i] * other.args[i]
        return self.result
    def __eq__(self, other):
        if self.length != other.length:
            raise ValueError("Vectors are not of the same dimension")
        else:
            if self.args == other.args:
                return True
            else:
                return False
    def __add__(self, other):
        if self.length != other.length:
            raise ValueError("Vectors are not of the same dimension")
        else:
            for i in range(self.length):
                self.new_vector[i] = self.args[i] + other.args[i]
            return VectorND(self.new_vector)
    def __sub__(self, other):
        if self.length != other.length:
            raise ValueError("Vectors are not of the same dimension")
        else:
            for i in range(self.length):
                self.new_vector[i] = self.args[i] - other.args[i]
            return VectorND(self.new_vector)
    def __mul__(self, other):
        if self.length != other.length:
            raise ValueError("Vectors are not of the same dimension")
        else:
            for i in range(self.length):
                self.new_vector[i] = self.args[i] * other.args[i]
            return VectorND(self.new_vector)
    def __getitem__(self, item):
        for num in range(self.length):
            if item == num:
                return self.args[item]
    def __setitem__(self, key, value):
        for num in range(self.length):
            if num == key:
                self.args[num] = value
    #Doesn't do anything at the moment
    def __str__(self):
        string = "("
        for num in range(self.length):
            string += str(self.args[num]) + ","
        string = string[:-1] + ")"
        return string

vector_1 = VectorND(3,4,7)
vector_2 = VectorND(3,4,7)

print(vector_1.scalar(vector_2))
"""
# -----  Excercise 6 -------
# Excercise 6.1
# Write a decorator to measure the execution time of a function. The printed output of the decorated
# function should be "... has been executed in 3.1 seconds"
# Use the decorator to see how long it takes to execute the function fibonacci(34) using recursion.
"""
import time as t

def execution_time(function):
    time_map = 0
    def inner(*args):
        nonlocal time_map
        start_t = t.time()
        result = function(*args)
        end_t = t.time()
        print("The function", function.__name__, "has been executed in", end_t-start_t, "secs.")
        return result
    return inner


#@execution_time
def fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

#you can force the decorator to only print out the last result, by appending the number of calls to the end.
#fibonacci_sequence = execution_time(fibonacci_sequence)(35)
#print(fibonacci_sequence)
"""
# Excercise 6.2
# Compare the computing time of the fibonacci function above with and without the decorator for n=30. Do you notice a
# difference? Estimate the number of function calls in both cases
"""
start_t = t.time()
print(fibonacci_sequence(30))
end_t = t.time() - start_t
print("Execution time", end_t)

fibonacci_sequence = execution_time(fibonacci_sequence)(30)
print(fibonacci_sequence)
"""
# Exercise 6.3
# Modify the decorator above to log also each time an attribute of an object is accessed

# __dict__ is where to objects are stored and can be accessed again
"""
def log_properties_and_access(cls):
    class Inner(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__dict__ = self
            for attr in self.__dict__:
                print(attr, "initalized to",
                      self.__dict__

                      [attr])
        def __setattr__(self, attr, value):
            print("setting", attr, "to", value)
            # will loop if set with self.__dict__[attr], because it gets the dict attribute
            self.__dict__[attr] = value
        #__getattr__ is only called when fetched attribute doesn't exist in the class
        def __getattribute__(self, attr):
            print("accessing attribute", attr)
            return self[attr]
    return Inner

@log_properties_and_access
class Square:
    def __init__(self, length):
        self.length = length

a_square = Square(5)
a_square.length = 9
"""
# Excercise 6.4
# Write a decorator check_range to check the range of the input value of a function, the range being provided with
# annotations. the decorator should for instance work like
# so that if the input variables "a" and "b" are outside the range specified, such as by calling f(5,13), an
# exception ValueError is raised


# This makes it possible to check the format needed for the function
# Does not force the input parameter to take any form though
""""
'''
def a(length:float) -> float:
    return length**2
    
    
print(a.__annotations__["return"](a("Hello")))
'''
import inspect


def boundaries(function):
    map_execute = dict()
    check_range_list = list()
    def inner(*args, **kwargs):
        get_args = inspect.signature(function).\
            bind(*args, **kwargs).arguments
        for i in get_args:
            check_range = list(function.__annotations__[i])
            if (get_args[i] < check_range[0])\
                or (get_args[i] > check_range[1]):
                map_execute[i] = False
            else:
                map_execute[i] = True
        if False in map_execute.values():
            raise ValueError("Value is outside of the functions range")
        return function(*args, **kwargs)
    return inner

@boundaries
def f(a: (0, 9), b: (3, 12)):
    return a + b

print(f(1,12))
"""
# -----  Excercise 7 -------
# Excercise 7.1
# Write a generator for the Fibonacci Sequence running up to a given F_n by defining a class with a member function __iter__
# Add also to the same class the possibility to check if a number "is" in the given sequence (function __contains__)
# , and the possibility to access randomly the element k of the sequence (function __getitem__). If k is larger than n,
# and IndexError exception should be raised.
"""
class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.n = 2
    def __contains__(self, item):
        pass
    def __iter__(self):
        self.n = 2
        self.res = 0
        while n < self.limit:
            #yield is used for iter and saves the function until this point and contains the execution point
            yield n
            self.res += (self.n - 1) + (self.n - 2)



for i in range(5):
    res += (n-1) + (n-2)
"""


# -----  Excercise 8 -------
# Excercise 8.1
# Using the module tkinter.messagebox write a simple program that waits four seconds and then display an information
# message. The message should be "All documents have been sucessfully deleted from your hard disk." Given that the script
# could really run some functions from the module os how safe is it to run a python code that you have not carefully read?
# Do you have a solution to prevent such a situation? If so, the program should wait another 10 seconds before displaying
# another message "It was a joke, don't worry!"However the next time I would suggest to... your suggestion.
"""
import tkinter as tk
import tkinter.messagebox as mbox
import time as t

class Message(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Test")
        t.sleep(4)
        self.display_message()
        t.sleep(10)
        self.joke_message()
    def display_message(self):
        mbox.showinfo("Progress", "All documents have been successfully deleted from your harddisk")
    def joke_message(self):
        mbox.showinfo("Joke", "It was a joke, don't worry! However the next time I would suggest to read your code!")
        
window = tk.Tk()
Message(window)
"""
# Excercise 8.2
# Using the module "tkinter", create a simple GUI ask to the user which one is the best programming language "java", "python"
# "C", "C++", "fortan" and "perl". The user should be able to select only one option. If "python" is selected, a message
# "Excellent choice!" should be shown, otherwise the message should be "I repect your opinion, but I totally disagree with
# you, programming in xxx is horrible" (xxx in the message should be replaced with the name of the programming language
# chosen by the user)
"""
import tkinter as tk
import tkinter.messagebox as mbox

class BestProgrammingLanguage(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_widgets()
        self.binds()
    def create_widgets(self):
        #Create Label
        self.label = tk.Label(master=window, text="Chose the best programming language!")
        self.label.grid(row=0, column=0, columnspan=3)
        #Create Buttons
        self.option = tk.IntVar()
        self.button_C = tk.Radiobutton(master=window,
                                  text="C", variable=self.option, value=1)
        self.button_C.grid(row=1, column=0)
        self.button_Cpp = tk.Radiobutton(master=window,
                                    text="C++", variable=self.option, value=2)
        self.button_Cpp.grid(row=2, column=0)
        self.button_Py = tk.Radiobutton(master=window,
                                   text="Python", variable=self.option, value=3)
        self.button_Py.grid(row=1, column=1)
        self.button_J = tk.Radiobutton(master=window,
                                   text="Java", variable=self.option, value=4)
        self.button_J.grid(row=2, column=1)
        self.button_f = tk.Radiobutton(master=window,
                                   text="fortran", variable=self.option, value=5)
        self.button_f.grid(row=1, column=3)
        self.button_p = tk.Radiobutton(master=window,
                                   text="perl", variable=self.option, value=6)
        self.button_p.grid(row=2, column=3)
    def callback(self, event):
        if self.option.get() == 3:
            mbox.showinfo("Right!","Excellent Choice!")
        else:
            self.dict = {1:"C", 2:"C++", 3: "Python", 4: "Java", 5: "fortran", 6: "perl"}
            self.text = self.dict[self.option.get()]
            mbox.showinfo("Wrong!","I respect your opinion, but I totally disagree with you, programming in " + self.text + " is horrible!")
        self.quit()
    def binds(self):
        self.button_C.bind("<ButtonRelease>", self.callback)
        self.button_Cpp.bind("<ButtonRelease>", self.callback)
        self.button_Py.bind("<ButtonRelease>", self.callback)
        self.button_J.bind("<ButtonRelease>", self.callback)
        self.button_f.bind("<ButtonRelease>", self.callback)
        self.button_p.bind("<ButtonRelease>", self.callback)
window = tk.Tk()
window.title("Chose a Programming Language!")

app = BestProgrammingLanguage(master=window)

tk.mainloop()
tk.destroy()
"""
# Excercise 8.3
# Using the module "tkinter", create a GUI to order a Pizza. The user should be able to select one or more ingredients
# ("pineapple", "mushroom", "prosciutto", "onions", "sardellen",...), possible extras (extra cheese, extra tomato sauce,
# basilicum, etc.) and a field free for comments of the user. If pineapples are chosen as ingredients, an error message
# "Pineapples for a pizza are totally wrong, please retry!" should be shown, otherwise the message should show the
# the ingredients, the extras selected and the comment of the user
"""
import tkinter as tk

class PizzaOrder(tk.Frame):
    def __init__(self, master):
        #Setting up the Parameters
        super().__init__(master)
        self.master = master
        self.master.title("Craft your own Pizza.")
        self.master.geometry("250x400")
        self.main_ingredients()
        self.extra_ingredients()
        self.comments()
        self.order_button()
    def main_ingredients(self):
        self.var = tk.BooleanVar()
        #Creating the main Label and the main buttons
        self.label = tk.Label(self.master, text="Main Toppings:")
        self.label.grid(row=0, column=0)
        self.c_button_p = tk.Checkbutton(self.master,
                                    text="pineapples", var=self.var)
        self.c_button_p.grid(row=1, column=0)
        self.c_button_m = tk.Checkbutton(self.master,
                                    text="mushrooms")
        self.c_button_m.grid(row=2, column=0)
        self.c_button_pr = tk.Checkbutton(self.master,
                                     text="prosciutto")
        self.c_button_pr.grid(row=3, column=0)
        self.c_button_o = tk.Checkbutton(self.master,
                                    text="onions")
        self.c_button_o.grid(row=4, column=0)
        self.c_button_s = tk.Checkbutton(self.master,
                                    text="sardellen")
        self.c_button_s.grid(row=5, column=0)
    def extra_ingredients(self):
        self.label_e = tk.Label(self.master, text="Extra Toppings:")
        self.label_e.grid(row=6, column=0)
        self.c_button_ec = tk.Checkbutton(self.master,
                                          text="extra cheese")
        self.c_button_ec.grid(row=7, column=0)
        self.c_button_et = tk.Checkbutton(self.master,
                                          text="extra tomato sauce")
        self.c_button_et.grid(row=8, column=0)
        self.c_button_b = tk.Checkbutton(self.master,
                                          text="extra basilicum")
        self.c_button_b.grid(row=9, column=0)
    def comments(self):
        self.label_t = tk.Label(self.master, text="Comments:")
        self.label_t.grid(row=10, column=0)
        self.text = tk.Text(self.master, height=5, width=30)
        self.text.grid(row=11, column=0)
    def order_button(self):
        self.order = tk.Button(self.master,
                              text="Order")
        self.order.grid(row=12, column=0,columnspan=4)
window = tk.Tk()
app = PizzaOrder(window)

tk.mainloop()
"""
# Excercise 8.4
# Create a class that implements a GUI interface to ask multiple choice questions to the user. The initializer should take
# as input the question, a list of the possible answers, and an index of the correct one. A message should inform the user
# wheather the selected answer is correct or not.
"""
import tkinter as tk

class MultipleChoice(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
"""

# -----  Excercise 9 -------
# Excercise 9.1
# Consider the performance test above, what happens if the size of the array is ten thousands or ten millions?
"""
import numpy as np
import time

v = np.random.uniform(-5,5,size=100000000)

start_time = time.time()
np_sum = np.sum(v[v<10000000])
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
my_sum = 0
for i in range(100000000):
    if v[i] < 10000000:
        my_sum += v[i]
end_time = time.time()

print(end_time - start_time)
print(np_sum, my_sum)
"""

# Excercise 9.2
# Using the matplotlib.pyplot module, prepare a plot that shows the Taylor approximation of sin(x) between -4 and 4,
# including the first two , four, six terms of the infinite series above
"""
import matplotlib.pyplot as plt
import numpy as np
import math

def taylor_sinus(x, cutoff):
    res = 0
    for i in range(0, cutoff):
        res += ((x**(2*i + 1))/math.factorial(2*i + 1))*((-1)**i)
    return res

x = np.linspace(-4, 4, 1000)
y1 = np.sin(x)
y2 = taylor_sinus(x, 2)
y3 = taylor_sinus(x, 4)
y4 = taylor_sinus(x, 6)


p1, = plt.plot(x, y1, label="sin(x)", color="blue")
p2, = plt.plot(x, y2, label="n=2", color="red")
p3, = plt.plot(x, y3, label="n=4", color="purple")
p4, = plt.plot(x, y4, label="n=6", color="green")

plt.xlabel("x")
plt.ylabel("y")

plt.legend(handles=[p1, p2, p3 , p4])

plt.subplots_adjust(wspace=0.4, left=0.1, top=0.9, bottom=0.1)
plt.show()
"""
# Excercise 9.3
# Prepare a scatter plot of the yearly growth in percantage of the nominal and real GDP for France, Germany, Italy, Spain,
# United Kingdom, USA and Greece for the last thirty years using the data of the World Bank database. Use the "savefig"
# to save the scatter plot to a file

# Excercise 9.4
# Prepare a plot of the function tan(x) similar to the one in Fig.9.1 the x-range -4pi and 4pi. Red points should mark
# the postion of the zeros on the x-axis of tan(x), while dashed red vertical lines should highlight the position of the
# asymptotes. Modify the FuncFormatter function so that pi is shown instead of 1pi for the first tick in the x-axis.
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import numpy as np
import math

fig, ax = plt.subplots()

x = np.linspace(-4*np.pi, 4*np.pi, 1000)    #linespace returns onyl 50 elements within any given range
y = np.tan(x)

#show grid
plt.grid()

ax.scatter([np.pi*k/2. for k in range(-8, 9, 2)],
           [0 for k in range(-8, 9, 2)], color="r")

#plot tan(x) without the connecting lines
y[:-1][np.diff(y) < 0] = np.nan

#makes the dashed lines for the asymptotes
xcoords = [np.pi*k/2. for k in range(-7, 8, 2)]
for xc in xcoords:
    plt.axvline(x=xc, color="r", linestyle="dashed")

#sets the limits for x and y
plt.ylim(-5, 5) #limit the range of y so that it looks better with 50 elements
plt.xlim(-4*np.pi, 4*np.pi) #limits in the x direction

#set the labels to radians (done by hand)
#radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
#radians = [n * np.pi for n in radian_multiples]
#radian_labels = ["$-2\pi$", "$-3\pi/2$", "$-\pi$", "$-\pi/2$", "0", "$\pi/2$", "$\pi$", "$3\pi/2$", "$2\pi$"]

#done more elegantly with FuncFormatter
def format_func(value, ticknumber):
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${}\pi/2$".format(N)
    else:
        return r"${}\pi/2$".format(N)

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
#plt.xticks(radians, radian_labels)
plt.title("$y = tan(x)$", fontsize=14)

plt.plot(x, y)

plt.show()
"""
# -----  Excercise 10 -------
# Excercise 10.1
# Does the bisection method work if there are an even number of zeros in the interval [a,b]? And if the numbers of zeros is
# odd?

# Excercise 10.2
# Implement your own function for finding the root of a function using the Newton method. Apply the method to the function
# and the starting point of the example above for 20 steps and plot the linear approximation of Eq 9.2 together with
# f for each iteration. Do you understand why the Newton method fails to converge?
"""
#also possible as class
'''
class Derivative:
    def __init__(self, function, epsilon=10e-09):
        self.f = function
        self.eps = epsilon
    def __call__(self, x):
        return (self.f(x + self.eps) -
                self.f(x + self.eps))/(2 * self.eps)
'''
#newton converges quadratically to the root faster than the bisection method
import matplotlib.pyplot as plt

def derive(f, x):
    eps = 10e-09
    return (f(x + eps) - f(x - eps))/(2 * eps)



def newton_method(function, x0, n):
    global x_list
    global y_list
    counter = 0
    x_list = []
    y_list = []
    while counter < n:
        x1 = x0 #in this case x1 would be x0 and vice versa
        x0 = x0 - function(x0)/derive(function, x0)
        y = function(x1) + (x0 - x1) * derive(function, x0)
        counter += 1
        x_list.append(x0)
        y_list.append(y)
    return x0, x_list, y_list

#Python sets a few variables when its starting (like __name__) and then it executes all the code found in the file
#if your module is the main program, then interpreter will assign name main to it

#its as if interpreter inserts this at the top of program that is being executed if yours is not the main program
#e.g. imported and  __name__ == "foo" then it will not satisfy the if condition
if __name__ == "__main__":
    def f(x):
        return x**2 - 3.*(x**3) + 5.*x - 1
        #return x**3 - 2. * (x**2) - 11. * x + 12


    newton = newton_method(f, 0.65, 20)

    x = x_list
    f_list = []
    for i in x_list:
        f_list.append(f(i))
    y1 = y_list
    y2 = f_list

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()
#The newton method fails to converge is that if the tangent line on the guess point doesnt cut the x-axis, then
#no new guess will be made and at no point the x-axis will be cut and a solution won't be found.
"""
# Excercise 10.3
# Considering the example above, find the interval around the origin where the Newton method converges to the zero x = 0.
"""
    #one point for that it converges is x0 = 1
    newton = newton_method(f, 1, 20)
"""

# Exercise 10.4
# Consider for instance alpha = -0.05, alpha = -0.10, and alpha = -0.15, with K = 100, for which t does y double?
"""
import numpy as np
import matplotlib.pyplot as plt

def solve_diffeq(time, alpha, initialcondition=100):
    return initialcondition * np.exp(- alpha * time)

func_list = []
for i in range(0,1001):
    func_list.append(solve_diffeq(i, -0.05))
    func_list.append(solve_diffeq(i+1000, -0.10))
    func_list.append(solve_diffeq(i+2000, -0.15))

x = np.arange(0, 1000)
y1 = func_list[:1000]
y2 = func_list[1000:2000]
y3 = func_list[2000:3000]

ax1 = plt.subplot(2, 2, 1)
ax2 = plt.subplot(2, 2, 2)
ax3 = plt.subplot(2, 2, 3)

ax1.plot(x, y1, color="r")
ax2.plot(x, y2, color="g")
ax3.plot(x, y3, color="y")

plt.show()

#doubles roughly at t = 900, exponential explosion
"""
# Exercise 10.5
# Euler numerical solution for differential equation, plot differences between numerical and analytical
"""
import numpy as np
import matplotlib.pyplot as plt
import operator

#numerical solution of differential equation

def euler_solve_fo(timepassed, epsilon, alpha=0.15, y0=100):
    #Only accounts for positive times and for whole integers as time
    global y_list
    y_list = []
    diffeq_list = []
    counter = 0
    while counter < timepassed:
        y0 = (1 - alpha * epsilon) * y0
        y_list.append(y0)
        diffeq = - alpha * y0
        diffeq_list.append(diffeq)
        counter += 1
    return diffeq_list

def euler_solve_so(timepassed, epsilon, alpha=0.15, y0=100):
    global y_so_list
    y_so_list = []
    diffeq_so_list = []
    counter = 0
    while counter < timepassed:
        y0 = (1 - alpha * epsilon + ((alpha**2) * (epsilon**2)) / 2) * y0
        y_so_list.append(y0)
        diffeq = - alpha * y0
        diffeq_so_list.append(diffeq)
        counter += 1
    return diffeq_so_list

#analytical solution of the differential equation

def solve_diffeq(time, alpha=0.15, initialcondition=100):
    global func_list
    func_list = []
    for i in range(0, time + 1):
        func_list.append(initialcondition * np.exp(- alpha * time))
    return func_list

#differnce plots, substract analytic solution from numerical one
fig, ax = plt.subplots(2, 3) #first is number of rows second number of columns

x = np.arange(0, 10)
y1 = list(map(operator.sub, euler_solve_fo(10, 2.), solve_diffeq(10)))
y2 = list(map(operator.sub, euler_solve_fo(10, 1.), solve_diffeq(10)))
y3 = list(map(operator.sub, euler_solve_fo(10, 0.5), solve_diffeq(10)))

y4 = list(map(operator.sub, euler_solve_so(10, 2.), solve_diffeq(10)))
y5 = list(map(operator.sub, euler_solve_so(10, 1.), solve_diffeq(10)))
y6 = list(map(operator.sub, euler_solve_so(10, 0.5), solve_diffeq(10)))

ax[0][0].plot(x, y1, color="r")
ax[0][1].plot(x, y2, color="g")
ax[0][2].plot(x, y3, color="b")
ax[1][0].plot(x, y4, color="r")
ax[1][1].plot(x, y5, color="g")
ax[1][2].plot(x, y6, color="b")

plt.tight_layout()  #makes sure individual graphs do not overlap with other ones
plt.show()
"""
# Exercise 10.6
# Solve the differential equation of the damped harmonic oscillator with external periodic force numerically

# Exercise 10.7
# Using the function scipy.optimize.curve_fit and the data from the world bank fit population of various country to
# some features


# -----  Excercise 12 -------
# Excercise 12.1
# Approximate the integral sqrt(1-x**2) from -1<x<1 = np.pi/2. Generate a random point box (-1,1)x(0,1). Compute it
# for 10000000. How does Monte Carlo approximation converge to np.pi. Plot the error of the first approximation
# using the first  10000, 20000, 30000 and 40000 and so on randomly generated points

# Excercise 12.2
# Compare the integral approximation of the previous exercise to the "trapezoidal rule" by preparing the same
# convergence plot using the same number N of evaluations of the function sqrt(1-x**2)
