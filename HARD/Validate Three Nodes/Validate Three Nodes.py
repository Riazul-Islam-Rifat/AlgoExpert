# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Time complexity: o(d) where d is the distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    searchOne = nodeOne
    searchTwo = nodeThree

    # We will search nodeTwo both from nodeOne and nodeThree at the same time
    while True: # Until we break the loop
        foundThreeFromOne = searchOne is nodeThree
        foundOneFromThree = searchTwo is nodeOne
        foundTwo = searchOne is nodeTwo or searchTwo is nodeTwo
        searchFinished = searchOne is None and searchTwo is None

        if foundThreeFromOne or foundOneFromThree or foundTwo or searchFinished:
            break

        if searchOne is not None:
            searchOne =  searchOne.left if nodeTwo.value < searchOne.value else searchOne.right

        if searchTwo is not None:
            searchTwo = searchTwo.left if nodeTwo.value < searchTwo.value else searchTwo.right

    # After breaking the loop
    foundedOneAnother = foundThreeFromOne or foundOneFromThree # In this case return False
    foundedTwo = foundTwo # In this case check the descendant

    if not foundedTwo or foundedOneAnother:
        return False

    target = nodeThree if searchOne is nodeTwo else nodeOne
    return searchTarget(nodeTwo,target)

def searchTarget(node,target):
    while node is not None and node is not target:
        node = node.left if target.value < node.value else node.right

    return node is target