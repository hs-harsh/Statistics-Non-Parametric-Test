import numpy as np
# arr = "59.42,   52.10,   64.22,   71.96,   56.46,   17.80,   39.02,   66.90,   75.30,   2.75,   29.16,   9.05,   14.70, 27.15, 48.80, 16.60"
arr = "29.7, 26.1, 32.2, 36.0, 8.8, 19.5, 38.7, 43.5, 5.6, 11.4"
arr = list(map(float, arr.replace(" ", "").split(",")))
n = len(arr)
arr = sorted(arr)
print(n, arr)
if(n % 2 != 0):
    print("Median : " + str(arr[n//2]))
else:
    print("Median : " + str((arr[n//2]+arr[n//2-1])/2))
q1, q3 = 0, 0
p1, p2 = 0.25, 0.75
p = 0.65
res = 0
for i in range(n-1):
    if((i+1)/(n+1) < p1 < (i+2)/(n+1)):
        print((i+1)/(n+1), (i+2)/(n+1))
        print(i+1)
        print(arr[i], arr[i+1])
        q1 = ((i+2)/(n+1)-p1)*arr[i] / (1/(n+1)) + \
            (p1-(i+1)/(n+1))*arr[i+1]/(1/(n+1))

    if((i+1)/(n+1) < p2 < (i+2)/(n+1)):
        print((i+1)/(n+1), (i+2)/(n+1))
        print(i+1)
        print(arr[i], arr[i+1])
        q3 = ((i+2)/(n+1)-p2)*arr[i] / (1/(n+1)) + \
            (p2-(i+1)/(n+1))*arr[i+1]/(1/(n+1))

    # if((i+1)/(n+1) < p < (i+2)/(n+1)):
    #     # print((i+1)/(n+1), (i+2)/(n+1))
    #     # print(i+1)
    #     # print(arr[i], arr[i+1])
    #     # print((p-(i+1)/(n+1)) / (1/(n+1)) + ((i+2)/(n+1)-p)/(1/(n+1)))
    #     res = ((i+2)/(n+1)-p)*arr[i] / (1/(n+1)) + \
    #         (p-(i+1)/(n+1))*arr[i+1]/(1/(n+1))
print(q1, q3, q3-q1)
# print(res)
