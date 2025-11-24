H,M = map(int,input().split())

M = M-45
if H == 0:
    H == 25
if M < 0 :
    if H == 0:
        H = 24
    H = H-1
    M = M + 60


print(H,M)