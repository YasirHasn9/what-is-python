# Ways of searching

'''
let's say we have data of thousand of thousand of names and we want to find certain 
name if we go though each name that called a linear search 


# This is Linear Search 
check the name if at index:
   return true if we found it 
else:
    return false if we dont and that would go to the end of out list 


order allows us to eliminate part of the data that enables our search to be faster

'''


def linear_search(arr, target):
    for el in arr:
        if el == target:
            return True


'''
            Imagine if we have 10000000 items in the list and the target is the last 
            item in the list , this would take a lot of time
'''


