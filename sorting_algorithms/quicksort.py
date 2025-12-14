# quicksort psuedocode:
# QUICKSORT(A, left, right)
#     if left < right
#         mid = PARTITION(A, left, right)
#         QUICKSORT(A, left, mid-1)
#         QUICKSORT(A, mid+1, right)
#
# PARTITION(A, left, right)
#     pivot = A[right]
#     i = left
#     for j = left to right-1
#         if A[j] < pivot
#             swap A[i] and A[j]
#             i = i + 1
#     swap A[i] and A[right]
#     return i

# the in class implementation of quicksort
# more memory efficient with memory O(log n)
# use this implementation
# Time Complexity: Best O(n log n), Average O(n log n), Worst O(n^2)
def quick_sort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left 
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quick_helper(arr):
    quick_sort(arr, 0, len(arr)-1)

arr = [3,4,5,6,7,5,4,3,5,2,3,2,2]
quick_helper(arr)
print(arr)
