import sys
class Solution:
    def numIsland(self, grid): # -> int
        self.grid = grid
        self.res = 0
        # self.s = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.res += 1
                    self._dfs(i,j)
        return self.grid
                 

    def _dfs(self,x,y):
        if x < 0 or y < 0 or x >= len(self.grid) or y >= len(self.grid[0]) or self.grid[x][y] == 0:
            return
        self.grid[x][y] = self.res
        self._dfs(x, y+1)
        self._dfs(x+1, y)
        self._dfs(x, y-1)
        self._dfs(x-1, y)
        # self._dfs(x+1, y+1)
        # self._dfs(x-1, y+1)
        # self._dfs(x+1, y-1)
        # self._dfs(x-1, y-1)

if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    grid = [
      [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
      [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    s = Solution()
    print(s.numIsland(grid))
