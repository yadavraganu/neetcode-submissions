# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head = ListNode()
        curr_new = head

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr_new.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                curr_new.next = ListNode(curr2.val)
                curr2 = curr2.next
            curr_new = curr_new.next
        if curr1:
            curr_new.next = curr1

        if curr2:
            curr_new.next = curr2
        
        return head.next