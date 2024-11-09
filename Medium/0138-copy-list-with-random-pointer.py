"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(n) solution

        if not head:
            return None
        
        node_map = {}

        # First pass: create copies of each node without next and random pointers
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        # Second pass: assign next and random pointers using node_map
        curr = head
        while curr:
            if curr.next: 
                # Set next of copied node to copy of curr.next
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                # Set random of copied node to copy of curr.random
                node_map[curr].random = node_map[curr.random]
            curr = curr.next

        return node_map[head]