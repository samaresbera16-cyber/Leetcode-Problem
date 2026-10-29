# Problem 1: Single Number
# Every number appears twice except one. Find the number that appears once.

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))

result = 0

for num in nums:
    result = result ^ num

print("Single number:", result)

# Time Complexity: O(n)
# Extra Space Complexity: O(1), excluding the input list
