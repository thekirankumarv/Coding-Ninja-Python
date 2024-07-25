# Problem statement: Alpha Hill
# Sam is curious about Alpha-Hills, so he decided to create Alpha-Hills of different sizes.
#
# An Alpha-Hill is represented by a triangle, where alphabets are filled in palindromic order.
#
# For every value of ‘N’, help Sam to return the corresponding Alpha-Hill.
#
# Example:
# Input: ‘N’ = 3
#
# Output:
#     A
#   A B A
# A B C B A
#
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 25
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
#     A
#   A B A
# A B C B A
# Sample Input 2 :
# 1
# Sample Output 2 :
# A
#
# Solution:

def alphaHill(n: int) -> None:
    if 1 <= n <= 25:
        for i in range(n):
            # Print leading spaces
            for j in range(n - i - 1):
                print(" ", end=" ")
            # Print ascending part of the alphabet
            p = 65
            for j in range(i + 1):
                print(chr(p), end=" ")
                p += 1
            # Print descending part of the alphabet
            p -= 2
            for j in range(i):
                print(chr(p), end=" ")
                p -= 1
            print()
    else:
        print("Please enter a number between 1 and 25.")

# Test cases
alphaHill(3)
alphaHill(1)
alphaHill(4)
