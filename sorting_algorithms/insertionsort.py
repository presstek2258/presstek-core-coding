# insertion sort psuedocode:
# INSERTION-SORT(A)
#     for i = 1 to length(A) - 1
#         key = A[i]
#         j = i - 1
#         while j >= 0 and A[j] > key
#             A[j+1] = A[j]
#             j = j - 1
#         A[j+1] = key
#
#
# Time Complexity: Best O(n), Average O(n^2), Worst O(n^2)

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        temp = arr[j]
        while j>0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -=1
        arr[j] = temp
    return arr

arr = [3,4,5,6,7,5,4,3,5,2,3,2,2]
print(insertion_sort(arr))
