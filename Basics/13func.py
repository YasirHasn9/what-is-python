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
