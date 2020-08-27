"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# iteratively
class Solution: 
    def preorder(self, root: 'Node') -> List[int]:
        que = [root]
        res = []
        while que:
            node = que.pop(0)
            if not node:
                continue
            res.append(node.val)
            if node.children:
                for child in node.children[::-1]:
                    que.insert(0,child)
        return res

# recursively
class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def preTraversal(node):
            if node:
                res.append(node.val)
                if node.children:
                    for c in node.children:
                        preTraversal(c)
        preTraversal(root)
        return res