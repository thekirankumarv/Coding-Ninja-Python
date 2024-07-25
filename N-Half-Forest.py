# Problem statement: N-Half-Forest
# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.
# An N/2-dimensional forest is represented by the lower triangle of the pattern filled with ‘*’.
# For every value of ‘N’, help Sam to print the corresponding N/2-dimensional forest.

# Example:
# Input: ‘N’ = 3
# Output: 
# * 
# * *
# * * *

# Constraints:
# 1 <= N <= 25
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# * 
# * *
# * * *

# Explanation Of Sample Input 1:
# For N = 3, fill all the rows and columns in the lower triangle of 3x3 matrix with ‘*’.

# Sample Input 2:
# 1
# Sample Output 2:
# * 

# Solution:
def nHalfForest(n: int) -> None:
    if 1 <= n <= 25:
        for i in range(n):
            for j in range(i + 1):
                print("*", end=" ")
            print()
    else:
        print("Invalid")

# Test cases
nHalfForest(3)
nHalfForest(1)
nHalfForest(4)
