# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        arr = []        
        self.dfs(root, arr)
        return arr
        
    def dfs(self, node, arr):
        if node is None:
            return
        if node.left and not node.right:
            arr.append(node.left.val)
        if node.right and not node.left:
            arr.append(node.right.val)
        
        self.dfs(node.left , arr)
        self.dfs(node.right, arr)

class Solution2:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c==']':
                num = stack.pop()
                preString = stack.pop()
                curString = preString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString