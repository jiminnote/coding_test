m,n = map(int,input().split()) 
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(min(b))
print(max(a))
