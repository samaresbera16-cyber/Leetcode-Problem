# Problem 2: Remove Duplicates Using a Hash Set
# Remove duplicates while preserving the order of first occurrence.

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter roll numbers separated by spaces: ").split()))

seen = set()
result = []

for num in nums:
    if num not in seen:
        result.append(num)
        seen.add(num)

print("List without duplicates:", result)

# Time Complexity: O(n) average
# Space Complexity: O(n)
