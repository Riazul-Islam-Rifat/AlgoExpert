numberOfNodes = int(input('Number of nodes- ')) # Includes 0
numberOfEdges = int(input('Number of edges- ')) # Includes 0

graphMatrix  = [[0 for i in range(numberOfNodes+1)] for _ in range(numberOfNodes+1)]
# print(graphMatrix)
# edges = [[1,3,8],[3,2,5],[1,4,2]] # Len will be  number of edges. Take these sub-lists from user rather than hardcoded one
edges = [[1, 5, 6],[6,3,5],[1,3,9],[3,4,7],[4,6,1],[5,6,8],[6,1,6]] # Len will be  number of edges. Take these sub-lists from user rather than hardcoded one
for i in edges:
    nodeFrom = i[0]
    nodeTo = i[1]
    weight = i[2]
    graphMatrix[nodeFrom][nodeTo] = weight

print(graphMatrix)
