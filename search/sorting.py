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


random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)


