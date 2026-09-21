# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        # Reverse the first half
        while fast and fast.next:
            fast = fast.next.next

            # Save next node
            tmp = slow.next
            # Point current node to backwards to the prevnode
            slow.next = prev
            # Move prev forward to curr node
            prev = slow
            # Move slow forward to next
            slow = tmp
        res = 0
        # Now we continue from slow(continuing from mid to last) and prev(mid to start) to add elements
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res
        
        