def reversePolishNotation(tokens):
    # Store the operators, operands and results
    stack = []
    for item in tokens:
        if item == '+':
            res = int(stack.pop()) + int(stack.pop())
            # put the result in the stack
            stack.append(res)

        elif item == '-':
            # --> 50 7 -  the stack is [50,7]. We need to do 50 - 7. First pop out 7 then substract it from 50
            firstPopped = int(stack.pop())
            res = int(stack.pop()) - firstPopped
            # put the result in the stack
            stack.append(res)

        elif item == '*':
            res = int(stack.pop()) * int(stack.pop())
            # put the result in the stack
            stack.append(res)

        elif item == '/':
            denominator = int(stack.pop())
            res = int(int(stack.pop()) / denominator)
            # put the result in the stack
            stack.append(res)
        else:
            stack.append(item)

    # Return the final result
    return int(stack.pop())