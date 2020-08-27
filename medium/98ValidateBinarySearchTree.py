# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        
class Solution:
    def isValidBST(self, root):
        left_max = -(2**31)
        right_min = 2**31
        return self.dfs(root, left_max, right_min)
    
    def dfs(self, node, left_max, right_min):
        if not node:
            return        
        
        if node.left:
            left_max = max(left_max, self.dfs(node.left))
            yield node.val
        if node.right:
            right_min = min(right_min, self.dfs(node.right))
            yield node.val
        
        if node.val < left_max or node.val > right_min:
            return False
        else:
            return True

## works , recursive 
class Solution1:
    def isValidBST(self, root) :
        return self.dfs(root)
    
    def dfs(self, node, mini = -(2147483649), maxi = 2147483648):
        if not node:
            return True
        val = node.val
        if val <= mini or val >= maxi:
            return False
        if not self.dfs(node.right, val, maxi):
            return False
        if not self.dfs(node.left, mini, val):
            return False
        return True

class Solution2:
    def isValidBST(self, root) :
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack :
            node, lower , upper = stack.pop()
            if not node:
                continue
            val = node.val
            if val <= lower or val >= upper :
                return False
            stack.append((node.right, val,   upper))
            stack.append((node.left,  lower, val  ))
        return True

if __name__ == "__main__":
    sol2 = Solution2()
    root = Node(5)
    root.left = Node(1)
    root.right = Node(4)
    root.right.right = Node(3)
    root.right.left = Node(6)
    print(sol2.isValidBST(root))