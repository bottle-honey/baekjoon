import sys
input = sys.stdin.readline
n = int(input())
words = []
for _ in range(n):
    word = input().rstrip('\n')
    if word in words:
        continue
    else: 
        words.append(word)
words.sort()
words.sort(key = lambda x:len(x))
for word in words:
    print(word)