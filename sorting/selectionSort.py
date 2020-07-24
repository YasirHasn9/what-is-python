'''
Selection sort is an algorithm if sorting the arrays by segment them into 
2 arrays , one sorted and another is unsorted 

implemetaion:
   we are gonna treat the one of the left as sorted array because it's only 
   have one element and take the smallest element in the unsorted array 
   and append to the sorted one
'''

def selection_sorting(arr):

    #  the number of loop is determine by how many element in the arr
    for i in range(0 , len(arr)):
        # assume the first element in the unsorted array is the smallest one
        smallest_index = i
        # this loop iteration over the unsorted arr
        for j in range(i + 1,len(arr)):
            # check the smallest item in the unsorted array less
            # than the one in the sorted arr
            if arr[j] < arr[smallest_index]:
                # then make  smallest_index the index in the unsorted arr
                smallest_index += 1
            arr[smallest_index] , arr[i] = arr[i] , arr[smallest_index]
    
    return arr


            

arr = [4,0,1,0,5,10]
print(arr)
print(selection_sorting(arr))
print(arr)

