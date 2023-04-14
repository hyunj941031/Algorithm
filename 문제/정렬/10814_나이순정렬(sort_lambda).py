n = int(input())
members = []
for _ in range(n):
    a, b = input().split()
    a = int(a)
    members.append((a, b))
    
members = sorted(members, key=lambda x: x[0])

for i in members:
    print(i[0], i[1])