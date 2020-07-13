# Big O notation
'''
The point of run time comlixcity is to differentiate the efficiency one algorithm to another
to get the same result 

so we have to ask ourself if we have some amount of data and we want to do  some operation on it 
how long does take to perform them 


one type if the big O notation is the O(C)
O(C) is the best run comlixcity of all and it means no what matter how large is our data we have
the number of operation is stable and will not change , so we can describe 
the operation as an indexed-operated which means there a certain thing and certain place will be fetched
like:
'''


def get_item(arr):
    # no matter the size of data is , the operation will happen once at that index and that's it
    return arr[99]
# or


def loop_over_arr(arr):

    # the operation will perform 50 times and that is
    for i in range(50):
        return arr[i]


# x******************************************************
        # Log of N - log(n)
'''
Log(n) is the second best type of run comlixcity but not as good as O(c)
the if the size of the data gets larger the operations that needs to perform on it will not increase 
by very much
think of the dictionary , if you are looking for a word , you are not gonna check every 
page of the dictionary, because you know how it orginazed, we might not know the exact
page of it but we have a solid idea where it is.
so the Binary search works perfectly with this 
'''


def binary_search(sorted_arr, target):
    low = 0
    high = len(sorted_arr) - 1
    midpoint = (high - low) / 2
    if target == sorted_arr[midpoint]:
        # then the terget index is the midpoint
        return midpoint
    elif target < sorted_arr[midpoint]:
        # make the midpoint the high index
        return binary_search(sorted_arr[:midpoint])
    else:
        # make the midpoint the low index
        return binary_search(sorted_arr[midpoint:])


# *********************************************************
        # Linear Time
'''
Linear O(n) time is the increasing of number of the operation as a linear function to the input size of n
so the more we have data the more the number of operation gets increasing like counting something
'''


def search(arr, target):
    for element in arr:
        if target == element:
            return True

