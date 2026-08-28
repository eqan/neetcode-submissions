# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            # swap operation
            curr.next = prev # shifted the next to previous e.g C
            prev = curr # shifted previous to curr e.g A
            curr = nxt # shifted curr to next e.g B
        return prev
