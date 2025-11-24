H,M = map(int,input().split())
P = int(input())

if P > 60:
    H=H+(P//60)
    P=P%60

m = M+P

if m > 59 :
    H = H+1 
    m = m - 60  

if H ==24:
    H=0

elif H > 24:
    H=H-24
    
print(H,m)