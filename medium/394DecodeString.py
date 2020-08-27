class Solution:
    def decodeString(self, s):
        if len(s) == 0:
            return ""
        numArr = []
        strArr = []
        res = ''
        idx = 0
        while(idx < len(s)):
            if s[idx].isnumeric():
                numArr.append(int(s[idx]))
                idx += 1
                while s[idx].isnumeric():
                    n = numArr.pop()
                    n = n*10+int(s[idx])
                    numArr.append(n)
                    idx += 1
            elif s[idx] == '[':
                strArr.append(res)
                res = ''
                idx += 1
            elif s[idx] == ']':
                tmp = strArr.pop()
                count = numArr.pop()
                for i in range(count):
                    tmp += res
                res = tmp
                idx += 1    
            else:
                res += s[idx]
                idx += 1
        return res

class Solution2:
    def decodeString(self, s) :
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c==']':
                num = stack.pop()
                preString = stack.pop()
                curString = preString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
    
    
if __name__ == "__main__":
    sol = Solution2()
    Arr = '3[a]2[bc]'
    Arr1 = '3[a2[c]]'
    print(sol.decodeString(Arr1))