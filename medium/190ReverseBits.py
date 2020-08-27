class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        print(bin(n))
        print(bin(n>>16))
        print(bin(n<<16))
        n = (n >> 16) | (n << 16)
        print(bin(n))
        print(bin(0xff00ff00))
        print(bin(n&0xff00ff00))
        print(bin((n&0xff00ff00)>>8))
        
        print(bin(0x00ff00ff))
        print(bin(n & 0x00ff00ff))
        print(bin((n & 0x00ff00ff)<<8))
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        
        print(bin(n))
        print(bin(0xf0f0f0f0))
        print(bin(n&0xf0f0f0f0))
        print(bin((n&0xf0f0f0f0)>>4))
        
        print(bin(0x0f0f0f0f0f))
        print(bin(n & 0x0f0f0f0f))
        print(bin((n & 0x0f0f0f0f)<<4))
        
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        print(bin(n))
        print(bin(0xcccccccc))
        print(bin(n&0xcccccccc))
        print(bin((n&0xcccccccc)>>2))
        
        print(bin(0x33333333))
        print(bin(n & 0x33333333))
        print(bin((n & 0x33333333)<<2))        
        
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        print(bin(n))
        print(bin(0xaaaaaaaa))
        print(bin(n&0xaaaaaaaa))
        print(bin((n&0xaaaaaaaa)>>1))
        
        print(bin(0x55555555))
        print(bin(n & 0x55555555))
        print(bin((n & 0x55555555)<<1))  
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        print(bin(n))
        return n
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(98454165648))