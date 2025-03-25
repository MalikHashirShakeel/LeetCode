"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root):
        if not root:
            return []

        res = []

        for node in root.children:
            res += self.postorder(node)

        res.append(root.val)

        return res