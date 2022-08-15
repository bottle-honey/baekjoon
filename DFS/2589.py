#보물섬
import sys
from collections import deque
import copy
input = sys.stdin.readline
n,m = map(int,input().split())

map = []
for _ in range(n):
    map.append(list(input().rstrip('\n')))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = [0]


        
for i in range(n):
    for j in range(m):
        if map[i][j] == 'L':
            #BFS
            map_copy = copy.deepcopy(map)
            q = deque([(i,j,0)])
            while q:
                x,y,distance = q.pop()
                map_copy[x][y] = distance
                able = 0
                for d in range(len(dx)):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if nx <0 or nx >=n or ny <0 or ny >=m or map_copy[nx][ny] != 'L':
                        continue
                    able+=1
                    q.appendleft((nx,ny,distance+1))
                if able == 0:
                    result.append(distance)
                    

print(max(result))