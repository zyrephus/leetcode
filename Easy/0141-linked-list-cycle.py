# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) solution
        
        tortoise = head
        hare = head

        # If there is no cycle, the hare will reach the end of the list
        while hare and hare.next: 
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return True

        return False
