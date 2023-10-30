import queue
inputFile = open('input.txt','r')
firstLine = inputFile.readline().strip()
numberOfNodes,numberOfEdges = int(firstLine[0]), int(firstLine[-1])
# Make the adjacency list
connections = inputFile.readlines()
adjacencyList = [[] for _ in range(numberOfNodes+1)] # As 1 indexed graph we take 0th list and ignore it
print(connections)
for item in connections:
    connection = item.strip()
    adjacencyList[int(connection[0])].append(int(connection[-1]))
    adjacencyList[int(connection[-1])].append(int(connection[0]))
# print(adjacencyList)

# Now we will run bfs on this adjacency list
# Initially no node is visited, all node's parents are none, node level -1
visited = [False for _ in range(numberOfNodes+1)]
parent = [None for _ in range(numberOfNodes+1)]
nodeLevel = [-1 for _ in range(numberOfNodes+1)]
traverseSequence = []

bfsQueue = queue.Queue()

# We have picked node 1 as our starting/source node
sourceNode = 1
visited[sourceNode] = True # Make the source node visited
nodeLevel[sourceNode] = 0 # Source node's level is 0
# Put this sourceNode in bfsQueue as we need to visit it's child
bfsQueue.put(sourceNode)

while not bfsQueue.empty():
    currentNode = bfsQueue.get()
    traverseSequence.append(currentNode)

    for child in adjacencyList[currentNode]:
        if not visited[child]:
            parent[child] = currentNode
            nodeLevel[child] = nodeLevel[currentNode]+1
            visited[child] = True
            bfsQueue.put(child)

print('The bfs traversal sequence is - ',traverseSequence)

# Now find a path to a particular node. This is where parent list works
# I am  trying for node 5
targetNode = 7
target = targetNode
path = []
while targetNode is not None:
    path.append(str(targetNode))
    targetNode = parent[targetNode]

path.reverse()
print('Time - ',nodeLevel[target])
print('Path to target node ', '-->'.join(path))