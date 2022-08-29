# 랜선 자르기
import sys
input = sys.stdin.readline

k,n = map(int,input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

lines.sort()

start= 1
end = lines[-1]
result = 0

while start<=end:
    mid = (start+end)//2
    count = 0
    for line in lines:
        count = count + (line//mid)
    if count >=n:
        start = mid + 1
        result= max(result,mid)
    else:
        end = mid - 1

print(result)