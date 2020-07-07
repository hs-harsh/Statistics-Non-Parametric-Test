X = "9.20	6.75	5.86	11.12	  7.44	  13.40"
Y = "7.80	12.36	8.20	11.00"
X = ' '.join(X.split())
Y = ' '.join(Y.split())
X = list(map(float, X.split(" ")))
Y = list(map(float, Y.split(" ")))
n, m = len(X), len(Y)

cnt = 0
for i in range(n):
    for j in range(m):
        if(X[i] < Y[j]):
            print("X  Y : " + str(X[i])+"  "+str(Y[j]))
            cnt += 1
print("U : "+str(cnt))
