# Exercise 3.5

"""Here python copies each list by reference"""

a_list = [5] * 4
a_list[2] = 1
print(a_list)

"""This means that now when you change the elements of one sublist, then python uses the elements of the inner list
and applies the same reference to the outer lists as well"""

a_list = [[5]] * 4
a_list[2][0] = 1
print(a_list)

a_list = [[5]] * 4
a_list[2] = 1
print(a_list)
