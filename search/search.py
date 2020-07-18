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


'''
Binary Search 
we are gonna start form the middel index
if target value found at the middle index:
     Then it is great and return the item

if the target is greater that the middel index:
    then eliminate the data from 0 - middle index
    and keep going on this style of searching
else:
    it means that the target value start from the 0- middle index 
    and eliminate the rest of the data 
    and keep going doing this style of searching 
'''


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = (high - low) / 2
    if arr[mid] == target:
        return True
    elif target > arr[mid]:
        mid = mid + 1
        binary_search(arr[mid:], target)
    else:
        high = mid - 1
        binary_search(arr[:high], target)
