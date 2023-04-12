def dfs(v):
    global result
    result += 1
    visited[v] = True
    for e in array[v]:
        if not visited[e]:
            dfs(e)
    
n = int(input())
case = int(input())
array = [[] for _ in range(n+1)]

for _ in range(case):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x)

visited = [False] * (n + 1)
result = -1

dfs(1)

print(result)