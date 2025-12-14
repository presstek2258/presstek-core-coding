# counting sort
# stable sorting algorithm
# in the parameters 
# k is the range of values
# Time Complexity: O(n + k) for all cases
def counting_sort(arr, k):
    
    # start with a count array of zeros
    count_arr = [0] * (k+1)
    output_arr = [0] * len(arr)

    # count the number of occurences of each element
    for i in range(len(arr)):
        count_arr[arr[i]] += 1

    # use the occurences to get the starting 
    # index for each element
    for i in range(1,k+1):
        count_arr[i] += count_arr[i-1]

    # populate the output array so that its sorted
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -=1

    return output_arr


arr = [3,4,5,6,7,5,4,3,5,2,3,2,2]
print(counting_sort(arr, 7))
