import math
class Solution1:
    def numSquares(self, n: int) -> int:
        # recursive
        global ans
        ans = n
        def dfs(n):
            global ans
            a = int(math.sqrt(n))
            if n <= 3:
                return n
            if a*a == n:
                return 1
            for i in range(1,a):
                ans = min(ans, 1+ dfs(n-i*i))
            return ans
        return dfs(n)
    
import math
class Solution:
    def numSquares(self, n: int) -> int:
        a = int(math.sqrt(n))
        if a*a == n:
            return 1
        if n <= 3:
            return n
        dp = [i for i in range(n+1)]
        
        for i in range(4,n+1):
            for j in range(1,a+1):
                dp[i] = min( dp[i], 1+dp[n-j*j])
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.numSquares(12))