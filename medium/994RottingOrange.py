class Solution:
    def orangesRotting(self, grid):
        que = []
        hasRottenOrange = False
        hasFreshOrange = False
        x_len = len(grid)
        y_len = len(grid[0])
        for x in range(x_len):
            for y in range(y_len):
                if grid[x][y]== 2:
                    que.append([x,y])
                    hasRottenOrange = True
                if grid[x][y] == 1:
                    hasFreshOrange = True
        if not hasRottenOrange and not hasFreshOrange:
            return 0
        counter = 0
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        while que:
            grid, que, counter = self.BFS(grid, que, counter,dirs,x_len,y_len)
        
        for x in range(x_len):
            for y in range(y_len):
                if grid[x][y] == 1:
                    return -1
        return counter
    
    def BFS(self, grid, que, counter, dirs,x_len,y_len):
        n = len(que)
        for _ in range(n):
            x,y = que.pop(0)
            for i,j in dirs:
                nx = x + i
                ny = y + j
                if 0<=nx<x_len and 0<=ny<y_len and grid[nx][ny] == 1:
                    que.append([nx,ny])
                    grid[nx][ny] = 2
        if len(que) != 0:
            counter += 1
        return grid, que, counter
    
if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    sol = Solution()
    print(sol.orangesRotting(grid))