# return values from function
'''
One of the amazing feature that function has is returning value 
that enables us to do lots of great thing we can even use the returning value as a value to a variable
'''


def get_sum(num1, num2):
    return num1 + num2


sum = get_sum(10, 10)
print(sum)


'''
and even more we can use the returned function an argument that we can pass to another function
'''


def get_multiplayer(num):
    return 2 * num


multiplayer = get_multiplayer(sum)
print(multiplayer)


# or

print(get_multiplayer(get_sum(20, 20)))
# COOOOOOOOOOOOOL , right ?

'''
passing by references is meaning whatever changes that you make to that information it
will also change the original data 
passing by value it will only change the data that you want without presisting data , which if you 
copy a list and you want to change it , the original one would not get any effect 
but the opposite would happend with the passing by references 


copying for large data is expensive 
PBR is cheaper 
'''

# if we have no return in a function does it remain in memory? even if it has executed?
# What’s the difference between a lightbulb and a pregnant woman? 😂😂 No cheating!!!