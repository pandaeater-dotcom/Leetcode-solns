# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        goodCount = 1

        def recursiveGoodCheck(root: Optional[TreeNode], pathHighest: int):
            if not root:
                return
            nonlocal goodCount
            if root.val >= pathHighest:
                goodCount += 1
            curHighest = max(root.val, pathHighest)
            recursiveGoodCheck(root.left, curHighest)
            recursiveGoodCheck(root.right, curHighest)

        recursiveGoodCheck(root.left, root.val)
        recursiveGoodCheck(root.right, root.val)
        return goodCount
