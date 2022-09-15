# 기타줄
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
#패키지
P = []
#낱개
O = []

for _ in range(m):
    a,b = map(int,input().split())
    P.append(a)
    O.append(b)
min_P = min(P)
min_O = min(O)
a,b = n//6,n%6
result = min(min_P,min_O*6) * a + min(min_P,min_O*b)
print(result)