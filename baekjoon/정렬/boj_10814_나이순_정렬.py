import sys


N = int(sys.stdin.readline())

sign_list = []

for i in range(N):
    # age, name = map(sys.stdin.readline().split()) age = int , name = str이라서 TypeError
    age, name = sys.stdin.readline().split()
    sign_list.append((i,int(age),name))

sign_list.sort(key=lambda x: (x[1], x[0]))
# x[1] 기준으로 오름차순을 한 후 x[1]의 같은값에 대해서는 x[0] 기준으로 오름차순
for _,age,name in sign_list:
    print(age,name)




