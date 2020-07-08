import  datetime
import calendar
# datetime
'''
To work with time in python , we have to import a class called datetime , that
contains a lot of info about the time
'''
# import datetime


# to see what is inside the datetime
# print(dir(datetime))


# to get the current day
# print(datetime.date.today())


'''
since a datetime is module that has a lot classes and each class has
its own classes to play with
so here i imported the datetime so i can get access to year, month and day
'''
today = datetime.date.today(
)  # it is an obj that holds {year: "" , month: "" , day: ""}
print(today.year)
print(today.month)
print(today.day)


# now dealing with time calendar
# in order to play with you have to import it
# to check what class does it have use the code below
# print(dir(calendar))

print(calendar.month(2020,7))

