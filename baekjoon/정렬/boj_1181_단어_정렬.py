import sys

N = int(sys.stdin.readline())
words = list(set([input().strip() for _ in range(N)]))

words.sort(key=lambda x: (len(x), x))
print(words)
for word in words:
    print(word)

