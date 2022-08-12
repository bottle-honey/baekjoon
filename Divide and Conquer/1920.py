# 수 찾기
n = int(input())
array = list(map(int,input().split()))
array.sort()
m = int(input())
targets = list(map(int,input().split()))

for target in targets:
    start = 0
    end = n-1
    val = False
    while(start<=end):
        mid = (start+end)//2
        if array[mid] == target:
            val = True
            break
        elif array[mid] < target:
            start=mid+1
        else:
            end = mid-1
    if val:
        print(1)
    else:
        print(0)