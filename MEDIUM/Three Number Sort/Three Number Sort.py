def threeNumberSort(array,order):
  firstVal = order[0]
  lastVal = order[-1]

  firstIdx = 0
  # Sort out the first part
  for item in range(len(array)):
    if array[item] == firstVal:
      array[item],array[firstIdx] = array[firstIdx], array[item]
      firstIdx+=1
  # Sort out the last part and the middle part is automatically sorted
  lastIdx = len(array) - 1
  for item in range(len(array)-1,-1,-1):
    if array[item] == lastVal:
      array[item],array[lastIdx] = array[lastIdx], array[item]
      lastIdx-=1

  return array
