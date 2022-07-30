n=int(input())
k=list(input().split())
print(k)
x,y=1,1

for i in k:
    if i=='L':
        y-=1
        if y==0:
            y=1
    if i=='R':
        y+=1
        if y==n+1:
            y=n
    if i=='U':
        x-=1
        if x==0:
            x=1
    if i=='D':
        x+=1
        if x==n+1:
            x=n
    print(x,y)