
def getPermutations(array):
  permutations = []
  permHelper(0,array,permutations)
  return permutations

def permHelper(i,arr,perms):
  if i == len(arr)-1:
    perms.append(arr[:])
    #print('++++++++++++++++++++++++++++++')
  else:
    for j in range(i,len(arr)):
      #print('j-- ', j)
      #print('i-- ',i)
      arr[i],arr[j]=arr[j],arr[i]
      #print('swapped-- ', arr)
      permHelper(i+1,arr,perms)
      arr[i],arr[j]=arr[j],arr[i]
      #print('reswapped-- ', arr)