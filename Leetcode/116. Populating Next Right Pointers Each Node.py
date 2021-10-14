"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Iteratively O(N) runtime and space  O(N)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = deque([root])

        while len(queue):
            levelLength = len(queue)

            for i in range(levelLength):
                currNode = queue.popleft()
                if i < levelLength - 1:
                    currNode.next = queue[0]

                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return root
