X = "65	76	61	67	56"
Y = "78	66	68	72"
X = ' '.join(X.split())
Y = ' '.join(Y.split())
X = list(map(float, X.split(" ")))
Y = list(map(float, Y.split(" ")))
n, m = len(X), len(Y)

cnt = 0
for i in range(n):
    for j in range(m):
        if(X[i] < Y[j]):
            cnt += 1
print(cnt)
