st = "65	76	61	67	56 78	65	68	72"
nks = [5, 4]
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
