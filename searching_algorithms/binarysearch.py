# binary search
# returns the index of the value if it exists
# if it doesn't exists, returns None
#
# Time complexity: O(log n), very efficient

def binary_search(arr, val, left, right):
    if left > right:
        return None
    mid = (left + right)//2
    if val == arr[mid]:
        return mid
    elif val > arr[mid]:
        return binary_search(arr, val, mid+1, right)
    else:
        return binary_search(arr, val, left, mid-1)

def binary_helper(arr, val):
    return binary_search(arr, val, 0 , len(arr)-1)

arr = [1,2,3,5,3,2,34,5]
print(binary_helper(arr,34))
