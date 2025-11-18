class DSU:
    def __init__(self, N):
        self.N = N
        self.size = [1] * N
        self.reps = list(range(N))
    
    def find(self, node):
        if self.reps[node] == node:
            return node
        self.reps[node] = self.find(self.reps[node])
        return self.reps[node]

    def doUnion(self, nodeA, nodeB):
        nodeA = self.find(nodeA)
        nodeB = self.find(nodeB)

        if nodeA == nodeB:
            return False
        if self.size[nodeA] > self.size[nodeB]:
            self.reps[nodeB] = nodeA
        elif self.size[nodeB] > self.size[nodeA]:
            self.reps[nodeA] = nodeB
        else:
            self.reps[nodeA] = nodeB
            self.size[nodeB] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for edge in edges:
            if not dsu.doUnion(edge[0] - 1, edge[1] - 1):
                return edge
        return []
