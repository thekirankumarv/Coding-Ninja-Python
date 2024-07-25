# Problem statement: Reverse-Star-Triangle
# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the Reverse N-Star Triangle.

# Example:
# Input: ‘N’ = 3
# Output: 
# *****
#  ***
#   *

# Constraints:
# 1 <= N <= 20
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# *****
#  ***
#   *

# Explanation Of Sample Input 1:
# The first row contains five stars.
# The second row contains one space, followed by three stars.
# The third row contains two spaces, followed by a star.

# Sample Input 2:
# 1
# Sample Output 2:
# *

# Solution:
def reverseStarTriangle(n: int) -> None:
    if 1 <= n <= 20:
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            for j in range(i, n):
                print("*", end="")
            for j in range(i, n - 1):
                print("*", end="")
            print()
    else:
        print("Please enter a number between 1 and 20.")

# Test cases
reverseStarTriangle(3)
reverseStarTriangle(1)
reverseStarTriangle(5)
