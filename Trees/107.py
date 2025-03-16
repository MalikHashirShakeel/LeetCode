class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            level = []
            temp = []

            for node in queue:
                level.append(node.val)  
                if node.left:
                    temp.append(node.left) 
                if node.right:
                    temp.append(node.right)  

            res.insert(0, level)

            queue = temp

        return res