# Bubble Sort
'''
Bubble sort is another way of sorting a list 
2 pair compare theirselves to each other and keep going until the larger one bubble up 
in the last index in the list while the smallest be at the bottom last index 0
the way this works:
1. comaper every 2 nighbor element in the list
2. if the ele on the left > the ele on the right then swap
3. the ele that stays on the right side would keep comapring itself 
to other element in the list until if find the one that smaller then the right one
3. when it find the one that greater than the one that we were 
comparing to other , the greater one start comapering itself to other 
el in the list if there is any
4 . this keeping going until the larger one be in the last index in the list
'''


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True


# worst case , the time complexity is O(n^2)
random_list_of_nums = [5, 2, 1, 8, 4]
print("bubble sort sort before sorting \n", random_list_of_nums,  "\n")
bubble_sort(random_list_of_nums)
print("after \n" ,random_list_of_nums)


# Selection sorting
'''
Selecting sorting is another way for inserting elements in the list to sort them
imagine we have a dock of cards and we want to sort them 
1. check every card in the list
2. select the smallest card in the list
3. swap what the ele in the index 0, now the ele is in the right spot
4. repeat the process

so the element in the list would divide into 2 parts sortted one and unsorted.
treated the leftmost part as sorted and jump to the second part to find the smallest item in it 
and compare it to the sorted item in the leftmost one
'''


def selection_sort(arr):
    # i corresponds to number of items in list
    for i in range(len(arr)):
        # consider the first index 0 in arr is the lowest value
        lowest_value_index = i
        # loop over the rest of the items in the arr
        for j in range(i + 1, len(arr)):
            # find if there is item that is lowest than the sorted item
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j

            # make the swap with lowest unsorted item with the first unsorted element
            arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]

# the time complexity is O(n^2)
random_list_of_nums = [12, 8, 3, 20, 11]
print("###################")
print("selection sort sort before sorting \n", random_list_of_nums, "\n")
selection_sort(random_list_of_nums)
print("after \n",random_list_of_nums)



