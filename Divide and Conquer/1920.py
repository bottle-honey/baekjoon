# 수 찾기
from bisect import bisect_left, bisect_right

def count_by_range(array,left_value,right_value):
    left_index = bisect_left(array,left_value)
    right_index = bisect_left(array,right_value)
    return right_index - left_index

n = int(input())
array = list(map(int,input().split()))
array.sort()
m = int(input())
targets = list(map(int,input().split()))

for target in targets:
    if count_by_range(array,target,target+1):
        print(1)
    else:
        print(0)