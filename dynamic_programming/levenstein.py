# Stanford NLP:
# group on Minimum Edit Distance (MED):
# http://www.stanford.edu/class/cs124/lec/med.pdf
# try it out on a few string pairs:
# • spoof/stool
# • podiatrist/pediatrician
# • blaming/conning

# NOTE: this algorithm is being used with a substituion mismatch cost of 2.
# this is atypical. levenstein's algorithm typically uses a mismatch cost 
# of 1 for word comparison. But the psuedocode example uses 2:
# http://www.stanford.edu/class/cs124/lec/med.pdf

# returns a distance (int) based on the number of 
# differences from word1 to word2
# word1 and word2 are strings
def levenstein(word1: str, word2: str) -> int:
    n = len(word1)
    m = len(word2)
    operations = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    # initlize the first row/coloumn
    for i in range(n+1):
        operations[i][0] = i
    for j in range(m+1):
        operations[0][j] = j
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            # substituion cost is zero if the same otherwise 2
            cost = 2
            if (word1[i-1] == word2[j-1]):
                cost = 0

            operations[i][j] = min(operations[i-1][j]+1, # delete
                                    operations[i][j-1]+1, # insert
                                    operations[i-1][j-1]+cost) # substitute
    return operations[n][m]


# TESTING: given test strings
print(f'hello & hell: {levenstein("hello", "hell")}') # should give 1 deletion is less costly
print(f'hello & hella: {levenstein("hello", "hella")}') # should give 2 substituion is more costly

print(f'spoof & stool: {levenstein("spoof", "stool")}')
print(f'podiatrist & pediatrician: {levenstein("podiatrist", "pediatrician")}')
print(f'blaming & conning: {levenstein("blaming", "conning")}')
