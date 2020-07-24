'''
Bubble compare 2 pairs to each other and if one them is less the the other then this one 
be on the left side of the greater one and this process keeps repeating until the lareger 
item in the list be at mosttop right of the list and the smallest one stays in the left
[4,1,6,9,4] => [1,4,6,9,4] => [1,4,4,6,9]
'''

def bubble_sort(arr):
    swapped = True
    # We set swapped to True in the beginning to ensure that the algorithm runs at least once.
    while swapped:
        # for the purpose of iteration
        swapped = False  
        for i in range(len(arr) - 1):
            # check the one of the left is less then the one of the right and is so , then swapped
            if arr[i] > arr[i + 1]:
                print("before", arr[i] , arr[i + 1] )
                arr[i] , arr[i + 1] = arr[i + 1] , arr[i]
                print("after",arr[i] , arr[i + 1])
                swapped = True #repeat the process 

                # if the one item is in the right position, the iteration would not happen again 


li = [8,6,5,3,10,9]
bubble_sort(li)
print(li)
