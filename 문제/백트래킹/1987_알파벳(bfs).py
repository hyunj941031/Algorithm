r, c = map(int, input().split())

array = []
for _ in range(r):
    array.append(input())

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def check_history(x, history):
    if x in history:
        return False
    else:
        return True
    
def check_available(x, y):
    if (x < 0) or (x >= c) or (y < 0) or (y >= r):
        return False
    return True
            
def bfs(x, y):
    global result
    # 동일한 경우는 한번만 계산하기 위해 set 사용
    q = set()
    q.add((x, y, array[y][x]))
    
    while q:
        x, y, step = q.pop()
        result = max(result, len(step))
        
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            
            if check_available(nx, ny) and check_history(array[ny][nx], step):
                q.add((nx, ny, step + array[ny][nx]))
        
result = 0
bfs(0,0)
print(result)