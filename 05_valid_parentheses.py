# Problem 5: Valid Parentheses Using a Stack
# Check whether (), [] and {} are correctly matched and nested.

s = input("Enter the brackets: ")

stack = []
valid = True

for ch in s:
    if ch == '(' or ch == '[' or ch == '{':
        stack.append(ch)
    else:
        if len(stack) == 0:
            valid = False
            break

        top = stack.pop()

        if ch == ')' and top != '(':
            valid = False
            break
        elif ch == ']' and top != '[':
            valid = False
            break
        elif ch == '}' and top != '{':
            valid = False
            break

if len(stack) != 0:
    valid = False

print(valid)

# Time Complexity: O(n)
# Space Complexity: O(n)
