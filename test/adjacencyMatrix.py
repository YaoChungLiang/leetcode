# Seattle = 0
# Salt Lake City = 1
# Las Vegas = 2
# Los Angeles = 3
# San Francisco = 4
d = dict()
d[(0,1)] = 832
d[(0,4)] = 808
d[(1,4)] = 736
d[(1,2)] = 421
d[(2,3)] = 270
d[(3,4)] = 382
A = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        if i==j:
            A[i][j] = 0
        elif (i,j) in d:
            A[i][j] = d[(i,j)]
            A[j][i] = d[(i,j)]
        elif (j,i) in d:
            A[i][j] = d[(j,i)]
            A[j][i] = d[(j,i)]
        else:
            A[i][j] = -1
print(A)