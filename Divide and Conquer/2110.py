#공유기 설치
n,c = map(int,input().split())

homes = []

for _ in range(n):
    homes.append(int(input()))
homes.sort()

start = homes[0]
end = homes[n-1]

dist = (end-start)//(c-1)
able = 1

while True:
    start = homes[0]
    for i in range(1,n):
        if homes[i]-start >= dist:
            able+=1
            start = homes[i]
    if able < c:
        dist-=1
    else:
        break

print(dist)
