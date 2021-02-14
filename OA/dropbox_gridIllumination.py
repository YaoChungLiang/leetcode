import random
# Complete the checkIllumination function below.
def checkIllumination(N, lamps, queries):
    n = len(queries)
    m = len(lamps)
    res = ["" for _ in range(n) ]
    for i in range(n):
        flag = 0
        s = set()
        while len(s) < m :
            j = random.randint(0, m-1)
            if j in s:
                continue
            s.add(j)
            if queries[i][0]-2 < lamps[j][0] < queries[i][0]+2 and queries[i][1]-2 < lamps[j][1] < queries[i][1]+2:
                continue
            if checkOnPath(lamps[j], queries[i]):
                flag = 1
                break
        if flag:
            res[i] = "LIGHT"
        else:
            res[i] = "DARK"
    return res 

def checkOnPath(lamp, query):
    denom = lamp[1] - query[1]
    nom = lamp[0] - query[0]
    if denom == 0 or nom == 0 or abs(denom/nom) == 1:
        return True
    return False


import collections
# Complete the checkIllumination function below.
def checkIllumination(N, lamps, queries):
    dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
    lamp_set = {(x,y) for x,y in lamps}
    hori = collections.Counter(x for x,y in lamps)
    vert = collections.Counter(y for x,y in lamps)
    diag = collections.Counter(x-y for x,y in lamps)
    anti_diag = collections.Counter(x+y for x,y in lamps)

    
    res = []
    for x, y in queries:
        for dx,dy in dirs:
            i,j = x+dx, y+dy
            if (i,j) in lamp_set:
                lamp_set.remove((i,j))
                hori[i] -= 1
                vert[j] -= 1
                diag[i-j] -= 1
                anti_diag[i+j] -= 1
        if hori[x] > 0 or vert[y] > 0 or diag[x-y] > 0 or anti_diag[x+y] > 0:
            res.append("LIGHT")
        else:
            res.append("DARK")
        for dx,dy in dirs:
            i,j = x+dx, y+dy
            if (i,j) not in lamp_set:
                lamp_set.add((i,j))
                hori[i] += 1
                vert[j] += 1
                diag[i-j] += 1
                anti_diag[i+j] += 1
    return res


# pass

import collections
# Complete the checkIllumination function below.
def checkIllumination(N, lamps, queries):
    dirs = []
    for i in range(-1,2):
        for j in range(-1,2):
            dirs.append((i,j))
    lamp_set = {(x,y) for x,y in lamps}
    hori = collections.Counter(x for x,y in lamps)
    vert = collections.Counter(y for x,y in lamps)
    diag = collections.Counter(x-y for x,y in lamps)
    anti_diag = collections.Counter(x+y for x,y in lamps)

    res = []
    for x, y in queries:
        turned_off = []
        for dx,dy in dirs:
            i,j = x+dx, y+dy
            if (i,j) in lamp_set:
                lamp_set.remove((i,j))
                turned_off.append((i,j))
                hori[i] -= 1
                vert[j] -= 1
                diag[i-j] -= 1
                anti_diag[i+j] -= 1
                
        if hori[x] > 0 or vert[y] > 0 or diag[x-y] > 0 or anti_diag[x+y] > 0:
            res.append("LIGHT")
        else:
            res.append("DARK")
            
        for i,j in turned_off:
            lamp_set.add((i,j))
            hori[i] += 1
            vert[j] += 1
            diag[i-j] += 1
            anti_diag[i+j] += 1            
    return res



import collections
# Complete the checkIllumination function below.
def checkIllumination(N, lamps, queries):
    dirs = []
    for i in range(-1,2):
        for j in range(-1,2):
            dirs.append((i,j))
    lamp_set = {(x,y) for x,y in lamps}
    hori = collections.Counter(x for x,y in lamps)
    vert = collections.Counter(y for x,y in lamps)
    diag = collections.Counter(x-y for x,y in lamps)
    anti_diag = collections.Counter(x+y for x,y in lamps)
    n_query = len(queries)
    res = ["LIGHT" for _ in range(n_query)]
    for k in range(n_query):
        x, y = queries[k][0], queries[k][1]
        turned_off = []
        for dx,dy in dirs:
            i,j = x+dx, y+dy
            if (i,j) in lamp_set:
                lamp_set.remove((i,j))
                turned_off.append((i,j))
                hori[i] -= 1
                vert[j] -= 1
                diag[i-j] -= 1
                anti_diag[i+j] -= 1
                
        if hori[x] > 0 or vert[y] > 0 or diag[x-y] > 0 or anti_diag[x+y] > 0:
            pass
        else:
            res[k] = "DARK"
            
        for i,j in turned_off:
            lamp_set.add((i,j))
            hori[i] += 1
            vert[j] += 1
            diag[i-j] += 1
            anti_diag[i+j] += 1            
    return res