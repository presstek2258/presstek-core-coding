# fibonacci series without dynamic programming
# dynamic programming: memoization
#
# Time complexity: T(n) = O(2^n)
def fib(n):
    if n <=1:
        return 1
    return fib(n-1) + fib(n-2)

# with memoization:
# bottom up memoization storage
# Time complexity: T(n) = O(n)
# better space complexity (use this algorithm)
def fib_memo(n):
    if n <=1:
        return 1

    arr = [0] * (n+1)
    arr[0] = 1
    arr[1] = 1

    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]


# recursive and with memoization
# top down memoization storage
# Time complexity: T(n) = O(n)
def fib_rec_memo_helper(n):
    memo = [0] * (n+1)
    return fib_rec_memo(n, memo)

def fib_rec_memo(n, memo):
    if n<=1:
        return 1
    elif memo[n] != 0:
        return memo[n]
    else:
        return fib_rec_memo(n-1,memo) + fib_rec_memo(n-2,memo)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print()

print(fib_rec_memo_helper(0))
print(fib_rec_memo_helper(1))
print(fib_rec_memo_helper(2))
print(fib_rec_memo_helper(3))
print(fib_rec_memo_helper(4))
print(fib_rec_memo_helper(5))
print(fib_rec_memo_helper(6))
print()

print(fib_memo(0))
print(fib_memo(1))
print(fib_memo(2))
print(fib_memo(3))
print(fib_memo(4))
print(fib_memo(5))
print(fib_memo(6))
