# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depth(root) != -1

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.depth(root.left)
        if leftHeight == -1:
            return -1

        rightHeight = self.depth(root.right)
        if rightHeight == -1:
            return -1

        if abs(rightHeight - leftHeight) > 1:
            return -1

        return 1 + max(leftHeight, rightHeight)
