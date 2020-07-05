st = "79	13	83	36	90 94	88	93	75 10	37	72	77	28"
nks = [5, 4, 5]
k = len(nks)

st = ' '.join(st.split())
arr = list(map(float, st.split(" ")))
N = len(arr)
print(N, arr)
print('--------------------------------------\n')

narr = sorted(arr)
farr = [[arr[i], narr.index(arr[i])+1+(narr.count(arr[i])-1)/2]
        for i in range(N)]
cnt = 0
rowSum = []
for i in range(k):
    print("Row - " + str(i+1)+" : " + str(farr[cnt:cnt+nks[i]]))
    rowSum.append(sum([farr[j][1]
                       for j in range(cnt, cnt+nks[i])]))
    cnt += nks[i]
print("Row Sum : "+str(rowSum))
rowSumSquare = [(rowSum[i]**2)/(nks[i]) for i in range(k)]
print("Row Sum Square: "+str(rowSumSquare))
H = (12*(sum(rowSumSquare)))/(N*(N+1)) - 3*(N+1)
print("Final H : " + str(H))
