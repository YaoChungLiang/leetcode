# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        head = cur
        carry = 0
        while l1 and l2:
            div, res =  divmod(l1.val+l2.val+carry, 10)
            carry = 1 if div > 0 else 0
            cur.next = ListNode(res)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        l = l1 if l1 else l2
        while l :
            div, res = divmod(l.val+carry,10)
            carry = 1 if div > 0 else 0
            cur.next = ListNode(res)
            cur = cur.next
            l = l.next
        
        if carry:
            cur.next = ListNode(carry)
        return head.next
    
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.val == val:
            dummy = head.next
            head = head.next
        while head and head.next and head.next.val == val:
            if head.next.next:
                head.next= head.next.next
                head = head.next.next
            else:
                head.next = None
        
        
        return dummy if not dummy.next else dummy.next