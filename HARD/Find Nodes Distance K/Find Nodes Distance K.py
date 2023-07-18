from collections import deque


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    # Find the parent node of each node
    parentNodes = {}
    findParents(tree, parentNodes)

    # Find the node object of the target value
    targetNode = findTargetNode(tree, target, parentNodes)

    # Find the k distanced node and return
    return kDistancedNodes(targetNode, parentNodes, k)


# Finding the parent nodes
def findParents(node, parentNodes, parent=None):  # Optional parameter parent. For root node parent will be None
    if node is not None:
        parentNodes[node.value] = parent
        findParents(node.left, parentNodes, node)
        findParents(node.right, parentNodes, node)
    else:
        # If the node is None we don't find it's parent node
        pass


# Finding the node object of the target node
def findTargetNode(tree, target, parentNodes):
    if target == tree.value:
        return tree
    parentOfTarget = parentNodes[target]
    # So the target node will be the left or right child of the parentOfTarget
    if parentOfTarget.left and parentOfTarget.left.value == target:
        return parentOfTarget.left
    return parentOfTarget.right


# Find the output
def kDistancedNodes(node, parents, k):
    tracker = deque([(node, 0)])  # The target node and it's distance from it is 0
    seen = {node.value}  # To avoid infinite loop

    # BFS. Pop --> Logic --> Add child to the queue
    while len(tracker):
        currentNode, distanceFromTarget = tracker.pop()

        # Logic
        if distanceFromTarget == k:
            # All the nodes in the queue will be added to the answer as all of them have k distance
            nodes = [currentNode.value]
            for node, _ in tracker:
                nodes.append(node.value)
            return nodes

        # Add connected nodes to the queue
        connectedNodes = [currentNode.left, currentNode.right, parents[currentNode.value]]
        for node in connectedNodes:
            if node is None:
                continue
            if node.value in seen:
                continue

            seen.add(node.value)
            tracker.appendleft((node, distanceFromTarget + 1))

    return []












