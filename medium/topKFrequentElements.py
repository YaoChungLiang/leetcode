

class Solution:
    def topKFrequent(self, nums, k):
        nums.sort()
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0]]
        pre = nums[0]
        counter = 0
        res = []
        for i in nums:
            if i == pre:
                counter += 1
            else:
                res.append([counter,pre])
                pre = i
                counter = 0
        if not nums:
            res.append([counter,pre])
        else:
            res.append([counter, i])
        
        res.sort()
        real_res = []
        for i in range(k):
            real_res.append( res[len(res)-1-i][1] )
        return real_res
from collections import Counter
class Solution1:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left,right, pivot_idx):
            pivot_freq = count[unique[pivot_idx]]
            unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]
            
    
if __name__ == "__main__":
    nums = [-1,-1]
    k = 1
    sol = Solution()
    print(sol.topKFrequent(nums, k ))