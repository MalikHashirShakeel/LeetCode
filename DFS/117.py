"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        if not root:
            return None

        queue = [root]
        temp = []
        while queue != []:
            node = queue.pop(0)
            node.next = queue[0] if queue != [] else None

            if node.left:
                temp.append(node.left) 

            if node.right:
                temp.append(node.right) 

            if queue == []:
                queue += temp
                temp = []

        return root
            