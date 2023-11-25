# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        self.parent = {} # To track parent and child

    def createSet(self, value):
        self.parent[value] = value # Initially value it self it's parent

    def find(self, value):
        if value not in self.parent:
            return None

        currentParent = value

        while currentParent != self.parent[currentParent]:
            currentParent = self.parent[currentParent]

        return currentParent

    def union(self, valueOne, valueTwo):
        if valueOne not in self.parent or valueTwo not in self.parent:
            return

        rootOne = self.find(valueOne)
        rootTwo = self.find(valueTwo)

        self.parent[rootTwo] = rootOne
