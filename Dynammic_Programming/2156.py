import sys
input = sys.stdin.readline

n = int(input())

array = []
for _  in range(n):
    array.append(int(input()))

dp1 = [0] * n
dp2 = [0] * n

for i in range(n):
    if i-2 >=0:
        dp1[i] = max(dp1[i-2],dp2[i-2]) + array[i]
    else:
        dp1[i] = array[i]
    if i-1 >=0 :
        dp2[i] = dp1[i-1] + array[i]
    else:
        dp2[i] = array[i]

print((max(max(dp1),max(dp2))))