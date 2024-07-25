# Problem statement: Alpha Triangle
# Sam is researching on Alpha-Triangles. So, he needs to create them for different integers ‘N’.
#
# An Alpha-Triangle is represented by the triangular pattern of alphabets in reverse order.
#
# For every value of ‘N’, help Sam to print the corresponding Alpha-Triangle.
#
# Example:
# Input: ‘N’ = 3
#
# Output:
# C
# C B
# C B A
#
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 25
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
# C
# C B
# C B A
# Sample Input 2 :
# 1
# Sample Output 2 :
# A
#
# Solution:

def alphaTriangle(n: int) -> None:
    if 1 <= n <= 25:
        for i in range(n):
            # Start with the highest character for each row
            p = 64 + n
            for j in range(i + 1):
                print(chr(p), end=" ")
                p -= 1
            print()
    else:
        print("Please enter a number between 1 and 25.")

# Test cases
alphaTriangle(3)
alphaTriangle(1)
alphaTriangle(4)
