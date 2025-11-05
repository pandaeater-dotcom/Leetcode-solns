"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def populateGraph(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return
            if node in visited:
                return visited[node]
            clone = Node(node.val)
            visited[node] = clone
            for neighbor in node.neighbors:
                val = populateGraph(neighbor)
                if val is not None:
                    clone.neighbors.append(val)
            
            return clone
        return populateGraph(node)
