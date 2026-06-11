def is_balanced(expression):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("{[()]}")) 
print(is_balanced("{[(])}"))  