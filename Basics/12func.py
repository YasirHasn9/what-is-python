# the number of arguments
'''
sometimes, we dont want to commit to certain number of arguments that been passed to the function 
we want to pass to it an infint number of argument
'''


def get_numbers(*nums):
    print(nums)


get_numbers(1, 2, 3, 5)

'''
we used * sign to tell python that the argument that i want to pass to the function unlimited  
they could be one or 100 arguments 
its up to whatever the program needs of arguments in order to solve the problems 
and also these *nums means its a list so the shape of the arguments is gonna be 
list  
'''
