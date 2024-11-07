# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) solution

        tortoise = head
        hare = head

        # If list has odd number of nodes, hare will reach the end (None), tortoise will be at exact middle node
        # If list has even number of nodes, hare will reach the last node (hare.next will be None), tortoise will be at second middle node
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

        return tortoise