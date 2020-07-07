st = "14.25	8.06	4.80	6.36	17.90	13.50	7.28	10.45	22.10 20.50	23.40	11.45	6.55	9.10	18.00	15.60	19.90	8.00"
nks = [9, 9]
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
