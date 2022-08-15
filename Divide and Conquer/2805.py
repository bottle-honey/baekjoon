# 나무 자르기
import sys
input = sys.stdin.readline

n,m=map(int,input().split())

trees = list(map(int,input().split()))
trees.sort()
start = 0
end = max(trees)
result = 0
while start<=end:
    count = 0
    
    # mid : h : 절단기의 높이
    mid = (start+end)//2
    start_t = 0
    end_t = n-1
    min_idx = n-1
    while start_t <= end_t:
        mid_t = (start_t + end_t)//2
        if trees[mid_t] >= mid:
            min_idx = min(min_idx,mid_t)
            start_t = mid_t+1
        else:
            end_t = mid_t-1
    count = sum(trees[min_idx:]) - ((n-min_idx) * mid)
    if count >= m:
        result = max(result,mid)
        start = mid + 1
    else:
        end = mid - 1

print(result)