class MinMaxStack:
    def __init__(self):
        # To track the minimum and maximum number of the stack
        self.MinMax = []
        # The stack
        self.stack = []

    def peek(self):
        # Return the last pushed element || the last element
        return self.stack[-1]
        # return self.stack[len(self.stack)-1]

    def pop(self):
        # pop out the last element
        # When we pop an element we pop out the min max correspond to this element.
        self.MinMax.pop()
        return self.stack.pop()

    def push(self, number):
        New_MinMax = {'min': number, 'max': number}
        if len(self.MinMax):
            last_MinMax = self.MinMax[-1]
            New_MinMax['min'] = min(last_MinMax['min'], number)
            New_MinMax['max'] = max(last_MinMax['max'], number)

        self.MinMax.append(New_MinMax)
        self.stack.append(number)

    def getMin(self):
        return self.MinMax[-1]['min']

    def getMax(self):
        return self.MinMax[-1]['max']