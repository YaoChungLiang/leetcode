from treenode import root

class Solution_recursive:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root:
            if root.left:
                print(root.val)
                self.helper(root.left, res)
            res.append(root.val) 
            if root.right:
                print(root.val)
                self.helper(root.right, res)
                
class Solution_iterative:
    def inorderTraversal(self, root):
        stack = []
        res = []
        cur = root
        while(cur or len(stack)):
            while(cur):
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
    
                
if __name__ == "__main__":
    res = Solution_iterative()
    print(res.inorderTraversal(root))
    #      1
    #   2     3
    # 4  5  6
