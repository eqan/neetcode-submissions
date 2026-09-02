# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Recursive Solution
    def recursive_solution(self, head):
        if not head or not head.next:
            return head
        new_head = self.recursive_solution(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.recursive_solution(head)
        return head
        # Iterative Solution
        # stack = []
        # actual_head = head
        # new_head = ListNode()
        # curr = new_head
        # while actual_head:
        #     stack.append(actual_head)
        #     actual_head = actual_head.next
        # while stack:
        #     node = stack.pop()
        #     curr.next = ListNode(node.val)
        #     curr = curr.next
        # return new_head.next


