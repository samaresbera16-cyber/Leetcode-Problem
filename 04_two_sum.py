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


