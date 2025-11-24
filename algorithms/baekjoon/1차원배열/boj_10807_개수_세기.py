

import sys 

cnt = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))[:cnt]
v = int(sys.stdin.readline())

print(nums.count(v)) #  매번 리스트 전체를 순회해야 함 → O(N)

# GPT


# import sys
# from collections import Counter

# cnt = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))[:cnt]
# v = int(sys.stdin.readline())

# counter = Counter(nums) # 처음에 딱 한 번 순회해서 모든 개수를 딕셔너리에 저장 → O(N), 그 후 O(1)에 조회 가능
# print(counter[v])
