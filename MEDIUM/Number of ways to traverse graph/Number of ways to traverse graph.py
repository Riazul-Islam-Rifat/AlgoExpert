# Time complexity:
# O(height*width)

# Space complexity:
# O(height*width)

# Optimal Solution
def numberOfWaysToTraverseGraph(width, height):
    ways = [[0 for item in range(0, width)] for i in range(0, height)]
    # Assuming 0 indexed 2D array
    for heightIndex in range(len(ways)):
        for widthIndex in range(len(ways[heightIndex])):
            if heightIndex == 0 or widthIndex == 0:
                ways[heightIndex][widthIndex] = 1  # Left and Top border = 1

            else:
                # Current Square Value = left square value + above square value
                ways[heightIndex][widthIndex] = ways[heightIndex][widthIndex - 1] + ways[heightIndex - 1][widthIndex]

    return ways[height - 1][width - 1]


# Non-Optimal solution
# recursive solution
# Time complexity:O(2^(height+width)) --> as 2 cases (left&right) so base 2. We can reach to a base case
# with at most height+width calls.
# Space complexity: O(height+width) --> for recursive call stacks
def numberOfWaysToTraverseGraph(width, height):

    # Base Case :
    if width ==1 or height ==1:
        return 1 # left and top border == 1

    return numberOfWaysToTraverseGraph(width, height-1) + numberOfWaysToTraverseGraph(width-1, height)