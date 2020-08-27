import heapq
class Solution:
    def topKFrequent(self, words, k):
        dic = dict()
        heap = []
        res = []
        for w in words:
            if w not in dic:
                dic[w] = 0
            dic[w] -= 1
        if len(dic) == k:
            return [w for w in dic]
        for key in dic:
            heappush(heap, (dic[key], key))
        tmp = []
        pre = 0
        for _ in range(k):
            freq, word = heappop(heap)
            if freq != pre:
                pre = freq
                for i in sorted(tmp):
                    res.append(i)
                tmp = [word]
            else:
                tmp.append(word)
                
        if tmp:
            for i in sorted(tmp):
                res.append(i)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    num = 4
    print(sol.topKFrequent(words, num))