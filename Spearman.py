R = "2	1	3	5	4"
S = "1	2	3	4	5"
R = ' '.join(R.split())
S = ' '.join(S.split())
R = list(map(float, R.split(" ")))
S = list(map(float, S.split(" ")))
n = len(R)
print(R, S)

D = [R[i]-S[i] for i in range(n)]
RC = 1 - 6*(sum([D[i]**2 for i in range(n)]))/(n*((n**2) - 1))
print("RC : " + str(RC))
