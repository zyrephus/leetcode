# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) solution, where n is the larger LL

        # Dummy node to serve as the start of the result LL
        res = ListNode()
        curr = res

        carry = 0
        while l1 or l2 or carry != 0:
            # Getting values of each LL
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculating the new carry and value to be inserted
            total = v1 + v2 + carry
            carry = total // 10
            total = total % 10
            curr.next = ListNode(total)
            
            # Updating nodes
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Returning next of dummy node (head of result list)
        return res.next