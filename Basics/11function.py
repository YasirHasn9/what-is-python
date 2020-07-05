# default Parameters


def person_info(name = "Ricky", age = 29):
    print("Hello, my name is " + name + " and my age is " + str(age))
    print("Hello, my name is ", name, " and my age is ", age)
    '''
    this called concatenation inside the print function and also notice 
    that i have used the str() built-in function in first print() , why ? 
                                                 -- google it

    and i have not converted age to str in the second print(), why? 
                                                -- google it
    
    '''

# now i can call the function without having to pass arguments to it 
# because i have default values in the deceleration
person_info()

# and also i can pass to them argument and change the default values 
person_info("Stephon" , 33)
# i told ya , they can do magical job ,)
