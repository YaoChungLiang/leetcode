import heapq
def NoDupStr(s, ch_limit):
    d = dict()
    for c in s:
        c = -ord(c)
        if c not in d:
            d[c] = 0
        d[c] += 1
    q = []
    res = []
    for k, v in d.items():
        heapq.heappush(q,(k,v))
    while q:
        c1, v1 = heapq.heappop(q)
        c1 = chr(-c1)
        if res and c1 == res[-1][0] not : break
        if v1 >= ch_limit:
            res.append(c1*ch_limit)
            v1 -= ch_limit
        else:
            res.append(c1*v1)
            v1 = 0
        if not q: break
        c2, v2 = heapq.heappop(q)
        c2 = chr(-c2)
        if not v1:
            if v2 >= ch_limit:
                res.append(c2*ch_limit)
                v2 -= ch_limit
            else:
                res.append(c2*v2)
                v2 = 0
        else:
            res.append(c2)
            v2 -= 1
        if v1:
            heapq.heappush(q,(-ord(c1), v1))
        if v2:
            heapq.heappush(q,(-ord(c2), v2))
    return ''.join(res)


if __name__ == "__main__":
    s = 'zzxxzzfbbbbbaa'
    limit = 1
    print(NoDupStr(s,limit))
