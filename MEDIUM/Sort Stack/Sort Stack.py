def sortStack(stack):
    # If stack is empty then return it
    if len(stack)==0:
        return stack
    # Otherwise pop the last element
    top = stack.pop()
    # Recursive call for rest of the elements as we need to make the stack empty and then insert
    sortStack(stack)
    # When the stack is empty the insertSortedValue function is called
    # Start insertion with the last popped value
    insertSortedValue(stack,top)

    #return the sorted stack
    return stack

def insertSortedValue(stack,val):
    if len(stack)==0 or val>=stack[-1]:
        stack.append(val)
        # Return as base case
        return

    # Otherwise pop the top element and then insert the val and after that insert the top element again
    top = stack.pop()
    insertSortedValue(stack,val)
    stack.append(top)