# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        que = PriorityQueue()
        curr = dummy = ListNode(0)
        for list_idx, node in enumerate(lists):
            if node:
                que.put((node.val ,list_idx, node))
        while que.qsize():
            popped = que.get()
            list_idx = popped[1]
            curr.next = popped[2]
            curr = curr.next
            if curr.next:
                que.put(( curr.next.val, list_idx ,curr.next))
        return dummy.next
    