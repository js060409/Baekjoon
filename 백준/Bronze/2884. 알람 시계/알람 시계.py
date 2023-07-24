H, M = map(int,input().split())



if H == 0  and M < 45:
    H = 23
    X = 45 - M
    M = 0
    M = 60 - X

elif H == 0 and M >= 45:
    H = 0
    M = M - 45

elif H > 0 and M < 45:
    H = H - 1
    X = 45 - M
    M = 0
    M = 60 - X

elif H > 0 and M >= 45:
    H = H
    M = M - 45

print(H , M)