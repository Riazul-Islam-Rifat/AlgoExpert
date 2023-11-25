def dijkstrasAlgorithm(start, edges):
    visited = set()  # Track the visited nodes
    pathCost = [float('inf')] * len(edges)  # Initially all nodes distance is infinity
    pathCost[start] = 0  # As source node has a 0 distance from it.

    for i in range(len(edges)):
        # while len(visited)!=len(edges):
        nodeToVisit, nodeDistance = getNode(pathCost, visited)  # Get which node we need to visit with it's distance

        if nodeDistance == float(
                'inf'):  # If we get a min of infinity that means there is a disconnected graph so we terminate
            break

        visited.add(nodeToVisit)  # Mark nodeToVisit as visited

        # Now visit the children
        for edge in edges[nodeToVisit]:
            destination, destinationDistance = edge  # child and it's distance
            # If we already have visited the destination then we skip it as it has the min distance already
            if destination in visited:
                continue

            newDestinationDistance = destinationDistance + nodeDistance
            curDestinationDistance = pathCost[destination]

            if newDestinationDistance < curDestinationDistance:
                pathCost[destination] = newDestinationDistance
    print(list(map(lambda x: -1 if x == float('inf') else x, pathCost)))
    return list(map(lambda x: -1 if x == float('inf') else x, pathCost))


def getNode(pathCost, visited):
    nodeToVisit = -1
    nodeDistance = float('inf')

    for node in range(len(pathCost)):
        if node in visited:
            continue
        if pathCost[node] < nodeDistance:
            nodeDistance = pathCost[node]
            nodeToVisit = node

    return nodeToVisit, nodeDistance


