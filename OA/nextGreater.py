class Solution:
    def nextGreaterElements(self, nums):
        res = [0.5] * len(nums)
        i = 0
        stack = []
        while i < 2 * len(nums):
            while stack and nums[stack[-1]] < nums[i%len(nums)]:
                if res[stack[-1]] == -2: 
                    res[stack.pop()] = nums[i%len(nums)]
                else:
                    stack.pop()
            stack.append(i%len(nums))
            if len(stack) > 1 and stack[-1] == stack[0]:
                break
            i += 1
        for i in range(len(res)):
            if res[i] == 0.5:
                res[i] = -1
        return res

if __name__ == "__main__":
    arr = [-3,-2,-2,-3]
    s = Solution()
    print(s.nextGreaterElements(arr),  [-2,-1,-1,-2])