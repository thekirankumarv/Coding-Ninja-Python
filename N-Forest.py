# Problem statement: N-Forest
# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.
# For every value of ‘N’, help Sam to print the corresponding N-dimensional forest.

# Example:
# Input: ‘N’ = 3
# Output: 
# * * *
# * * *
# * * *

# Constraints:
# 1 <= N <= 25
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# * * *
# * * *
# * * *

# Explanation Of Sample Input 1:
# For N = 3, fill all the rows and columns in 3x3 matrix with ‘*’.

# Sample Input 2:
# 1
# Sample Output 2:
# *

# Sample Input 3:
# 4
# Sample Output 3:
# * * * *
# * * * *
# * * * *
# * * * *

# Solution:
def nForest(n: int) -> None:
    if 1 <= n <= 25:
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()
    else:
        print("")

# Test cases
nForest(3)
nForest(1)
nForest(4)
