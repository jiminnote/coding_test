import sys
from collections import Counter

N = int(sys.stdin.readline())

nums = []

for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)

print (round(sum(nums) / N))
print(sorted(nums)[N//2])

most_common = Counter(nums).most_common()
max_freq = Counter(nums).most_common()[0][1]

ad = [num for num, freq in most_common if freq == max_freq]
ad.sort()

if len(ad) == 1:
    print(ad[0])
else:
    print(ad[1])

print(abs(max(nums)-min(nums)))



