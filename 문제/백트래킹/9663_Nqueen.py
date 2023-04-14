n = int(input())

row = [0] * n
result = 0

def check(x):
    for i in range(x):
        # 세로 확인
        if row[x] == row[i]:
            return False
        # 대각선 확인
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)
                
dfs(0)
print(result)