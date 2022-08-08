#트리의 지름

# def dfs(node,sum,result):
#     node_inf = tree[node]
#     visited[node] = True
#     if result < sum:
#         return sum
#     #i : 인접 노드 / n : 간선 거리
#     for i,n in enumerate(node_inf):
#         if n != 0:
#             if not visited[i]:
#                 dfs(i,sum+n,sum+n)
                


n = int(input())
def dfs(start_node,tree):
    stk = [(start_node,0)]
    result = 0
    visited = [False] * len(tree)
    while stk:
        node,cur_v = stk.pop()
        visited[node] = True
        node_inf = tree[node]
        #i : 인접 노드 / n : 간선 거리
        for i,n in enumerate(node_inf):
            if n != 0:
                if not visited[i]:
                    stk.append((i,cur_v+n))
            else:
                result = max(result,cur_v)
    return result
tree = [[0]*n for _ in range(n)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    tree[a-1][b-1] = c
    tree[b-1][a-1] = c

result = 0
for i in range(n):
    result = max(result,dfs(i,tree))
print(result)
