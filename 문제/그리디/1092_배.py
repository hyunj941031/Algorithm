import sys

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

cranes.sort(reverse=True)
boxes.sort(reverse=True)
# 각 크레인이 현재 옮겨야하는 박스번호
positions = [0] * n
# 각 박스를 옮겼는지 여부
checked = [False] * m

result = 0
count = 0
while True:
    if count == len(boxes):
        break
    for i in range(n):
        while positions[i] < len(boxes):
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1
    
print(result)