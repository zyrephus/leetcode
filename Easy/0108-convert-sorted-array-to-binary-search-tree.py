# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createTree(arr):
            if not arr:
                return None
                
            n = len(arr)
            root = TreeNode(arr[n//2], createTree(arr[:n//2]), createTree(arr[n//2+1:]))

            return root
        
        return createTree(nums)
        
