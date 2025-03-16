# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        queue = [root]
        res = [root.val]
        temp = []
        
        while queue:
            node = queue.pop(0)

            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

            if queue == []:
                queue += temp
                if queue != []:
                    res.append(queue[-1].val)
                temp = []

        return res

        