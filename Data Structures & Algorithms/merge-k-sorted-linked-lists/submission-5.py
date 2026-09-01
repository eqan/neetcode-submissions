# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoList(self,l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
                


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        '''
        Divide & Conquer Approach, specific type used here is merge sort

        Start: [L1, L2, L3, L4, L5, L6, L7, L8]
        Level 1: Merge L1+L2 → M1, L3+L4 → M2, L5+L6 → M3, L7+L8 → M4
        Result: [M1, M2, M3, M4]  (each merge touches ~2n nodes)
        Level 2: Merge M1+M2 → N1, M3+M4 → N2
         Result: [N1, N2]  (each merge touches ~4n nodes)
        Level 3: Merge N1+N2 → Final
         Result: [Final]  (touches all 8n nodes)
        '''
        while len(lists) > 1:
            mergedLists = []
            # Picking 2 lists at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None 
                mergedLists.append(self.mergeTwoList(l1, l2))
            lists = mergedLists
        return lists[0]


