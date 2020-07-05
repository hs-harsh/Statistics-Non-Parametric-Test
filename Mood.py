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
print(X, [(x-(N+1)/2)**2 for x in X])
Mn = sum([(x-(N+1)/2)**2 for x in X])
print(Mn)
