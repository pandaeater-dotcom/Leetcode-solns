# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def findLCA(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root.val == startValue or root.val == destValue:
                return root
            
            left = right = None
            if root.left:
                left = findLCA(root.left)
            if root.right:
                right = findLCA(root.right)
            
            if left and right:
                return root
            return left or right
        
        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path
            
        if not root:
            return []
        LCA = findLCA(root)
        destLst = []
        startLst = []
        find(LCA, destValue, destLst)
        find(LCA, startValue, startLst)
        return "".join("U" * len(startLst)) + "".join(reversed(destLst))
