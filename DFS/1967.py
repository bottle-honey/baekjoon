import sys

sys.setrecursionlimit(10**9)

n = int(input())
tree = [[]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))


def dfs(start_node,sum_v):
    for node,v in tree[start_node]:
        if distances[node] == -1:
            distances[node] = max(distances[node],sum_v+v)
            dfs(node,sum_v+v)
distances = [-1] * (n+1)
distances[1]=0
dfs(1,0)

max_value_node = distances.index(max(distances))

distances = [-1] * (n+1)
distances[max_value_node] = 0
dfs(max_value_node,0)
print(max(distances))