# 01타일
n = int(input())
left,right = 1,2
DIV = 15746
for i in range(3,n+1):
    left,right = right%DIV, (left+right)%DIV
if n == 1:
    print(1)
else:
    print(right)

