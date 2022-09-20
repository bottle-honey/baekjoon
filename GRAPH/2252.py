# 줄 세우기
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited= [False]*(n+1)
degree = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b]+=1
q = deque([])
result = []
for i in range(1,n+1):
    if degree[i] == 0:
        if not visited[i]:
            q.append(i)
            visited[i] = True
while q:
    cur_node= q.popleft()
    result.append(cur_node)
    for node in graph[cur_node]:
        degree[node]-=1
        if degree[node] == 0:
            q.append(node)
for r in result:
    print(r,end=' ')