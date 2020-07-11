# building calculator

import re
pervious = 0
run = True


def performMath():
    # this how do make a var global
    equation = input("Enter equation: ")
    if equation == 'quit':
        global run
        global pervious
        print("See you soon")
        # this is not gonna work because the run/pervious var is been decleared outside
        # the function. so whatever happens here is gonna effect it
        # how to fix this ?
        # we have to declear the run/pervious var as globale var that will change through the
        # process in the given function
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()+" "]', '', equation)
        pervious = eval(equation)
        print("You typed ", equation)


while run:
    performMath()
