# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        queue = deque()
        queue.append(root)

        while queue:
            q_len = len(queue)

            for i in range(q_len):
                node = queue.popleft()
                
                # Last node in the level
                if i == q_len - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return res
      
