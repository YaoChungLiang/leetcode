class Solution:
    def minFlips(self, a, b, c):
        res = 0
        bina = bin(a)
        binb = bin(b)
        binc = bin(c)
        for i in range(32):
            mask = 1 << i
            maskc = c & mask
            maska = a & mask
            maskb = b & mask
            if maskc :
                if ~(maska | maskb):
                    res += 1
            else:
                if maska & maskb:
                    res += 2
                elif (maska | maskb):
                    res += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minFlips(2,6,5))