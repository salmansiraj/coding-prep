class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # USING BFS
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            levelLength = len(queue)
            for i in range(levelLength):
                currNode = queue.popleft()
                levels[level].append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

            level += 1

        return levels

        # USING DFS
        def levelOrder2(self, root: TreeNode) -> List[List[int]]:
            levels = []
            if root is None:
                return levels

            def helper(node, levels, level):
                if len(levels) == level:
                    levels.append([])

                if node is not None:
                    levels[level].append(node.val)

                if node.left:
                    helper(node.left, levels, level + 1)
                if node.right:
                    helper(node.right, levels, level + 1)

                return levels

            helper(root, levels, 0)
            return levels
