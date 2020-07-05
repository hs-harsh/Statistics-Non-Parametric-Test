X = "9.3 8.8 10.7 11.5 8.2 9.7 10.3 8.6 11.3 10.7 9.9 11.2 9.0 9.8 9.3 9.9 10.3 10.0 10.1 9.6 10.4"
Median = 9.9
X = ' '.join(X.split())
X = list(map(float, X.split(" ")))
X = list(filter(lambda a: a != Median, X))
n = len(X)

D = [abs(round(X[i] - Median, 5)) for i in range(n)]
XD = [[X[i], D[i]] for i in range(n)]
XD = sorted(XD, key=lambda x: abs(x[1]))
XDR = []
Tplus, Tminus = 0, 0
for i in range(n):
    x, d = X[i], abs(round(X[i] - Median, 5))
    sign = ""
    idx = 0
    for i in range(n):
        if d in XD[i]:
            idx = i
            break

    rank = idx+(D.count(d)-1)/2 + 1
    if(x - Median > 0):
        sign = "+"
        Tplus += rank
    else:
        Tminus += rank
        sign = "-"
    XDR.append([x, sign, d, rank])

for i in range(n):
    print(XDR[i])
print("T+ : " + str(Tplus))
print("T- : " + str(Tminus))
