#숫자 카드
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

def count_by_range(array,left_value,right_value):
    left_index=bisect_left(array,left_value)
    right_index=bisect_right(array,right_value)
    
    return right_index - left_index
cards.sort()
result = []
for target in targets:
    result.append(count_by_range(cards,target,target))
for re in result:
    print(re,end=' ')
    
    
    