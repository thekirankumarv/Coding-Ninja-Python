# Problem statement: N-Star-Triangle
# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Triangle.

# Example:
# Input: ‘N’ = 3
# Output: 
#   *
#  ***
# *****

# Constraints:
# 1 <= N <= 20
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
#   *
#  ***
# *****

# Explanation Of Sample Input 1:
# The first row contains two spaces, followed by a star.
# The second row contains one space, followed by three stars.
# The third row contains five stars.

# Sample Input 2:
# 1
# Sample Output 2:
# *

# Solution:
def nStarTriangle(n: int) -> None:
    if 1 <= n <= 20:
        for i in range(n):
            for j in range(i, n-1):
                print(" ", end="")
            for j in range(i):
                print("*", end="")
            for j in range(i + 1):
                print("*", end="")
            print()
    else:
        print("Please enter a number between 1 and 20.")

# Test cases
nStarTriangle(3)
nStarTriangle(1)
nStarTriangle(5)
