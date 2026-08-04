# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       set_val = set() 
       start = head
       while start != None:
            if start in set_val:
                return True
            set_val.add(start)
            start = start.next
       return False