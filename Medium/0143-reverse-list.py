# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Split the list in half
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Disconnect first half
        second = slow.next
        slow.next = None
        
        # Reverse the second half list
        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge the two sorted lists 
        first, second = head, prev
        while second:
            temp_1, temp_2 = first.next, second.next
            first.next = second
            second.next = temp_1
            first, second = temp_1, temp_2

