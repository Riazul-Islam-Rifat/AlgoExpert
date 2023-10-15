def countInversions(arr):
  if len(arr)<=1: # This is the base case. Single element --> the count inversion is 0
    return 0
  # When there are multiple elements we start dividing and conquering to find the count inversion
  midPoint = (0+len(arr))//2
  leftArr = arr[0:midPoint]
  rightArr = arr[midPoint:len(arr)]

  print('The left array is -- ',leftArr)
  leftArrInversion = countInversions(leftArr)
  print('Inversion value for left array -- ', leftArrInversion)
  print('The right array is -- ',rightArr)
  rightArrInversion = countInversions(rightArr)
  print('Inversion value for right array -- ', rightArrInversion)

  inversion = 0
  print('The initial non merged inversion value is -- ', inversion)
  i=j=k=0
  while i<len(leftArr) and j<len(rightArr):
    if leftArr[i]<=rightArr[j]:
      arr[k]=leftArr[i]
      i+=1
      k+=1
    elif leftArr[i]>rightArr[j]:
      arr[k]=rightArr[j]
      j+=1
      k+=1
      inversion+= len(leftArr)-i


  while i<len(leftArr):
    arr[k]=leftArr[i]
    i+=1
    k+=1
  while j<len(rightArr):
    arr[k]=rightArr[j]
    k+=1
    j+=1


  print('The final inversion value is  -- ', inversion)

  return leftArrInversion+rightArrInversion+inversion

