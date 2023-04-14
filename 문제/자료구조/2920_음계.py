melody = list(map(int, input().split()))

if melody[0] < melody[1]:
    now = "ascending"
else:
    now = "descending"

for i in range(1, 7):
    if melody[i] < melody[i+1]:
        if now == "ascending":
            continue
        else:
            now = "mixed"
            break
    else:
        if now == "descending":
            continue
        else:
            now = "mixed"
            break
        
print(now)