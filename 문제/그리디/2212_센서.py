import sys

n = int(input())
k = int(input())

if k >= n:
    print(0)
    sys.exit()

sensors = list(map(int, input().split()))
sensors.sort()

diff = []
for i in range(len(sensors)-1):
    diff.append(sensors[i+1] - sensors[i])
    
diff.sort()

for _ in range(k-1):
    diff.pop()
    
print(sum(diff))