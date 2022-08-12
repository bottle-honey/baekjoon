#공유기 설치
from bisect import bisect_left, bisect_right
def count_by_range(array,left_value,right_value):
    left_index = bisect_left(array,left_value)
    right_index = bisect_right(array,right_value)
    return right_index-left_index
n,c = map(int,input().split())

homes = []

for _ in range(n):
    homes.append(int(input()))
homes.sort()

start = homes[0]
end = homes[n-1]

dist = (end-start)//(c-1)
# 12489
while start<=end:
    if count_by_range(homes,start,start+dist+1)>1:
        start = start+dist
    else:
        start = homes[0]
        dist-=1

print(dist)
