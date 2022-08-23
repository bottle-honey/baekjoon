#파이프 옮기기 1
import sys
input = sys.stdin.readline

n = int(input())
house = []

for _ in range(n):
    house.append(list(input().split()))
result = 0
# shape = [h,v,d]
def dfs(x,y,shape):
    global result
    if x==n-1 and y == n-1:
        result+=1
        return
    if shape == 'h':
        if y+1 < n and house[x][y+1]=='0':
            dfs(x,y+1,'h')
            if x+1<n and house[x+1][y+1]=='0':
                dfs(x+1,y+1,'d')
    elif shape == 'v':
        if x+1 <n and house[x+1][y]=='0':
            dfs(x+1,y,'v')
            if y+1<n and house[x+1][y+1]=='0':
                dfs(x+1,y+1,'d')
    elif shape == 'd':
        if x+1 <n and house[x+1][y]=='0':
            dfs(x+1,y,'v')
            if y+1<n and house[x+1][y+1]=='0':
                dfs(x+1,y+1,'d')
        elif y+1<n and house[x][y+1]=='0':
            dfs(x,y+1,'h')

dfs(0,1,'h')

print(result)