X = "31.32	37.75	35.18"
Y = "25.73	35.95"

X = ' '.join(X.split())
Y = ' '.join(Y.split())
X = list(map(float, X.split(" ")))
Y = list(map(float, Y.split(" ")))
n, m = len(X), len(Y)

A = []
for i in range(n):
    A.append([X[i], 'X'])
for i in range(m):
    A.append([Y[i], 'Y'])
A.sort(key=lambda x: x[0])
print(A)
N = len(A)
A = [A[i][1] for i in range(N)]
print(A)
X, Y = [], []
for i in range(len(A)):
    if(A[i] == "X"):
        X.append(i+1)
    else:
        Y.append(i+1)
print(X, [(x-(N+1)/2)**2 for x in X])
Mn = sum([(x-(N+1)/2)**2 for x in X])
print(Mn)
