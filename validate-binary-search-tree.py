# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveValidBST(self, node: Optional[TreeNode], lower: int, upper: int) ->  bool:
        if not node:
            return True
        print(node.val, lower, upper)
        if node.val <= lower or node.val >= upper:
            return False
        return self.recursiveValidBST(node.left, lower, node.val) and self.recursiveValidBST(node.right, node.val, upper)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.recursiveValidBST(root.left, float('-inf'), root.val) and self.recursiveValidBST(root.right, root.val, float('inf'))
  
