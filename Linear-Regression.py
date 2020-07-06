import numpy as np
X = "1	1.5	2	3	3.25	4	4.5	6"
Y = "-5	 -4	-2.5	0	1	8	12	25"
X = ' '.join(X.split())
Y = ' '.join(Y.split())
X = list(map(float, X.split(" ")))
Y = list(map(float, Y.split(" ")))
n = len(X)
m = 2

Yi, Xi = sum(Y), sum(X)
Ybar, Xbar = Yi/n, Xi/n
Xi2 = sum([x**2 for x in X])
Xi3 = sum([x**3 for x in X])
Xi4 = sum([x**4 for x in X])
XiYi = sum([X[i]*Y[i] for i in range(n)])
Xi2Yi = sum([(X[i]**2)*Y[i] for i in range(n)])

# A*Beta = B  || Beta --> coefficients
A = np.array([[n, Xi, Xi2],
              [Xi, Xi2, Xi3],
              [Xi2, Xi3, Xi4]])
B = np.array([Yi, XiYi, Xi2Yi]).T
print(A)
print(B)
Beta = np.dot(B, np.linalg.inv(A))
print(Beta)
