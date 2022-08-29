import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
time = 0
cnt = 0
for i in range(n):
    cnt += board[i].count(1)
def bfs(x,y):
    q = deque([(x,y)])
    visited = [[False]*m for _ in range(n)]
    count = 0
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx<0 or nx >=n or ny < 0 or ny >=m:
                    continue
                if board[nx][ny] == 0 and not visited[nx][ny]:
                    q.append((nx,ny))
                elif board[nx][ny] == 1:
                    board[nx][ny] = 0
                    visited[nx][ny] = True
                    count+=1
    return count

while True:
    time+=1
    remove = bfs(1,1)
    if cnt - remove == 0:
        result = remove
        break
    cnt -= remove
print(time,result)
