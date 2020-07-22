class Solution_combination:
    def subsets(self, nums):
        ans = []
        
        def dfs(amount, start_pos, cur_arr):
            if len(cur_arr) == amount:
                ans.append(cur_arr.copy())
                return
            for i in range(start_pos, len(nums)):
                cur_arr.append(nums[i])
                dfs(amount, i+1, cur_arr)
                cur_arr.pop()
        
        for i in range(len(nums)+1):
            dfs(i,0, [])
        
        return ans
    
class Solution_permutation():
    def subsets(self, nums):
        ans = []
        used = [False]*len(nums)
        def dfs(amount, cur_arr):
            if len(cur_arr) == amount:
                ans.append(cur_arr.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                cur_arr.append(nums[i])
                dfs(amount, cur_arr)
                cur_arr.pop()
                used[i] = False
                
        for i in range(len(nums)+1):
            dfs(i, [])
        return ans
if __name__ == "__main__":
    grid = [1,2,3]
    sol = Solution_combination()
    print(sol.subsets(grid))
    
    sol2 = Solution_permutation()
    print(sol2.subsets(grid))