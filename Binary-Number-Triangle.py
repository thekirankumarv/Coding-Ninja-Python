# Problem statement: Binary-Number-Triangle
# Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the N-Binary Number Triangle.

# Example:
# Input: ‘N’ = 3
# Output: 
# 1
# 0 1
# 1 0 1

# Constraints:
# 1 <= N <= 20
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# 1
# 0 1
# 1 0 1

# Sample Input 2:
# 4
# Sample Output 2:
# 1
# 0 1
# 1 0 1
# 0 1 0 1

# Sample Input 3:
# 6
# Sample Output 3:
# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 
# 0 1 0 1 0 1 

# Solution:
def nBinaryTriangle(n: int) -> None:
    if 1 <= n <= 20:
        for i in range(n):
            sequence = 1 if i % 2 == 0 else 0
            for j in range(i + 1):
                print(sequence, end=" ")
                sequence = 1 - sequence
            print()
    else:
        print("Please enter a number between 1 and 20.")

# Test cases
nBinaryTriangle(3)
nBinaryTriangle(4)
nBinaryTriangle(6)
