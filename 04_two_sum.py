# Problem 4: Two Sum Using a Hash Map
# Find two indices whose values add up to the target.
# The problem guarantees exactly one valid answer.

n = int(input("Enter number of elements: "))
prices = list(map(int, input("Enter prices separated by spaces: ").split()))
target = int(input("Enter target amount: "))

seen = {}
found = False

for i in range(n):
    needed = target - prices[i]

    if needed in seen:
        print("Indices:", [seen[needed], i])
        found = True
        break

    seen[prices[i]] = i

if not found:
    print("No valid pair found.")

# Time Complexity: O(n) average
# Space Complexity: O(n)
