A, B, C = map(int, input().split())

if A == B == C:
    result = 10000 + A * 1000
elif A == B or A == C:
    result = 1000 + A * 100
elif B == C:
    result = 1000 + B * 100
else:
    result = max(A, B, C) * 100

print(result)