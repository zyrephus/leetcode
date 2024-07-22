# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # O(n) solution

        res = []

        def inorder(root):
            if not root: # Base case
                return
            # Order is left, root, right
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return res