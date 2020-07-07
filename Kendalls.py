# arr = [(14.58, 19.11), (15.28, 17.21), (19.26, 15.47), (19.92, 22.60), (16.19, 20.10), (12.46, 17.45),
#        (14.95, 24.77), (16.10, 17.70), (19.10, 19.46), (11.20, 23.01), (12.12, 20.45), (13.90, 19.96)]
# arr = [(1, 3),  (10, 12),  (9, 7),  (7, 5),  (16, 18)]
arr = [(1, 15), (6, 12),  (7, 13), (9, 9)]
N = len(arr)

concordant, discordant = 0, 0
Aij = 0
for i in range(N):
    for j in range(i+1, N):
        Xi, Yi = arr[i]
        Xj, Yj = arr[j]
        if((Xi-Xj)*(Yi-Yj) > 0):
            concordant += 1
            Aij += 1
        elif((Xi-Xj)*(Yi-Yj) < 0):
            discordant += 1
            Aij -= 1
Tau = 2*Aij/(N*(N-1))
print("concordant discordant : "+str(concordant)+" "+str(discordant))
print("Tau : " + str(Tau))
