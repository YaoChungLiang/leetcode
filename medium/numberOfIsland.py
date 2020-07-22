class Solution:
    def numIslands(self, grid) :
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        x_len = len(grid)
        y_len = len(grid[0])
        res = 0
        que = []
        for x in range(x_len):
            for y in range(y_len):
                if grid[x][y] == '0':
                    continue
                res += 1
                grid[x][y] = '0'
                que.append(x*y_len + y)
                while(que):
                    idx = que.pop(0)
                    row = idx // y_len
                    col = idx % y_len
                    if row -1 >= 0 and grid[row-1][col] == '1':
                        que.append( (row-1)*y_len+col)
                        grid[row-1][col] = '0'
                    if row + 1 < x_len and grid[row+1][col] == '1':
                        que.append((row+1)*y_len+col)
                        grid[row+1][col] = '0'
                    if col -1 >= 0 and grid[row][col-1] == '1':
                        que.append(row*y_len + col-1)
                        grid[row][col-1] = '0'
                    if col + 1 < y_len and grid[row][col+1] == '1':
                        que.append(row*y_len+col+1)
                        grid[row][col+1] = '0'
        return res
    
if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sol = Solution()
    print(sol.numIslands(grid))
    
