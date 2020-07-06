'''
Knowing how the shape of the structure of your data in the memory is so essintail,because it helps you
how to deal with them.
imagine you have list of name or phone numbers and you one to do something for each one 
of them.  well, this sounds so easy to deal with especially if you have small list of them 
but what if you have a list of 10000 of items ?
now, this wasting of time and many because it costs the companies a lot of many. plus, nowdays, people
live in fast world so doing something opposite will make your client run away from you.

you are so smart person and you would ask me this, but 
              how can iterate over each element inside the list ?
               -- here programmers make it easy for by using for-loop to loop over them 
'''

nums = [10, 20, 30, 40, 50]
for num in nums:
    # this code will run over each number in the list
    # if we have list with 1000 numbers then would print 1000 times
    print(num)

# outputs
#   round 1 --> 10
#      round 2 --> 20
#         round 3 --> 30
#             round 4 --> 40
#               round 5 --> 50
'''
first you use the word for and then declear an element that represent each 
item in the list
and there is a lot of ways on how to access an item in the list through 
using for-loop and even we can know the index of an item which we will 
figure it this out later 
'''
