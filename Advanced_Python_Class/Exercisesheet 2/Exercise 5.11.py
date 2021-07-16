# Exercise 5.11

# functions


def init(self, name, age):
    self.age = age
    self.name = name

def init_s(self, name, age, university):
    super(Student, self).__init__(name, age)
    self.university = university

def init_m(self, name, age, instrument):
    super(Musician, self).__init__(name, age)
    self.instrument = instrument

def init_t(self, name, age, subject):
    super(Teacher, self).__init__(name, age)
    self.subject = subject

def info(self):
    print(f"I am {self.name} and I am {self.age} years old.")

def info_s(self):
    super(Student, self).print_info()
    print(f"I study in {self.university}")

def info_m(self):
    super(Musician, self).print_info()
    print(f"I play the {self.instrument}")

def info_t(self):
    super(Teacher, self).print_info()
    print(f"I teach {self.subject}")

# Classes

Person = type("Person", (), {"__init__": init,
                             "print_info": info})
Student = type("Student", (Person, ), {"__init__": init_s,
                                       "print_info": info_s})
Musician = type("Musician", (Person, ), {"__init__": init_m,
                                         "print_info": info_m})
Teacher = type("Teacher", (Person, ), {"__init__": init_t,
                                       "print_info": info_t})


# Printout

me = Person("Marten", 24)
me.print_info()
me_student = Student("Marten", 24, "Regensburg")
me_student.print_info()
me_musician = Musician("Marten", 24, "piano")
me_musician.print_info()
me_teacher = Teacher("Marten", 24, "physics")
me_teacher.print_info()