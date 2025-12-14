# merge sort
# Time Complexity: O(n log n) for all cases
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    left_arr = [0] * n1
    right_arr = [0] * n2

    for i in range(n1):
        left_arr[i] = arr[left + i]
    for j in range(n2):
        right_arr[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # compares the elements of the arrays halves from left to right and
    # adds the smaller element to arr this is repeated till the left or right
    # array has been fully traversed
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1


    # these while loops add the rest of the elements from the
    # un-traversed parts of the array
    # (this will occur if left and right are different sizes)
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_helper(arr):
    merge_sort(arr, 0, len(arr)-1)

arr = [3,4,5,6,7,5,4,3,5,2,3,2,2]
merge_helper(arr)
print(arr)

