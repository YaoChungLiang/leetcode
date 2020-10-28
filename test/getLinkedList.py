class LL:
    def __init__(self,val, nxt = None):
        self.val = val
        self.nxt = nxt

class Sol:
    def mkLL(self, n):
        if n <= 0:
            return 
        cur = head = LL(1)
        while cur.val < n:
            cur.nxt = LL(cur.val + 1)
            cur = cur.nxt
        return head

