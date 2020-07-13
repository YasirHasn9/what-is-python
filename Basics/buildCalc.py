# building calculator

import re
pervious = 0
run = True

'''
this is not gonna work because the run/pervious var is been decleared outside
the function. so whatever happens here is gonna effect it
how to fix this ?
we have to declear the run/pervious var as globale var that will change through the
process in the given function
    '''


def performMath():
    # this how do make a var global
    global run
    global pervious
    equation = ''

    if pervious == 0:
        equation = input("Enter equation: ")
    else:
        print("You typed ", pervious)
        equation = input(f"{str(pervious)}")

    if equation == "quit":
        print("Thanks for using me")
        run = False
    else:
        # because the eval module is so dangours and this is why we have to make
        # sure that there is no letter and other characters in case somebody print something
        # to our input and plays with our data
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if pervious == 0:
            pervious = eval(equation)
        else:
            pervious = eval(str(pervious) + equation)


while run:
    performMath()
