# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = [[root.val]]
        q = deque([root])
        temp = deque()

        while q:
            node = q.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if not q:
                if temp:
                    levels.append([_.val for _ in temp])
                q = temp
                temp = deque()
        return levels
