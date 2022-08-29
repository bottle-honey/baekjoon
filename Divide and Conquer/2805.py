# 나무 자르기
import sys
# 전역변수 : trees, m, result
result = []
input = sys.stdin.readline
def binary_search(start,end):
    if start>end:
        return
    sum = 0
    mid = (start+end)//2
    for tree in trees:
        if tree > mid:
            sum += tree - mid
    if sum >= m:
        result.append(mid)
        binary_search(mid+1,end)
    else:
        binary_search(start,mid-1)

n,m=map(int,input().split())        
trees = list(map(int,input().split()))
start = 0
end = max(trees)

binary_search(1,max(trees))
if result:
    print(max(result))
else:
    print(0)