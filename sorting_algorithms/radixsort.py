# radix sort used any other stable sorting algorithm
# both counting sort and bucket sort are stable
# typically counting sort is used
#
# Time Complexity: O(n * d) where d is the number of digits

# exp picks which digits exp=1 for ones, exp=10 for tens...
# use (arr[i]//exp)%10 to get the index for the digit
#
# example: with "170"
# exp = 1: (170//1)%10 = 170%10 = 0 (ones digit)
# exp = 10: (170//10)%10 = 17%10 = 7 (tens digit)
# exp = 100: (170//100)%10 = 1%10 = 1 (hundreds digit)
def counting_sort(arr, exp):
    k = 9 # range from 0 to 9 for a digit
    count_arr = [0] * (k+1)
    output_arr = [0] * len(arr)

    for i in range(len(arr)):
        count_arr[(arr[i]//exp)%10] += 1
    for i in range(1,k+1):
        count_arr[i] += count_arr[i-1]
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[(arr[i]//exp)%10]-1] = arr[i]
        count_arr[(arr[i]//exp)%10] -=1
    return output_arr

# radix sort implementation
# basically applies counting sort to words digit by digit
# d is the number of digits of the max element
# exp is the exponent
def radix_sort_counting(arr):
    if len(arr) < 1:
        return None
    d = len(str(max(arr)))

    exp = 1
    for i in range(d):
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr


arr = [170, 45, 75, 90, 802, 24, 2, 66, 123, 34, 280]
print(radix_sort_counting(arr))
