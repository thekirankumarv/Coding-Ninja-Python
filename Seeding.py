# Problem statement:  Seeding
# Sam is planting trees on the upper half region (separated by the left diagonal) of the square shared field.
# For every value of ‘N’, print the field if the trees are represented by ‘*’.

# Example:
# Input: ‘N’ = 3
# Output: 
# * * *
# * *
# *

# Constraints:
# 1 <= T <= 10
# 1 <= N <= 25
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# * * *
# * *
# *

# Sample Input 2:
# 1
# Sample Output 2:
# *

# Sample Input 3:
# 4
# Sample Output 3:
# * * * *
# * * *
# * *
# *

# Solution:
def seeding(n: int) -> None:
    if 1 <= n <= 25:
        for i in range(n):
            for j in range(i, n):
                print("*", end=" ")
            print()
    else:
        print("Please enter a number between 1 and 25.")

# Test cases
seeding(3)
seeding(1)
seeding(4)
