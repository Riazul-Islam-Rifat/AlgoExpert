def waterArea(heights):
    if len(heights)==0:
        return 0

    leftIdx = 0
    rightIdx = len(heights)-1
    leftMax = heights[leftIdx]
    rightMax = heights[rightIdx]
    water = 0

    while leftIdx < rightIdx:
        if heights[leftIdx] < heights[rightIdx]:
            leftIdx+=1
            leftMax = max(leftMax,heights[leftIdx])
            water+= leftMax - heights[leftIdx]

        else:
            rightIdx-=1
            rightMax = max(rightMax,heights[rightIdx])
            water+= rightMax - heights[rightIdx]

    return water

    # More intuitive solution:
    # Find leftMax(height) for each index in a list.
    # Find rightMax(height) for each index [In reverse order] in a list.
    # Take the min of leftMax and rightMax for each index in another list.
    # If the given height is smaller than the min then do min-height else 0 and store in a list for each index.
    # Return the sum of the prev list.