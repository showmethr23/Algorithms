# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode()
        
        while l1 and l2: # while list1 and list2 are not None
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1: # if l1 is not empty add it at the end of the list
            current.next = l1
        elif l2: # if l2 is not empty add it at the end of the list
            current.next = l2
            
        return dummy.next

        # Solution 2


