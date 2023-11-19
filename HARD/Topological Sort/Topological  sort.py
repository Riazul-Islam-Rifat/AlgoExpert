def topologicalSort(jobs, deps):
    #   First  make the graph
    jobGraph = createJobGraph(jobs, deps)
    # Now implement DFS
    jobOrder = []  # To store the final order
    nodes = jobGraph.nodes

    while len(nodes):
        node = nodes.pop()  # We will start from a random node
        containCycle = DFS(node, jobOrder)
        if containCycle:
            return []
    return jobOrder


def DFS(node, jobOrder):
    if node.visited:
        return False
    if node.visiting:  # Wher we encounter a cycle
        return True
    node.visiting = True

    for prereqs in node.preqs:
        containCycle = DFS(prereqs, jobOrder)
        if containCycle:
            return []
    node.visited = True
    node.visiting = False

    jobOrder.append(node.job)


def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    # Populate the self.preqs || add pre-requisites of each node
    for prereq, job in deps:
        graph.addPrereq(job, prereq)
    return graph


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []  # List  of nodes / vertices
        self.graph = {}  # job : node
        # Now add nodes to the graph
        for job in jobs:
            self.addNode(job)

    def addNode(self, job):
        self.graph[job] = JobNode(job)  # Create a node for job and add it like graph = {job:JobNode}
        self.nodes.append(self.graph[job])  # Track  the nodes to iterate easily

    def addPrereq(self, job, prereq):
        # First find the jobNode or Node for job and prereq
        jobNode = self.graph[job]
        prereqNode = self.graph[prereq]
        # Now add pre-reqs
        jobNode.preqs.append(prereqNode)


# Class to create  the JobNode
class JobNode:
    def __init__(self, job):
        self.job = job
        self.preqs = []  # Stores the pre-requisites of a node
        # Next two to track the cycle
        self.visited = False  # Is the node visited or not
        self.visiting = False  # Are we visiting the node
