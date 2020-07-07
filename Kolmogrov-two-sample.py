from math import comb
X = "1 4 5"
Y = "2 3 6 7"
# xyyxxyy
X = ' '.join(X.split())
Y = ' '.join(Y.split())
X = list(map(float, X.split(" ")))
Y = list(map(float, Y.split(" ")))
m, n = len(X), len(Y)

A = []
for i in range(m):
    A.append([X[i], 'X'])
for i in range(n):
    A.append([Y[i], 'Y'])
A.sort(key=lambda x: x[0])
print(A)
N = len(A)

path = []
u, v = 0, 0
for i in range(N):
    path.append((u, v))
    if(A[i][1] == 'Y'):
        v += 1
    else:
        u += 1
path.append((u, v))
print(path)
d = -float('inf')
for i in range(len(path)):
    u, v = path[i]
    d = max(d, abs(u/m - v/n))
print("d : "+str(d))

pInside = []
for i in range(m+1):
    for j in range(n+1):
        if((j-(n/m)*i - n*d)*(j-(n/m)*i + n*d) < 0):
            pInside.append((i, j))

dp = [[0]*(n+1) for i in range((m+1))]
for i in range(m+1):
    for j in range(n+1):
        if((i, j) in pInside):
            if(i == 0 or j == 0):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
for i in range(m+1):
    print(dp[i])
prob = 1 - dp[m][n]/(comb(N, m))
print("Prob(D>d) = " + str(prob))
