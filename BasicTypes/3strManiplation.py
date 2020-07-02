                       #String Maniplation
'''
In some cases we want to print out a number inside or connect to a sentence. Unfortunately, we can't 
do this in python (not every language behaves like Javascript lol). 
However, python provides some ways to help us do this
'''
# print("this is a" + 6 + "dollars")  -- > cant be done because python only concatenates strings
"""
to make it work , python has a built-in function that can convert a number to a string called str(number)
"""
print("this is a " + str(6) + " dollars") # --> works .Sweeeeeeeeeeet.

# even you can perform a mathticall  operation with this built-in function
print(str(10 + 11))
'''
since python able to concatante string it also able to split strings. 
To do the splitting , python has another built-in function that can do this 
called string.split("where do you wanna split the string but do not include the chars,  WHAAAAAAT ?")
let me show an example 
'''
print("my name is Yasir,Hassan".split(","))
'''
The output would be a list type ['my name is Yasir', 'Hassan'] notice that the "," doesn't not exist in the 
list 
another example
'''
print("my name is Yasir,Hassan".split(",Ha"))
'''the output is ['my name is Yasir', 'ssan'] 
did you get it ?
you can also access the list with index number list print("my name is Yasir,Hassan".split(",Ha")[0])
'''