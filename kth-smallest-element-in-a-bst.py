# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def treeSize(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     return 1 + self.treeSize(root.left) + self.treeSize(root.right)

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     index = self.treeSize(root.left) + 1
    #     print(index)
    #     if k > index:
    #         return self.kthSmallest(root.right, k - index)
    #     elif k < index:
    #         return self.kthSmallest(root.left, k)
    #     return root.val
    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        lst = []
        lst.extend(self.inorder(root.left))
        lst.append(root.val)
        lst.extend(self.inorder(root.right))
        return lst
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:        
        return self.inorder(root)[k-1]
        
            
