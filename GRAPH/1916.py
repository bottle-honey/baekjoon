# 최소비용 구하기
# 다익스트라
import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = int(10e9)
n=int(input())
m=int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
A,B= map(int,input().split())
d = [0] + [INF]*n
for i in range(1,n+1):
    d[i] = graph[A][i]
visited = [False]*(n+1)
# (비용,노드)
def dijkstra(start_node:int):
    q = [(0,start_node)]
    heapq.heapify(q)
    while q:
        value, node = heapq.heappop(q)
        visited[node] = True
        for i in range(1,n+1):
            

# 갈수 있는 경로 갱신
# 방문하지 않은 노드 중 비용이 최소인 노드 