# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) solution

        prev = head
        curr = head.next if head else None # In case there are 0 nodes
        while curr:
            # Skip duplicate
            if prev.val == curr.val:
                prev.next = curr.next
            # Move prev forward if there is no duplicate
            else:
                prev = curr
            curr = curr.next

        return head 
