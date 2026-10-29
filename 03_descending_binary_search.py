# Problem 3: Binary Search in a Descending Array
# Find the index of the target in a distinct array sorted high to low.
# Print -1 if the target is not present.

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter numbers in descending order: ").split()))
target = int(input("Enter target: "))

left = 0
right = n - 1
result = -1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        result = mid
        break
    elif target < nums[mid]:
        left = mid + 1
    else:
        right = mid - 1

print("Index:", result)

# Time Complexity: O(log n)
# Extra Space Complexity: O(1)
