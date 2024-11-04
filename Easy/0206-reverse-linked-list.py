# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) solution
        
        prev = None 
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev # Reverse curr node pointer to point to prev node

            prev = curr # Move the prev up to curr node
            curr = temp #  Move curr to the next node in original list

        return prev