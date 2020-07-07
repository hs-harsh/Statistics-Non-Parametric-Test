import numpy as np
arr = "16.21 15.80 14.25 10.23 36.68 23.06 14.16 15.70 5.65 22.00 17.80 32.84"
arr = ' '.join(arr.split())
arr = list(map(float, arr.split(" ")))
n = len(arr)
arr.sort()
print(n)

Fn = [("x < "+str(arr[0]), 0)]
for i in range(n-1):
    Fn.append(((str(arr[i])+"< x < "+str(arr[i+1])), (i+1)/n))
Fn += [("x > "+str(arr[n-1]), 1)]
for i in range(len(Fn)):
    print(Fn[i])


def CDFExponential(lamb, x):  # lamb = lambda
    if x <= 0:
        cdf = 0
    else:
        cdf = 1-np.exp(-lamb*x)
    return cdf


Exp = []
for i in range(n):
    Exp.append((arr[i], CDFExponential(0.1, arr[i])))

for i in range(n):
    a, b = Fn[i]
    print(a, b, Exp[i][1], abs(b-Exp[i][1]))
# print(Exp)
