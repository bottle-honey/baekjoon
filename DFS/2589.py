#보물섬
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

map = []
for _ in range(n):
    map.append(list(input().rstrip('\n')))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
for i in range(n):
    for j in range(m):
        #dfs
        if map[i][j] == 'L':
            stk = [(i,j,0)]
            visited = [[False]*m for _ in range(n)]
            
            while stk:
                x,y,distance = stk.pop()
                visited[x][y] = True
                # 종착지 판별 변수
                able = 0
                for d in range(len(dx)):
                    nx= x+dx[d]
                    ny=y+dy[d]
                    if nx<0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                        continue
                    if map[nx][ny] == 'L':
                        stk.append((nx,ny,distance+1))
                        able+=1
                if able == 0:
                    result = max(result,distance)
print(result)