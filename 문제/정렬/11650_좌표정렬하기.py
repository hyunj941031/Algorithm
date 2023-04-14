n = int(input())
array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))
    
array = sorted(array)

for i in array:
    print(i[0], i[1])