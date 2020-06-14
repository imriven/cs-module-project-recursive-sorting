# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    left = 0
    right = 0
    current = 0
    
    #left represents index we are looking at in the left array
    #right represents index we are looking at in right array
    #current is looking at output array = merged_arr

    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged_arr[current] = arrA[left]
            left += 1
            current += 1
        else:
            merged_arr[current] = arrB[right]
            right += 1
            current += 1
    
    while left < len(arrA):
        merged_arr[current] = arrA[left]
        left += 1
        current += 1

    while right < len(arrB):
        merged_arr[current] = arrB[right]
        right += 1
        current += 1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    arr = merge(merge_sort(left), merge_sort(right))


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

