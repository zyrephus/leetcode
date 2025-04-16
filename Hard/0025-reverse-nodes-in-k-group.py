# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKthNode(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        prev_group_end = dummy

        while True:
            kth = getKthNode(prev_group_end, k)
            if not kth:
                break
            
            group_start = prev_group_end.next
            next_group_start = kth.next
        
            # Reverse group
            prev, curr = None, group_start
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect reversed group
            prev_group_end.next = prev
            group_start.next = next_group_start
            prev_group_end = group_start
        
        return dummy.next
