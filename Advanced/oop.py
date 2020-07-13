'''
Python is multi-paradigm language which means it support different way to get the job done.
one of these ways is creating objects & this known oop(the main focus is on the object not the functions)
in oop object has 2 parts 
1.attributes 
2.behaviors
The concpet of oop is creating reusable code , to make object we have to know how to deal with classes.

Class is blueprint of the object and object is instantiation of class
'''

'''
1.OPP Inheritance is a way of creating a new class for using details about an exiting class.
so the newly class(child class) is made of the base class(parent class) without modify the base one.

this relationship can be defined between  specific child classes that extand the functionality of 
a genreal parent class , this hierarchal relationship helps writing clean code and also allows to re-use it 


inheritcane allows for using hierarchical relationships 
avoid redundant code
python allows for multiple inheritance
'''


class Animal:
    def __init__(self, name, hunger, diet):
        self.name = name
        self.hunger = hunger
        self.diet = diet

    def eat(self, food):
        if food > 0 and self.hunger < 25:
            self.hunger += food


class Dog(Animal):

    # these init would help us to override the init in the parent (method overriding )
    def __init__(self, name, hunger, diet, breed, indoor):
        # to use the attributes form the parent (base class ) we have to call the super on it
        # and call the initializer of the base class
        super().__init__(name, hunger, diet)
        self.breed = breed
        self.indoor = indoor

    def fetch(self, ballX, ballY):
        self.ballX = ballX
        self.ballY = ballY


class Student:
    def __init__(self, name):
        self.name = name


class Graduate(Student):
    # init here is overriding the init in the parent class(Student)
    def __init__(self, name, graduation_date):
        super().__init__(name)
        self.name = name
        self.graduation_date = graduation_date


# association relationship between class that can make great functionality through
# composition between
# composition when more than class work together to make one object with great ability


class Duck:
    def __init__(self, tail, bill):
        self.tail = tail
        self.bill = bill

    def about(self):
        return f"This is {self.tail.length} and {self.bill.description}"


class Tail:
    def __init__(self, length):
        self.length = length


class Bill:
    def __init__(self, description):
        self.description = description


duck = Duck(Bill('wide orange'), Tail('long')) # beauty  
 