class Solution:
    def canJump(self, nums):
        lastGood = len(nums)-1
        for i in range(len(nums)-2, -1 ,-1):
            if i + nums[i] >= lastGood:
                lastGood = i
        return lastGood == 0
    
class Solution1:
    def canJump(self, nums):
        pass
    