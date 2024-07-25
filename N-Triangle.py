# Problem statement: N-Triangle
# Sam is making a Triangular painting for a maths project.
# An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers starting from 1.
# For every value of ‘N’, help Sam to print the corresponding N-dimensional Triangle.

# Example:
# Input: ‘N’ = 3
# Output: 
# 1
# 1 2 
# 1 2 3

# Constraints:
# 1 <= N <= 25
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# 1
# 1 2 
# 1 2 3

# Sample Input 2:
# 1
# Sample Output 2:
# 1

# Solution:
def nTriangle(n: int) -> None:
    if 1 <= n <= 25:
        for i in range(n):
            p = 1
            for j in range(i + 1):
                print(p, end=" ")
                p += 1
            print()
    else:
        print("Please enter a number between 1 and 25.")

# Test cases
nTriangle(3)
nTriangle(1)
nTriangle(4)
