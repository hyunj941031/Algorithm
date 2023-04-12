from collections import deque

n, m = map(int, input().split())
array = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[b].append(a)

# 간선이 많으면 dfs보다 bfs가 더 효과적
def bfs(v):
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for e in array[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1
    return count

result = []
max_value = -1

for i in range(1, n + 1):        
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        
for r in result:
    print(r, end=' ')