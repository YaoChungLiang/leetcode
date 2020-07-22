class Solution:
    def validIPAddress(self, IP: str) -> str:
        arr = []
        number = set(['0','1','2','3','4','5','6','7','8','9'])
        alpha = set(['a','b','c','d','e','f','A','B','C','D','E','F'])
        if '.' in IP:
            arr = IP.split('.')
            if len(arr) != 4 or "" in arr:
                return "Neither"
            for i in arr:
                for j in i:
                    if j not in number:
                        return "Neither"
                if int(i)> 255 or len(i) >= 4 or (len(i) != 1 and i[0] == '0'):
                    return "Neither"
            return "IPv4"
            
        else:
            arr = IP.split(':')
            if len(arr) != 8 or "" in arr:
                return "Neither"
            for i in arr:
                if len(i) > 4 or (len(i) == 1 and i not in '0fF'):
                    return "Neither"
                for j in i:
                    if j not in number and j not in alpha:
                        return "Neither"
            return "IPv6"
if __name__ == "__main__":
    grid = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    sol = Solution()
    print(sol.validIPAddress(grid))