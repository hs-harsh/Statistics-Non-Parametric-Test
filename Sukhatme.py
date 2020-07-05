X = " -3	-1.5	-1	0.5	1.5	2.75"
Y = "-5	-2	-0.5	1	3	4"
X = ' '.join(X.split())
Y = ' '.join(Y.split())
X = list(map(float, X.split(" ")))
Y = list(map(float, Y.split(" ")))
n, m = len(X), len(Y)

cnt = 0
for i in range(n):
    for j in range(m):
        if(0 < X[i] < Y[j] or Y[j] < X[i] < 0):
            print(X[i], Y[j])
            cnt += 1
print('-----------------------------------')
print("D : " + str(cnt))
