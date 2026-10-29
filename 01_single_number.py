n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))

result = 0

for num in nums:
    result = result ^ num

print("Single number:", result)

