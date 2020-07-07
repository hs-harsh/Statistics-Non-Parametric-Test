arr = "0.18    0.20   0.21   0.29   0.35   0.43    0.48    0.51   0.58   0.59"
arr = ' '.join(arr.split())
arr = list(map(float, arr.split(" ")))
n = len(arr)
arr.sort()

Fn = [("x < "+str(arr[0]), 0)]
for i in range(n-1):
    Fn.append(((str(arr[i])+"< x < "+str(arr[i+1])), (i+1)/n))
Fn += [("x > "+str(arr[n-1]), 1)]
for i in range(len(Fn)):
    print(Fn[i])
