import collections
class Solution:
    def findTargetSumWays(self, A, S):
        count = collections.Counter({0: 1})
        for x in A:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[S]
    
if __name__ == "__main__":
    sol = Solution()
    tar = [1,1,1,1,1]
    print(sol.findTargetSumWays(tar,3))