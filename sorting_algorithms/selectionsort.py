# selection sort
# Time Complexity: O(n^2) for all cases
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp

arr = [3,4,5,6,7,5,4,3,5,2,3,2,2]
selection_sort(arr)
print(arr)
