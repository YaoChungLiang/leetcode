# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        res = dict()
        r = []
        def inorder(node, idx):
            if node:
                if idx not in res:
                    res[idx] = []
                res[idx].append(node.val)
                inorder(node.left, idx-1)       
                inorder(node.right, idx+1)
        inorder(root, 0)
        for i in sorted(res.keys()):
            r.append(res[i])
        return r
    
