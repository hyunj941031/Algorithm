import heapq

n = int(input())
problems = []
result = []

for _ in range(n):
    d, c = map(int, input().split())
    problems.append((d, c))
problems.sort()

for i in problems:
    d = i[0]
    heapq.heappush(result, i[1])
    
    if d < len(result):
        heapq.heappop(result)

print(sum(result))
