n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter roll numbers separated by spaces: ").split()))

seen = set()
result = []

for num in nums:
    if num not in seen:
        result.append(num)
        seen.add(num)

print("List without duplicates:", result)


