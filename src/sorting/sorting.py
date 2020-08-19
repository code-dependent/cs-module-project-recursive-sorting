# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements

#     a = 0
#     b = 0

#     # Your code here
#     # loop over the range merged_arr
#     for i in range(elements):
#         if a >= len(arrA):
#             merged_arr[i] = arrB[b]
#             b+=1
#         elif b >= len(arrB):
#             merged_arr[i] = arrA[a]
#             a+=1
#         elif arrA[a] < arrB[b]:
#             merged_arr[i] = arrA[a]
#             a+=1
#         else:
#             merged_arr[i] = arrB[b]
#             b+=1
#     return merged_arr
arrA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arrB = [0, 10, 11, 12, 13, 14, 15]

# print(merge(arrA,arrB),"<<<<")
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        l = merge_sort(arr[:middle])
        r = merge_sort(arr[middle:])

        arr = merge(l,r)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# instead of new array, lets swap stuff
# (x,y = y,x)

# what is our base case
### if the right is less than the left
### recurse downward on left and right halves

def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid +1

    if (arr[mid] <= arr[start2]):
        return arr

    while start <= mid and start2 <= end:

        if arr[start] < arr[start2]:
            start +=1
        else:
            value = arr[start2]
            indx = start2
            while indx != start:
                arr[indx] = arr[indx -1]
                indx -= 1

            arr[start] = value
            start+= 1
            start2+=1
            mid+=1

    return arr


def merge_sort_in_place(arr, left, right):
    # Your code here
    if right <= left:
        return arr
    else:
        middle = (right + left) // 2
        merge_sort_in_place(arr,left, middle)
        merge_sort_in_place(arr, middle+1, right)

        merge_in_place(arr, left, middle, right)

    return arr

def partition(arr):
    pivot = arr[0]
    left =[]
    right =[]
    for i in arr:
        if i > pivot:
            right.append(i)
        if i < pivot:
            left.append(i)
    return left, pivot, right

def quicksort(arr):
    if len(arr) == 0:
        return arr
    left, pivot, right = partition(arr)

    return quicksort(left)+[pivot]+quicksort(right)

print(quicksort([9,8,7,6,5,4,3,2,1,66,67]))


def merge(arr1, arr2):
    # TODO: figure out how many elements are going to be needed in the merged array
    elems = len(arr1) + len(arr2)
    ###
    # TODO: create the list that will contain the elems of each array. fill this list with 0 * len(arr1) + len(arr2) for now
    merged_arr = [0] * elems
    ###
    # TODO: we need variables to keep track of the index of each array element as we loop over them
    indx1 = 0
    indx2 = 0
    ###
    # TODO: loop through the range or elements
    # (assumes all elements are unique)
    for i in range(elems):
        # TODO: if the variable holding the index for arr1 id greater of equal to the len of arr1,
        # # only worry about arr2 and vice-versa
        if indx1 >= len(arr1):
            merged_arr[i] = arr2[indx2]
            indx2+=1
        elif indx2 >= len(arr2):
            merged_arr[i] = arr1[indx1]
            indx1+=1
        ###
        # else if arr1[indx1]  is greater than arr2[indx2]
        #  and vice-versa
        # (assumes elements are unique)
        elif arr1[indx1] < arr2[indx2]:
            # assign 'merged_arr' at index 'indx' to the value of arr1 at index 'indx1'
            merged_arr[i] = arr1[indx1]
            indx1+=1
        else:
            # assign 'merged_arr' at index 'indx' to the value of arr2 at index 'indx2'
            merged_arr[i] = arr2[indx2]
            indx2+=1
        ##
    return merged_arr