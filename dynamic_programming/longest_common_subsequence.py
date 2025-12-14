# longest common subsequence
# note: doesn't need to be consecutive 
# Time complexity: Theta(m*n)
#
# X and Y are sequences
# n and m are there lengths
# returns the length of the longest common sequence

def LCS_LENGTH(X, Y, m, n):
    # Create a 2D table c with dimensions (m+1) x (n+1)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Fill the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # Note: strings are 0-indexed
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = c[i][j - 1]
    
    return c[m][n]

X = "ABCB"
Y = "BDCAB"
m = len(X)
n = len(Y)
print(LCS_LENGTH(X, Y, m, n))
