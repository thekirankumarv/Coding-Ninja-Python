# Problem statement: Star-Diamond
# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.

# Example:
# Input: ‘N’ = 3
# Output: 
#   *
#  ***
# *****
# *****
#  ***
#   *

# Constraints:
# 1 <= N <= 20
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
#   *
#  ***
# *****
# *****
#  ***
#   * 

# Sample Input 2:
# 1
# Sample Output 2:
# *
# *

# Solution:
def nStarDiamond(n: int) -> None:
    if 1 <= n <= 20:
        # Top half of the diamond
        for i in range(n):
            for j in range(i, n-1):
                print(" ", end="")
            for j in range(i):
                print("*", end="")
            for j in range(i + 1):
                print("*", end="")
            print()
        
        # Bottom half of the diamond
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
nStarDiamond(3)
nStarDiamond(1)
nStarDiamond(5)
