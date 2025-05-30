"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        if not root:
            return []

        res = []

        res.append(root.val)

        for node in root.children:
            res += self.preorder(node)

        return res 