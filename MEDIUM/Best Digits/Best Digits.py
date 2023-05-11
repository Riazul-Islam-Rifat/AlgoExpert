def bestDigits(number, numDigits):
    # Store the numbers in the stacks and pop when needed
    stack = []
    for num in number:
        while len(stack) and numDigits > 0 and num > stack[-1]:
            numDigits -= 1
            stack.pop()
        stack.append(num)

    # When the numbers are in descending order. Like 987654321
    while numDigits:
        numDigits -= 1
        stack.pop()

    return ''.join(stack)