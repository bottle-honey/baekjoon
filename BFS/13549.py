# 숨바꼭질 3
from queue import PriorityQueue
n,k = map(int,input().split())

queue = PriorityQueue()
queue.put((0,n))

while queue:
    count,cur_pos = queue.get()
    if cur_pos == k:
        result = count
        break
    if cur_pos-1 >=0:
        queue.put((count+1,cur_pos+1))
        queue.put((count+1,cur_pos-1))
    if cur_pos*2 > 0 and cur_pos*2 < 2*k:
        queue.put((count,cur_pos*2))
print(count)