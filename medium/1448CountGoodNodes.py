class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    def __repr__(self,pp):
        return 3
    # 3
   #1    4
 #3    1   5

class npy:
    @staticmethod
    def count(a):
        return a+1


class Solution:
    def goodNodes(self, root):
        maximum = root.val
        global count
        count = 0
        
        def dfs(node, max_num):
            global count
            if not node:
                return
            if node.val >= max_num:
                count += 1
            if node.left:
                dfs(node.left,  max(max_num, node.val))
            if node.right:
                dfs(node.right,  max(max_num, node.val))
                
        dfs(root, maximum)    
        return count
    
if __name__ == "__main__":
    root = Node(3)
    root.left = Node(1)
    root.right = Node(4)
    root.left.left = Node(3)
    root.right.right = Node(5)
    root.right.left = Node(1)
    
    sol = Solution()
    print(sol.goodNodes(root))
    
    print(npy.count(6))