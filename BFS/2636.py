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
def bfs(x,y):
    q = deque([(x,y)])
    visited = [[False]*m for _ in range(n)]
    space = [(x,y)]
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx==0 or nx ==n-1 or ny ==0 or ny ==m-1:
                    return []
                if board[nx][ny] == 0 and not visited[nx][ny]:
                    q.append((nx,ny))
    return space
while True:
    count = 0
    remove = []
    space_list = []
    for i in range(1,n-1):
        for j in range(1,m-1):
            space_list= space_list + bfs(i,j)
            
    for x in range(1,n-1):
        for y in range(1,m-1):
            if board[x][y] == 1:
                count +=1
                air = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if board[nx][ny] == 0:
                        if (nx,ny) in space_list:
                            continue                            
                        else:
                            air+=1
                            break
                if air>0:
                    remove.append((x,y))
    for x,y in remove:
        board[x][y] = 0
    # print(space_list)
    # for i in range(n):
    #     print(board[i])
    
    if count == 0:
        break
    else:
        result = count
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 0
        time+=1
print(time)
print(result)