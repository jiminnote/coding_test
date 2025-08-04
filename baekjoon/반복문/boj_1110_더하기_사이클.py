N = int(input())
cnt = 0

c = [int(i) for i in str(N).zfill(2)]  # 항상 두 자리로 패딩

while True:
    cnt += 1
    s = sum(c)
    c.append(s % 10)  # 합의 일의 자리만 사용
    c.pop(0)
    num = int("".join(map(str, c)))
    if num == N:
        break

print(cnt)