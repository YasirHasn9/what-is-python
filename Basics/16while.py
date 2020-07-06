# while-loop
'''
while loop is another way to iterate over items in the list 
there is a slightly different between for-loop and while-loop ? 
'''
sum = 0
num = 5
i = 0
while i < num:
    sum += i
    i += 1
    print(sum)
'''
while loop requires some stuff to work with 
initializer 
so in while-loop is good for looping around something that we don't know how many times should we run
the loop , it stops when the given condition return false.
 so the while loop checks if the condition is true.
'''

# now we can use both looping statement and the logic ones

checkNumber = True
number = 1
while checkNumber:
    print(number)
    if number == 100:
        checkNumber = False
    number += 1
