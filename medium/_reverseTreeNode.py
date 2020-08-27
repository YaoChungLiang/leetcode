class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        return str(self.val)
    def loopthrough(self, node):
        while node and node.val != None:
            print(node.val)
            node = node.next

def loopthrough(node):
    while node.val != None:
        print(node.val)
        node = node.next

def reverseNodes(node):
    head = ListNode(8)
    while node and node.next:
        tmp = ListNode(node.val)
        node = node.next
        new_node = ListNode(node.val)
        new_node.next = tmp
        tmp = new_node
        
def reverseNodes_v2(node):
    head = ListNode(8)
    while node and node.next:
        rev_head = ListNode(node.next.val)
        tmp = ListNode(node.val)
        rev_head.next = tmp
        rev_head = rev_head.next

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = ListNode(0)
    cur = head
    for i in arr:
        cur.next = ListNode(i)
        cur = cur.next
    head.loopthrough(head.next)
    rev_nodes = reverseNodes(head.next)
    rev_nodes.loopthrough(rev_nodes)
    