# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Middle Point
        fast = head.next
        slow  = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow
        
        # Reverse second half of list
        curr = middle.next
        prev = None
        middle.next = None # Break from first half of list

        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp

        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
