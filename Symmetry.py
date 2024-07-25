# Problem statement: Symmetry
# Sam is curious about symmetric patterns, so he decided to create one.
#
# For every value of ‘N’, return the symmetry as shown in the example.
#
# Example:
# Input: ‘N’ = 3
#
# Output:
# *         *
# * *     * *
# * * * * * *
# * *     * *
# *         *
#
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 25
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
# *         *
# * *     * *
# * * * * * *
# * *     * *
# *         *
# Sample Input 2 :
# 1
# Sample Output 2 :
# *
#
# Solution:

def symmetry(n: int) -> None:
    if 1 <= n <= 25:
        # Upper part of the symmetry including the middle row
        for i in range(n):
            # Print the left stars
            for j in range(i + 1):
                print("*", end=" ")
            # Print the spaces in the middle
            for j in range((n - i - 1) * 2):
                print(" ", end=" ")
            # Print the right stars
            for j in range(i + 1):
                print("*", end=" ")
            print()

        # Lower part of the symmetry (excluding the middle row)
        for i in range(n - 1):
            # Print the left stars
            for j in range(n - i - 1):
                print("*", end=" ")
            # Print the spaces in the middle
            for j in range(i * 2 + 2):
                print(" ", end=" ")
            # Print the right stars
            for j in range(n - i - 1):
                print("*", end=" ")
            print()
    else:
        print("Please enter a number between 1 and 25.")

# Test cases
symmetry(3)
symmetry(1)
symmetry(4)
