# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def _diameter(root: Optional[TreeNode]) -> None:
            if not root:
                return 0

            left_path = _diameter(root.left)
            right_path = _diameter(root.right)

            nonlocal diameter
            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        _diameter(root)
        return diameter
