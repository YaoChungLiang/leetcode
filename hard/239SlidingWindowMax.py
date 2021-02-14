class Solution:
    def maxSlidingWindow(self, nums, k):
        if k > len(nums):
            return [max(nums)]
        
        res = []
        window = []
        for i in range(k):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
        res.append(nums[window[0]])
        
        for i in range(k ,len(nums)):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            
            if window and window[0] <= i - k:
                window.pop(0)
            
            window.append(i)
            res.append(nums[window[0]])
        return res

sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.maxSlidingWindow(nums, k))