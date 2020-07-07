import numpy as np
X = "-6	-4	 -3	-2	    2	    3	4	6"
Y = " 36	 15	  9	1	  -1	    1	7	25"
# X="1 1.5	2	3	3.25	4	4.5	6"
# Y="-7	 -6	-5	 -2	 -1	 6	10	24"
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

print("Xi Yi : "+str(Xi)+" "+str(Yi))
print("Xi2 : "+str(Xi2)+" "+str([x**2 for x in X]))
print("Xi3 : "+str(Xi3)+" "+str([x**3 for x in X]))
print("Xi4 : "+str(Xi4)+" "+str([x**4 for x in X]))
print("XiYi : "+str(XiYi)+" "+str([X[i]*Y[i] for i in range(n)]))
print("Xi2Yi : "+str(Xi2Yi)+" "+str([(X[i]**2)*Y[i] for i in range(n)]))

# A*Beta = B  || Beta --> coefficients
A = np.array([[n, Xi, Xi2],
              [Xi, Xi2, Xi3],
              [Xi2, Xi3, Xi4]])
B = np.array([Yi, XiYi, Xi2Yi]).T
print("--------------------------------------------")
print(A)
print(B)
Beta = np.dot(B, np.linalg.inv(A))
print(Beta)
