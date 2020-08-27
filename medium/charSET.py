
def isUnique(string):
    charSet = [False]*10
    for char in string:
        if charSet[int(char)] :
            return False
        charSet[int(char)] = True
        
        
print(isUnique('0123421'))
    