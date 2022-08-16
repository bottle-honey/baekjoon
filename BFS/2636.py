import sys
input = sys.stdin.readline
from collections import deque
import copy 
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
    copy_board = copy.deepcopy(board)
    copy_board[x][y] = 2
    while q:
        x,y = q.popleft()
        for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx<0 or nx >=n or ny <0 or ny >=m:
                    return []
                if copy_board[nx][ny] == 0:
                    q.append((nx,ny))
                    copy_board[x][y] = 2
    return copy_board
while True:
    count = 0
    remove = []
    for x in range(1,n-1):
        for y in range(1,m-1):
            if board[x][y] == 1:
                count +=1
                air = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if board[nx][ny] == 0:
                        copy_board = bfs(nx,ny)
                        if copy_board:
                            board= copy_board[:]
                        else:
                            air+=1
                            break
                if air>0:
                    remove.append((x,y))
    for x,y in remove:
        board[x][y] = 0
    
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