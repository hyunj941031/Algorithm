n = int(input())
hope = []
for _ in range(n):
    hope.append(int(input()))
    
hope.sort()
result = 0
rank = 1
for i in range(len(hope)):
    result += abs(hope[i] - rank)
    rank += 1

print(result)