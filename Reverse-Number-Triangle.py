# Problem statement: Reverse-Number-Triangle
# Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the Reverse N-Number Triangle.

# Example:
# Input: ‘N’ = 3
# Output: 
# 1 2 3
# 1 2
# 1

# Constraints:
# 1 <= N <= 20
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# 1 2 3
# 1 2
# 1

# Sample Input 2:
# 4
# Sample Output 2:
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Sample Input 3:
# 7
# Sample Output 3:
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Solution:
def reverseNumberTriangle(n: int) -> None:
    if 1 <= n <= 20:
        for i in range(n):
            p = 1
            for j in range(i, n):
                print(p, end=" ")
                p += 1
            print()
    else:
        print("Please enter a number between 1 and 20.")

# Test cases
reverseNumberTriangle(3)
reverseNumberTriangle(4)
reverseNumberTriangle(7)
