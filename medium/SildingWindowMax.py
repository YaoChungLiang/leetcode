from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        # edge case:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        # initialization
        deq = deque()
        max_idx = 0
        for i in range(k):
            # clean deque
            if deq and deq[0] == i-k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            # append items to deque
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]
        
        # looping through
        for i in range(k,n):
            if deq and deq[0] == i-k:
                deq.popleft()
                
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            output.append(nums[deq[0]])
        return output
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))