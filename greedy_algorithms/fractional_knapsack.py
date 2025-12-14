# the fractional knapsack problem
#
# greedy algorithm will find the answer in all cases
# the goal is the maximize the value for a permitted weight
#
# w is an array of weights
# b is an array of benefits/values
# n is the number of items
# W is the max weight
#
# Time complexity: O(nlogn)
def fractional_knapsack(w, b, n, W):
    # Create list of items with their value-to-weight ratio
    items = []
    for i in range(n):
        ratio = b[i] / w[i] if w[i] != 0 else 0 
        items.append((ratio, w[i], b[i]))
    
    # Sort items from greatest to least ratio
    items.sort(key=lambda x: x[0], reverse=True)
    
    total_value = 0
    remaining_capacity = W
    
    for ratio, weight, value in items:
        if remaining_capacity == 0:
            break
            
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of the item
            total_value += ratio * remaining_capacity
            remaining_capacity = 0
            break
    
    return total_value

# TESTING:
# same example as from slides
# items(weight, benefit): (10,60),(20,100),(30,120)
# max weight = 50
# expected result = 240

weights = [10, 20, 30]
values = [60, 100, 120]
n = len(weights)
W = 20

result = fractional_knapsack(weights, values, n, W)
print(f"Maximum value: {result}")
