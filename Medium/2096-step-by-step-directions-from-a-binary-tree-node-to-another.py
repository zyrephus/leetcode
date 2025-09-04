# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def getPath(curr, target, path):
            if not curr:
                return False

            if curr.val == target:
                return True

            path.append("L")
            if getPath(curr.left, target, path):
                return True
            path.pop()

            path.append("R")
            if getPath(curr.right, target, path):
                return True
            path.pop()

            return False
        
        s_path, d_path = [], []
        getPath(root, startValue, s_path)
        getPath(root, destValue, d_path)

        i = 0
        while i < len(s_path) and i < len(d_path) and s_path[i] == d_path[i]:
            i += 1
        
        return 'U' * (len(s_path) - i) + ''.join(d_path[i:])
