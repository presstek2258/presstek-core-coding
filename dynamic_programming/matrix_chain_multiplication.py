# dynamic programming:
# optimize matrix chain multiplication order
# p is an array of the matrices dimnesions in the chain
#
# returns a cost table m where m[i][j] is the 
# min multiplications to multiply matrices from i to j
#
# return a split table s which holds the index 
# for the optimal split point
def matrix_chain_order(p):
    n = len(p)-1
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf') # initliaze to infinity

            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s


# matrix multiplication
# A is a pxq matrix
# B is a qxr matrix
#
# Time complexity: Theta(pqr)
def matrix_multiply(A, B):
    # make sure arrays arent empty
    if len(A[0])<1 or len(B[0])<1 or len(A)<1 or len(B)<1:
        print("empty arrays")
        return None

    p = len(A) # A rows
    q = len(A[0]) # A cols
    r = len(B[0]) # B cols

    # make sure B rows and A cols are the same
    if q != len(B):
        print("dimensions dont match")
        return None 
        
    # make a pxr array C
    C = [[0 for _ in range(r)] for _ in range(p)]
    for i in range(p):
        for j in range(r):
            C[i][j] = 0
            for k in range(q):
                C[i][j] += A[i][k] * B[k][j]
    return C

# prints the optimal multiplication chain order 
# to multiply matrices from i to j
def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end="")  # Print matrix A_i
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

def multiply_chain(matrices, s, i, j):
    if i == j:
        return matrices[i]
    else:
        left = multiply_chain(matrices, s, i, s[i][j])
        right = multiply_chain(matrices, s, s[i][j] + 1, j)
        return matrix_multiply(left, right)

def matrix_chain_helper(matrices):
    # make the p array
    p = []
    for matrix in matrices:
        p.append(len(matrix))
    p.append(len(matrices[-1][0]))
    print(f'{p = }')

    # get the cost and split tables
    m,s = matrix_chain_order(p)
    print(f'{m = }')
    print(f'{s = }')

    # print results
    print("Minimum number of scalar multiplications:", m[0][len(matrices)-1])
    print("Optimal parenthesization: ", end="")
    print_optimal_parens(s, 0, len(matrices)-1)
    print()

    # perform the multiplication and return
    result = multiply_chain(matrices, s, 0, len(matrices)-1)
    return result 

    
# TESTING:
# if A is 2x3
# if B is 3x3
# if C is 3x1
# result should be 2x1

A = [[0,1,2],[3,4,6]]
B = [[3,2,1],[3,4,5],[3,3,3]]
C = [[3],[0],[1]]
matrices = [A,B,C]
result = matrix_chain_helper(matrices)
print(f"{result = }")
