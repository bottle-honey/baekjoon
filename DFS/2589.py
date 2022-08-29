#보물섬
import sys
from collections import deque
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
        if map[i][j] == 'L':
            distance = [[-1]*m for _ in range(n)]
            distance[i][j] = 0
            q = deque([(i,j)])
            while q:
                x,y = q.popleft()
                for d in range(len(dx)):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >=n or ny <0 or ny >= m or map[nx][ny] != 'L':
                        continue
                    if distance[nx][ny] == -1:
                        distance[nx][ny] = distance[x][y] + 1
                        q.append((nx,ny))
                        result = max(result,distance[nx][ny])
print(result)

            