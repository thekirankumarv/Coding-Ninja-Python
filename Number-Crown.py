# Problem statement: Number-Crown
# Aryan and his friends are very fond of the pattern. They want to make the Reverse N-Number Crown for a given integer 'N'.

# Example:
# Input: ‘N’ = 3
# Output:
# 1         1
# 1 2     2 1
# 1 2 3 3 2 1

# Constraints:
# 1 <= N <= 20
# Time Limit: 1 sec

# Sample Input 1:
# 3
# Sample Output 1:
# 1         1
# 1 2     2 1
# 1 2 3 3 2 1

# Sample Input 2:
# 4
# Sample Output 2:
# 1             1
# 1 2         2 1
# 1 2 3     3 2 1
# 1 2 3 4 4 3 2 1

# Sample Input 3:
# 7
# Sample Output 3:
# 1                         1
# 1 2                     2 1
# 1 2 3                 3 2 1
# 1 2 3 4             4 3 2 1
# 1 2 3 4 5         5 4 3 2 1
# 1 2 3 4 5 6     6 5 4 3 2 1
# 1 2 3 4 5 6 7 7 6 5 4 3 2 1

# Solution:
def numberCrown(n: int) -> None:
    if 1 <= n <= 20:
        for i in range(n):
            # Print the first half of the pattern
            for j in range(i + 1):
                print(j + 1, end=" ")
            
            # Print spaces
            for j in range(2 * (n - i - 1)):
                print(" ", end=" ")
            
            # Print the second half of the pattern
            for j in range(i + 1, 0, -1):
                print(j, end=" ")
            
            print()
    else:
        print("Please enter a number between 1 and 20.")

# Test cases
numberCrown(3)
numberCrown(4)
numberCrown(7)
