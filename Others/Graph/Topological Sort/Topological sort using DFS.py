# Time complexity: O(V+E) V-->Vertex  E--> Edge

graph = [[],[2,4],[4,5,3],[],[6,5],[3],[5],[8],[]]
# graph = [[], [2], [], [1], [5], []]
# graph = [[], [2], [3], [], [3,5], [6],[4]]
# We can start from any node
# We have to track if there is any cycle or not. If cycle exists then topological sorting is impossible
cycleTracker = [0] * len(graph)  # 0 --> Not visited, 1--> visiting, 2--> completely visited
topologicalOrder = [False]


def dfs(node, topologicalOrder, cycleTracker):
    cycleTracker[node] = 1  # Make the  node in visiting state
    # Now traverse the neighbour node
    neighbors = graph[node]
    for neighbor in neighbors:
        if cycleTracker[neighbor] == 1:
            topologicalOrder[0] = True  # As we encounter a visiting node. Encountering a visiting node means a child goes back to it's parent and make a cycle
        elif cycleTracker[neighbor] == 0:
            dfs(neighbor, topologicalOrder, cycleTracker)

    cycleTracker[node] = 2  # When the node is completely traversed
    topologicalOrder.append(node)



for node in range(1, len(graph)):  # For this problem we are assuming that no 0 node exists
    if cycleTracker[node] == 2 or cycleTracker == 1:
        continue
    dfs(node, topologicalOrder, cycleTracker)


if topologicalOrder[0] == True:
    print('IMPOSSIBLE')

else:
    finalOrder = topologicalOrder[1::]
    print(finalOrder[len(finalOrder)::-1])



