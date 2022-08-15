# 나무 자르기
import sys
input = sys.stdin.readline

n,m=map(int,input().split())

trees = list(map(int,input().split()))

start = 1
end = max(trees)
result = 0
while start<=end:
    sum = 0
    # mid : h : 절단기의 높이
    mid = (start+end)//2
    for tree in trees:
        if tree > mid:
            sum += tree-mid
    if sum >= m:
        result = max(result,mid)
        start = mid + 1
    else:
        end = mid - 1
print(result)