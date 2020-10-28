'''
data bricks:
    given 
    a : array[int]
    b : array[int]
    lower : int
    upper : int
    find number of pairs where
    lower <= a[i]^2 + b[j]^2 <= upper
'''
class Solution:
    def findPairs(self, a, b, upper, lower):
        a.sort()
        b.sort()
        print(f' a array = {a}')
        print(f' b array = {b}')
        print(f' lower = {lower}, upper = {upper}')
        # lower <= a*a + b*b <= upper
        # b <= sqrt(upper - a*a)
        # b >= sqrt(lower - a*a)
        res = 0
        for i in range(len(a)):
            if upper >= a[i]**2:
                up_remainder = (upper-a[i]**2)**(0.5)
                upper_idx = self.searchInsert(b, up_remainder)
                if upper_idx == len(b)or b[upper_idx] > up_remainder:
                    upper_idx -= 1
            else:
                continue

            if lower >= a[i]**2:
                lower_idx = self.searchInsert(b, (lower-a[i]**2)**0.5)
                if lower_idx == len(b):
                    continue
            else:
                lower_idx = 0
            print(f' cur a = {a[i]}, lower = {lower_idx},{b[lower_idx]} ,upper = {upper_idx}, {b[upper_idx]} , res = {res}')
            res += upper_idx - lower_idx + 1
        return res
            
    def searchInsert(self, nums, target):
        l , r = 0, len(nums)-1
        while l <= r:
            mid=(l+r)//2
            if nums[mid]== target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l
        

if __name__ == "__main__":
    sol = Solution()
    a = [0,1,3 ,5,8,9 , 10,11 ,13,17,21]
    b = [0,1,2,4,5,6,7,8]
    upper = 100000
    lower = -1
    print(sol.findPairs(a,b,upper,lower))