class Solution:
    def hammingWeight(self, n):
        # solution 1
        res = 0
        while n != 0:
            if(n & 1) != 0:
                res += 1
            n = n >> 1
        return res
        
        # solution 2
        #return bin(n).count('1')
        
        #solution 3
        #res = 0
        #while(n!=0):
        #    res += 1
        #    n = n&(n-1)
        #return res