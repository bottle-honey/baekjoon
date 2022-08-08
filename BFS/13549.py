# 숨바꼭질 3
from queue import PriorityQueue
n,k = map(int,input().split())
MAX = 100001
visited = [False] * MAX

queue = PriorityQueue()
queue.put((0,n))

while queue:
    count, cur_pos = queue.get()
    
    if cur_pos == k:
        result = count
        break
    visited[cur_pos] = True
    
    cases = [(count,cur_pos*2),(count+1,cur_pos-1),(count+1,cur_pos+1)]
    
    for add,case in cases:
        if case<=k+1 and not visited[case]:
            queue.put((add,case))

print(result)