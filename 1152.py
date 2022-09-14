#단어의 개수

import sys
input = sys.stdin.readline
sen = list(input().split())
count = 0
for s in sen:
    if s != ' ':
        count+=1
print(count)
