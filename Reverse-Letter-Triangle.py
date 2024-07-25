# Problem statement: everse Letter Triangle
# Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Reverse Letter Triangle.
#
# You must print a matrix corresponding to the given Reverse Letter Triangle.
#
# Example:
# Input: ‘N’ = 3
#
# Output:
#
# A B C
# A B
# A
#
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 20
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
# A B C
# A B
# A
# Sample Input 2 :
# 4
# Sample Output 2 :
# A B C D
# A B C
# A B
# A
# Sample Input 3 :
# 7
# Sample Output 3 :
# A B C D E F G
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A
#
# Solution:

def nLetterTriangle(n: int) -> None:
    if 1 <= n <= 20:
        for i in range(n):
            p = 65
            for j in range(n - i):
                print(chr(p), end=" ")
                p += 1
            print()
    else:
        print("Please enter a number between 1 and 20.")

# Test cases
nLetterTriangle(3)
nLetterTriangle(4)
nLetterTriangle(7)
