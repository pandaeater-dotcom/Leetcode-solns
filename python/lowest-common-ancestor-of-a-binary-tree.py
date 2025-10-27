# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        returnNode = None

        def recursiveAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional[bool]:
            nonlocal returnNode
            if not root:
                return False
            leftCheck = recursiveAncestor(root.left, p, q)
            rightCheck = recursiveAncestor(root.right, p, q)

            if leftCheck is None or rightCheck is None:
                return None

            elif leftCheck == 1 and rightCheck == 1:
                returnNode = root
            elif root.val == p.val or root.val == q.val:
                if leftCheck or rightCheck:
                    returnNode = root
                else:
                    return True
            else:
                return leftCheck or rightCheck

        recursiveAncestor(root, p, q)
        if not returnNode:
            return root
        return returnNode
