# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        actual_head = head
        new_head = ListNode()
        curr = new_head
        while actual_head:
            stack.append(actual_head)
            actual_head = actual_head.next
        while stack:
            node = stack.pop()
            curr.next = ListNode(node.val)
            curr = curr.next
        return new_head.next


