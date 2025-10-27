# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView = []

        def recursiveRightView(root: Optional[TreeNode], level: int):
            if not root:
                return

            nonlocal rightView
            if len(rightView) - 1 < level:
                rightView.append(root.val)
            recursiveRightView(root.right, level + 1)
            recursiveRightView(root.left, level + 1)

        recursiveRightView(root, 0)
        return rightView
