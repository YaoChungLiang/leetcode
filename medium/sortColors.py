class Solution1:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        st = 0
        end = len(nums)-1
        for i in range(len(nums)):
            if nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            if nums[i] == 0:
                nums[i], nums[st] = nums[st], nums[i]
                st += 1
            if i >= end:
                break
        return nums
    
class Solution:
    def sortColors(self, nums):
        st = 0
        end = len(nums)-1
        cur = 0
        while(cur <= end):
            if nums[cur] == 0:
                nums[cur],nums[st] = nums[st],nums[cur]
                st += 1
                cur += 1
            elif nums[cur]==2:
                nums[cur], nums[end]=nums[end], nums[cur]
                end-=1
            else:
                cur+=1
        return nums

if __name__ == "__main__":
    # coins = [186,419,83,408]
    # amount = 6249
    # nums = [2,0,2,1,1,0]
    # nums = [2,1,2]
    nums = [2,0,1]
    sol = Solution()
    print(sol.sortColors(nums))
    