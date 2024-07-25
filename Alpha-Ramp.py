# Problem statement: Alpha-Ramp
# Sam is curious about Alpha-Ramp, so he decided to create Alpha-Ramp of different sizes.
#
# An Alpha-Ramp is represented by a triangle, where alphabets are filled from the top in order.
#
# For every value of ‘N’, help Sam to return the corresponding Alpha-Ramp.
#
# Example:
# Input: ‘N’ = 3
#
# Output:
# A
# B B
# C C C
#
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 25
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
# A
# B B
# C C C
# Sample Input 2 :
# 1
# Sample Output 2 :
# A
# Sample Input 3 :
# 4
# Sample Output 3 :
# A
# B B
# C C C
# D D D D
#
# Solution:

def alphaRamp(n: int) -> None:
    if 1 <= n <= 25:
        p = 65
        for i in range(n):
            for j in range(i+1):
                print(chr(p), end=" ")
            p += 1
            print()
    else:
        print("Please enter a number between 1 and 25.")

# Test cases
alphaRamp(3)
alphaRamp(1)
alphaRamp(4)
