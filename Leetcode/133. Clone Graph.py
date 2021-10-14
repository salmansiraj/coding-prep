class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# O(V + E)
# Format visited dict with MAPPING oldNode -> newClone that is currently empty
# Loop through the node.neighbors and run helper

class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        if not node:
            return None

        def helper(node):
            if node in visited:
                return visited[node]

            cloneNode = Node(node.val, [])
            visited[node] = cloneNode

            if node.neighbors:
                cloneNode.neighbors = [helper(n) for n in node.neighbors]

            return cloneNode

        return helper(node)
