
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n) solution

        # Create dummy node to handle edge cases like removing the head
        dummy = ListNode(0, head)
        res = dummy
        end = head

        for i in range(n):
            end = end.next
        
        # Move res and end together until end reaches the last node
        while end is not None:
            res = res.next
            end = end.next
        
        res.next = res.next.next

        return dummy.next 