import numpy as np
class Solution:
    def canPartition(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return False
        total = 0
        for num in nums:
            total += num
        if total % 2:
            return False
        target = total//2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for i in range(target,-1,-1):
                if i >= num:
                    dp[i] = dp[i] or dp[i-num]
                print(np.matrix(dp))
        return dp[target]

if __name__ == "__main__":
    sol = Solution()
    tar = [1,5,11,5]
    print(sol.canPartition(tar))