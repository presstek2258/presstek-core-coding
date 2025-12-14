# bucket sort
# stable sorting algorithm
# this implementation works for numbers 0 to 1
# n is the number of buckets
# Time Complexity: Best O(n+k), Average O(n+k), Worst O(n^2) 
def bucket_sort(arr, n):
    # make n empty buckets
    buckets = [[] for _ in range(n)]

    # insert the elements into buckets
    for i in range(len(arr)):
        buckets[int(n*arr[i])].append(arr[i])

    # sort each bucket
    for i in range(n):
        insertion_sort(buckets[i]) # any sorting algorithm

    # concatenate the buckets and return
    output_arr = []
    for i in range(n):
        output_arr += buckets[i]
    return output_arr
    

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        temp = arr[j]
        while j>0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -=1
        arr[j] = temp
    return arr


# this implementation works for numbers 0 to 1
arr = [0.3,0.4,0.5,0.6,0.7,0.5,0.4,0.3,0.5,0.2,0.3,0.2,0.2]
# 10 buckets
print(bucket_sort(arr, 10))
