#공유기 설치
import sys
input = sys.stdin.readline
n,c = map(int,input().split())
homes = []
for _ in range(n):
    homes.append(int(input()))
homes.sort()

start = 1
end = homes[-1]-homes[0]
result = 0

while start<=end:
    dist = (start+end)//2
    pivot = homes[0]
    count = 1
    for i in range(1,n):
        if homes[i]-pivot >= dist:
            count+=1
            pivot = homes[i]
    if count >= c:
        result = max(result,dist)
        start = dist+1
    else:
        end = dist-1

print(result)
