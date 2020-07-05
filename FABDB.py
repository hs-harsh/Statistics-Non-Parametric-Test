A = "X Y X Y X Y X Y"
A = ' '.join(A.split())
A = list(map(str, A.split(" ")))
print(A)
N = len(A)
X, Y = [], []
for i in range(len(A)):
    if(A[i] == "X"):
        X.append(i+1)
    else:
        Y.append(i+1)
m, n = len(X), len(Y)
print(X, [abs(x-(N+1)/2) for x in X])
An = sum([abs(x-(N+1)/2) for x in X])
Fn = (m*(N+1)/2) - An
print(Fn)
