# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return None

        queue = deque([root])
        leftmost = root.val  

        while queue:
            leftmost = queue[0].val  
            for _ in range(len(queue)): 
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return leftmost