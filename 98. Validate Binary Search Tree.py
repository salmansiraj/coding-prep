# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # O(n) time with O(1) space
    def helper(self, node, lower, upper):
           if not node:
                return True

            if lower >= node.val or upper <= node.val:
                return False

            if not self.helper(node.left, lower, node.val):
                return False

            if not self.helper(node.right, node.val, upper):
                return False
            return True

    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))



    # O(n) time with O(n) space 
    # def inorderTraversal(self, root: TreeNode, result):
    #     if root is None:
    #         return

    #     self.inorderTraversal(root.left, result)
    #     result.append(root.val)
    #     self.inorderTraversal(root.right, result)

    #     return result

    # def isValidBST(self, root: TreeNode) -> bool:

    #     if root is None or (root.left is None and root.right is None):
    #         return True

    #     result = []
    #     self.inorderTraversal(root, result)

    #     for i in range(1, len(result)):
    #         if result[i] <= result[i - 1]:
    #             return False

    #     return True


