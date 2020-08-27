class Solution1:
    def jump(self, nums): # O(n^2)  time limit exceed
        if len(nums) == 1:
            return 0
        if nums[0]  >= len(nums)-1:
            return 1
        res = len(nums)
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)-1):
            for j in range(1,nums[i]+1):
                if i+j <= len(nums)-1:
                    dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[-1]
    
class Solution:
    def jump(self, nums) :  # O(n) pass
        steps = farest =  curEnd = 0
        for i in range(len(nums)-1):
            farest = max(farest, nums[i] + i)
            if i == curEnd:
                steps += 1 
                curEnd = farest
        return steps

if __name__ == "__main__":
    sol = Solution()
    tar = [2,3,1,1,4]
    print(sol.jump(tar))