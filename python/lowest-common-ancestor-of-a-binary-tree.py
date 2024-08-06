# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasDescendant(self, root: Optional[TreeNode], d: int) -> bool:
        if not root:
            return False
        if root.val == d:
            return True
        return self.hasDescendant(root.left, d) or self.hasDescendant(root.right, d)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val == p.val or root.val == q.val):
            return root
        pPos = self.hasDescendant(root.left, p.val)
        qPos = self.hasDescendant(root.right, q.val)
        print(root.val, pPos, qPos)
        if qPos and not pPos:
            return self.lowestCommonAncestor(root.right, p, q)
        if not qPos and pPos:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
