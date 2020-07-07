st = "75.91 71.97 46.76 36.80 68.29 36.35 63.01 47.77 56.94 82.43 35.49 93.75"
nks = [5, 4, 3]
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
