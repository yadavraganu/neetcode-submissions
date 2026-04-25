# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head_res = ListNode()
        carry = 0
        curr = head_res
        while l1 or l2:
            
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            add = l1v + l2v + carry
            carry = add // 10
            digit = add % 10

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            curr.next = ListNode(carry)
        
        return head_res.next
        