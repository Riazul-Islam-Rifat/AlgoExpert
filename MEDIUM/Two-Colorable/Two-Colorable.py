def twoColorable(edges):
    # Connected nodes will have different colors and we are allowed to use only two colors
    # For instance one color in True another color is False
    # Initially no color is assigned to any of the nodes
    colors = [None for _ in range(len(edges))]  # Len of edge is the total numberof nodes in the graph
    colors[0] = True  # Assigning a color to the node 0
    # In stack we will store the nodes those need to be visited
    stack = [0]  # Initially we want to visit the first node

    while len(stack):
        node = stack.pop()  # Node we want to visit
        for neighbors in edges[node]:
            if colors[neighbors] is None:
                colors[neighbors] = not colors[node]
                stack.append(
                    neighbors)  # Color is None, means we haven't visited this node yet so we append it in stack to visit.

            elif colors[neighbors] == colors[node]:
                return False

    return True
