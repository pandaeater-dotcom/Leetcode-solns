# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxWidth = 0
        q = deque([(0, root)])

        while q:
            level_size = len(q)
            maxWidth = max(maxWidth, q[-1][0] - q[0][0] + 1)

            for _ in range(level_size):
                index, node = q.popleft()
                if node.left:
                    q.append((index * 2, node.left))
                if node.right:
                    q.append((index * 2 + 1, node.right))
        return maxWidth
