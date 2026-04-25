# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        curr1 = head
        while curr1:
            length += 1
            curr1 = curr1.next
        last_kth = length - n
        if last_kth == 0:
            return head.next

        track = 0
        curr2 = head
        while curr2:
            if track == last_kth - 1:
                curr2.next = curr2.next.next
            track += 1
            curr2 = curr2.next
        return head

        