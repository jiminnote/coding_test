X = int(input()) # 영수증 총 금액
N = int(input()) # 물건 종류의 개수
c = 0


for i in range(N):
    a, b = map(int,input().split())
    c += (a*b)

if c==X:
    print('Yes')
else:
    print('No')