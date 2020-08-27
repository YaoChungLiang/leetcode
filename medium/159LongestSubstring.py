class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        left, right = 0,0
        dic = dict()
        max_len = 2
        while(right < n-1):
            if len(dic) < 3:
                dic[s[right]] = right
                right += 1
                
            if len(dic) == 3:
                del_idx = min(dic.values())
                del dic[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len, right-left)
            #dic[s[left]] = left
        return max_len
if __name__ == "__main__":
    sol = Solution()
    arr = 'eaaaaabbcdcd'
    print(sol.lengthOfLongestSubstringTwoDistinct(arr))