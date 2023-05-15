def nextGreaterElement(array):
  # Resulting array
  result = [-1]*len(array)
  # Here the indices will be stored
  stack = []
  # We are looping upto 2n as the given array is curcular. In the first half the array will be traversed from left to right:
  # In the 2nd half the array will be traversed in circular way
  for idx in range(2*len(array)):
    circularIdx = idx % len(array) # When idx will be greater then len(array), circularIdx will start from 0 again.
    while len(stack) and array[stack[-1]] < array[circularIdx]: # The right element is greater
      result[stack[-1]] = array[circularIdx]
      stack.pop()
    stack.append(circularIdx)

  return result
