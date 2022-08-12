# 숨바꼭질 3
from collections import deque
n,k = map(int,input().split())
MAX = 100001
visited = [False] * MAX

queue = deque([(0,n)])

while queue:
    count, cur_pos = queue.popleft()
    if cur_pos == k:
        result = count
        break
    visited[cur_pos] = True
    
    cases = [(count,cur_pos*2),(count+1,cur_pos-1),(count+1,cur_pos+1)]
    
    for i in range(len(cases)):
        if cases[i][1] >=0 and cases[i][1]<=MAX-1 and not visited[cases[i][1]]:
            if i == 0:
                queue.appendleft((cases[i][0],cases[i][1]))
            else:
                queue.append((cases[i][0],cases[i][1]))

print(result)