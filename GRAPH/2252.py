# 줄 세우기
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
degree = [0]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
visited= [False]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    degree[b]+=1
q = deque([])
result = []
while len(result)<n:
    for i in range(1,n+1):
        if degree[i] == 0:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    while q:
        cur_node= q.popleft()
        result.append(cur_node)
        for j in range(1,n+1):
            if graph[cur_node][j]:
                degree[j]-=1
                graph[cur_node][j] = 0
for r in result:
    print(r,end=' ')