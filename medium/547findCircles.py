class Solution:
    def findCircleNum(self, M):
        row = col = len(M)
        groups = 0
        visited = set()
        for i in range(row):
            if i not in visited:
                visited.add(i)
                self.dfs(M, i , visited)
                groups += 1
        return groups
                
    def dfs(self, M, i ,visited ):
        for j in range(len(M[i])):
            if j != i and M[i][j] == 1:
                self.dfs(M, j, visited)
                visited.add(j)
                
class Solution2:
    def findCircleNum(self, M):
        row = col = len(M)
        groups = 0
        visited = [0]*row
        for i in range(row):
            if visited[i] == 0:
                self.dfs(M, i , visited)
                groups += 1
        return groups
                
    def dfs(self, M, i ,visited):
        for j in range(len(M)):
            if visited[j] == 0 and M[i][j] == 1:
                visited[j] = 1
if __name__ == "__main__":
    sol = Solution2()
    M = [[1,1,0],[1,1,0],[0,0,1]]
    print(sol.findCircleNum(M))