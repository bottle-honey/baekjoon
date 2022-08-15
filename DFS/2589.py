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
            visited = [[False]*m for _ in range(n)]
            board = [[0]*m for _ in range(n)]
            #BFS
            q = deque([(i,j)])
            while q:
                x,y = q.popleft()
                visited[x][y] = True
                result = max(result,board[x][y])
                for d in range(len(dx)):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if nx <0 or nx >=n or ny <0 or ny >=m or map[nx][ny] != 'L' or visited[nx][ny]:
                        continue
                    q.append((nx,ny))
                    board[nx][ny] = board[x][y]+1
                    

print(result)