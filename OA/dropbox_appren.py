
import time


def keyboard1(wordList, keypads):
    arrSet = [set() for _ in range(len(wordList)) ]
    arrRes = [0] * len(keypads)
    for i in range(len(wordList)):
        arrSet[i] = set(wordList[i])
    # print(arrSet)
    for i in range(len(keypads)):
        kSet = set(keypads[i])
        # print(kSet)
        for wSet in arrSet:
            if wSet.issubset(kSet):
                arrRes[i] += 1
    return arrRes

def keyboard2(wordList, keypads):
    wordDict = dict()
    res = [0] * len(keypads)
    for word in wordList:
        if word not in wordDict:
            wordDict[word] = [set(word), 1]
        else:
            wordDict[word][1] += 1
    print(wordDict)


    for i, keypad in enumerate(keypads):
        keypadSet = set(keypad)
        for keyWD in wordDict:
            if keypad[0] not in wordDict[keyWD][0]:
                continue
            cnt = 0
            for w in keyWD:
                if w not in keypadSet:
                     break
                cnt += 1
            if cnt == len(keyWD):
                res[i] += wordDict[keyWD][1]
    return res
    

def numKeypadSolutions(wordlist, keypads):
    # Write your code here
    wordDict = dict()
    res = [0] * len(keypads)
    for word in wordlist:
        wordSet = set(word)
        key = tuple(sorted(list(wordSet)))
        if key not in wordDict:
            wordDict[key] = [wordSet, 1]
        else:
            wordDict[key][1] += 1
    
    for ind, keypad in enumerate(keypads):
        keypadSet = set(keypad)
        for key in wordDict:
            if keypad[0] not in wordDict[key][0]:
                continue
            cnt = 0
            if wordDict[key][0].issubset(keypadSet):
                res[ind] += wordDict[key][1]
    return res


def numKeypadSolutions(wordlist, keypads):
    # Write your code here
    wordDict = dict()
    res = [0] * len(keypads)
    for word in wordlist:
        wordSet = set(word)
        if len(wordSet) > 7:
            continue
        if word not in wordDict:
            wordDict[word] = [wordSet, 1]
        else:
            wordDict[word][1] += 1
    
    for ind, keypad in enumerate(keypads):
        keypadSet = set(keypad)
        for key in wordDict:
            if keypad[0] not in wordDict[key][0]:
                continue
            cnt = 0
            if wordDict[key][0].issubset(keypadSet):
                res[ind] += wordDict[key][1]
    return res

import collections
def numKeypadSolutions(wordlist, keypads):
    # Write your code here
    trie = dict()
    for word in wordlist:
        for i in word:
                        
    return res

    
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = 0
        

class Trie:
    def __init__(self):
        self.root = TrieNode()    
        
    def insert(self, word):
        cur = self.root
        for letter in word:
            cur = cur.children[letter]
        cur.is_word += 1
        
    def dfs(self, keypad):



if __name__ == "__main__":
    wordList = ['APPLES', 'PLEAS', 'PLEASE']
    keypads = ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY']
    # expected 0 1 3 2 0
    start1 = time.time()
    print(keyboard1(wordList, keypads))
    print(time.time() - start1)

    start2 = time.time()
    print(keyboard2(wordList, keypads))
    print(time.time() - start2)