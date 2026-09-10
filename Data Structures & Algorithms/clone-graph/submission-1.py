"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hashmap to store old to new mappings
        oldToNew = {}
        
        def dfs(node):
            # Return copy if the node is present in the hashmap
            if node in oldToNew:
                return oldToNew[node]
            # Deep copy of the node
            copy = Node(node.val)
            # Mapping the old node with its copy
            oldToNew[node] = copy
            # Iterating and copying all neighbors using DFS to copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            # After all done returning the copy
            return copy
        # Returning the copy after the dfs finished
        return dfs(node) if node else None
