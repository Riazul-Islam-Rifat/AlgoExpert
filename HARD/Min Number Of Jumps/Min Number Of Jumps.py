def minNumberOfJumps(array):
    jumps = 0
    left=right= 0

    while right<len(array)-1:
        maxDistance = 0

        for i in range(left,right+1):
            maxDistance = max(maxDistance,array[i]+i)

        left = right+1
        right = maxDistance

        jumps+=1

    return jumps