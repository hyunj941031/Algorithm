import sys
# 재귀횟수 늘리기
sys.setrecursionlimit(10000)

def dfs(x, y):
    visited[x][y] = True
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)
    
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    array = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    count = 0
    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y] = 1
        
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)