# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Search for the middle using the fast/slow pointer aka Floyd's Tortoise and Hare algorithm
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Reverse the middle to the end linked list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # Check from prev to head that all values are matching
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True