# the O/1 knapsack problem
#
# greedy algorithm wont always find the answer
# the goal is to maximize the value for a permitted weight
# 
# w is an array of weights
# b is an array of benefits/values
# n is the number of items
# W is the max weight
#
# Time complexity: Theta(n * w)
def knapsack(w, b, n, W):
    # make a DP table to map towards the answer
    B = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w_capacity in range(W + 1):
            # if the current items weight fits in the knapsack
            if w[i - 1] <= w_capacity:
                # take the max of the 2 possible outcomes:
                bval1 = b[i-1] + B[i-1][w_capacity-w[i-1]]
                bval2 = B[i-1][w_capacity]
                B[i][w_capacity] = max(bval1, bval2)

                # or:

                # bval1 = b[i - 1] + B[i - 1][w_capacity - w[i - 1]]
                # bval2 = B[i - 1][w_capacity]
                # if bval1 > bval2:
                #     B[i][w_capacity] = bval1
                # else:
                #     B[i][w_capacity] = bval2
            else:
                # Item doesn't fit, so we can't include it
                B[i][w_capacity] = B[i - 1][w_capacity]
    return B[n][W]



# TESTING:
# same example as from slides
# items(weight, benefit): (2,3),(3,4),(4,5),(5,6)
# max weight = 5
# expected result = 7

weights = [2,3,4,5]
benefits = [3,4,5,6]
n = len(weights)
W = 5

result = knapsack(weights, benefits, n, W)
print(f"Maximum value: {result}")

