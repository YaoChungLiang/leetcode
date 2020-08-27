# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution: # stack is slow
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        cur = rev_head = ListNode(0)
        while stack:
            newnode = ListNode(stack.pop())
            cur.next = newnode
            cur = cur.next
        return rev_head.next

class Solution: # iterative using three pointers
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return cur
'''    
class Solution3: # recursive
    def looop(self, node):
        while node:
            print(node.val)
            node = node.next
    def reverseList(self, head):
        cur = None
        def _rev(node, prev= None):
            nnn = node
            ppp = prev
            print("loop through node")
            self.looop(nnn)
            print("loop through prev")
            self.looop(ppp)
            
            
            if not node:
                return prev     
            n = node.next  
            node.next = prev
            return _rev(n, node)
        return _rev(head)
    
if __name__ == "__main__":
    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(None)
    sol = Solution3()
    k = sol.reverseList(head)
    while k:
        print(k.val)
        k = k.next
    