# Global and local and non-local
'''
Scopes are a huge topic that each langauge has almost its way in declearing local and 
global function 
In python if a variable decleared outside the function of the global scope called a global.
And this var can be used anywhere where ever you want
'''

x = 3


def get_x():
    # we have access to x var but we cant change it , why ?
    print("I can use x here inside the function ", x)


get_x()
print("we can use x wherever we want", x)


'''
But what if want to change the x inside the function 
'''

'''
def change_x():
    x = x * 2
    print(x)

change_x() 
'''
'''
the above can not be done , because x been used before assignment, and also Python treats as a local var
   So how can we fix this ?
'''


def change_x():
    global x
    x = x * 2
    print("This is a changed ", x)


change_x()
'''
Global var allows you to modify vars outside the scope , so by using it inside the function 
we are telling python that it is okey to change x inside the function

Rules of global var 
1. it is global by default in the global scope 
2. var is a local inside the function when we declear it inside it
3. we use global inside the function to write and read var inside the function 
'''

# Nested function


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "change x "
        print(x)

    inner()
    print(x)


outer()
'''
In the above code , we cant change x because the scope of the inner cant change x unless 
we use the keyword nonlocal 
'''
