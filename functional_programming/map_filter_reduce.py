# basic lambda usage
value = 5
func = lambda x: 2*x
print(f"{value = }")
print(f"{func(value) = }\n")

# map filter and reduce
# these are used to efficiently apply functions 
# to arrays / lists
#
# the functions return an iterable -> use list()

arr = [1,2,3,4,5]
print(f"{arr = }\n")

# map applies a function to every element
# return a list
print(f"{list(map(lambda x: 2*x, arr)) = }")
print(f"{list(map(lambda x: x-1, arr)) = }\n")

# applies a condition to every element
# drops those that dont meet the condition
# returns a list
print(f"{list(filter(lambda x: x>3, arr)) = }")
print(f"{list(filter(lambda x: x%2==0, arr)) = }\n")

# applies a function to every element sequentially
# at each step x is the current value
# at each step y is the next value
# returns a single value
from functools import reduce
print(f"{reduce(lambda x,y: x+y, arr) = }")
print(f"{reduce(lambda x,y: x*y, arr) = }\n")



