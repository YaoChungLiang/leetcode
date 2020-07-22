class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        x_len = len(board)
        y_len = len(board[0])
        NotSurround = [[0 for _ in range(y_len)] for _ in range(x_len)]
        que = []
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(x_len):
            for j in range(y_len):
                if (i == 0 or j == 0 or i == x_len-1 or j== y_len-1) and board[i][j]=='O':
                    que.append([i,j])
                    NotSurround[i][j] = 1
        while que:
             que, NotSurround = self.BFS(que, board, NotSurround, dirs,x_len,y_len)
        for i in range(x_len):
            for j in range(y_len):
                if NotSurround[i][j] == 0:
                    board[i][j] = 'X'
        self.board = board
                    
    def BFS(self, que, board, NotSurround, dirs,x_len,y_len):
        n = len(que)
        for _ in range(n):
            x,y = que.pop(0)
            for i,j in dirs:
                nx = x + i
                ny = y + j
                if  0<=nx<x_len and 0<=ny<y_len and board[nx][ny] == 'O' and NotSurround[nx][ny] == 0:
                    que.append([nx,ny])
                    NotSurround[nx][ny] = 1
        return que, NotSurround
if __name__ == "__main__":
    grid = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol = Solution()
    sol.solve(grid)
    print(sol.board)