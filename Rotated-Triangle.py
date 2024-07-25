# Problem statement: Rotated-Triangle
# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Rotated Triangle.

# Example:
# Input: ‘N’ = 3
# Output: 
# *
# **
# ***
# **
# *

# Constraints:
# 1 <= N <= 20
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# *
# **
# ***
# **
# *

# Sample Input 2:
# 1
# Sample Output 2:
# *

# Solution:
def nStarRotatedTriangle(n: int) -> None:
    if 1 <= n <= 20:
        # Top half of the triangle
        for i in range(n):
            for j in range(i + 1):
                print("*", end="")
            print()
        
        # Bottom half of the triangle
        for i in range(n - 1):
            for j in range(n - i - 1):
                print("*", end="")
            print()
    else:
        print("Please enter a number between 1 and 20.")

# Test cases
nStarRotatedTriangle(3)
nStarRotatedTriangle(1)
nStarRotatedTriangle(5)
