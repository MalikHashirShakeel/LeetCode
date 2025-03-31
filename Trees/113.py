# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, path, currSum):
            if not node: return

            path.append(node.val)
            currSum += node.val

            if not node.left and not node.right and currSum == targetSum:
                result.append(list(path))

            dfs(node.left, path, currSum)
            dfs(node.right, path, currSum)

            path.pop()

        dfs(root, [], 0)
        return result