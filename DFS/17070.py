#파이프 옮기기 1
import sys
input = sys.stdin.readline

n = int(input())
house = []

for _ in range(n):
    house.append(list(input().split()))
result = 0
stk = [(0,1,'h')]
while stk:
    x,y,shape = stk.pop()
    if x==n-1 and y==n-1:
        result+=1
        continue
    if shape == 'h':
        if y+1 < n and house[x][y+1]=='0':
            stk.append((x,y+1,'h'))
        if x+1 < n and y+1<n and house[x+1][y] == '0' and house[x+1][y+1]=='0' and house[x][y+1] == '0':
            stk.append((x+1,y+1,'d'))
    elif shape == 'v':
        if x+1 <n and house[x+1][y]=='0':
            stk.append((x+1,y,'v'))
        if x+1 < n and y+1<n and house[x+1][y] == '0' and house[x+1][y+1]=='0' and house[x][y+1] == '0':
            stk.append((x+1,y+1,'d'))
    elif shape == 'd':
        if x+1 <n and house[x+1][y]=='0':
            stk.append((x+1,y,'v'))
        if y+1<n and house[x][y+1]=='0':
            stk.append((x,y+1,'h'))
        if x+1<n and y+1<n and house[x+1][y] == '0' and house[x+1][y+1]=='0' and house[x][y+1] == '0':
            stk.append((x+1,y+1,'d'))
    
print(result)