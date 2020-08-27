# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        middle = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:middle+1],inorder[:middle] )
        root.right = self.buildTree(preorder[middle+1:],inorder[middle+1:])
        return root
    
class Solution2:
    def buildTree(self, preorder, inorder):
        idx = dict()
        for index, val in enumerate(inorder):
            idx[val] = index
        stack = []
        head = None
        for val in preorder:
            if not head:
                head = TreeNode(val)
                stack.append(head)
            else:
                node = TreeNode(val)
                if idx[val] < idx[stack[-1].val]:
                    stack[-1].left = node
                else:
                    while stack and idx[stack[-1].val] < idx[val]:
                        u = stack.pop()
                    u.right = node
                stack.append(node)
        return head
    
if __name__ == "__main__":
    sol = Solution2()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(sol.buildTree(preorder, inorder))
    