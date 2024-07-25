# Problem statement: Row-Number-Triangle
# Sam is making a Triangular painting for a maths project.
# An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers representing the row number.
# For every value of ‘N’, help Sam to print the corresponding Triangle.

# Example:
# Input: ‘N’ = 3
# Output: 
# 1
# 2 2 
# 3 3 3

# Constraints:
# 1 <= N <= 25
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# 1
# 2 2 
# 3 3 3

# Sample Input 2:
# 1
# Sample Output 2:
# 1

# Solution:
def rowNumberTriangle(n: int) -> None:
    if 1 <= n <= 25:
        for i in range(1, n + 1):
            for j in range(i):
                print(i, end=" ")
            print()
    else:
        print("Please enter a number between 1 and 25.")

# Test cases
rowNumberTriangle(3)
rowNumberTriangle(1)
rowNumberTriangle(4)
