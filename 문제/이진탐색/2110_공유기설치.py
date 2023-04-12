n, c = list(map(int, input().split()))
house = []
for i in range(n):
    house.append(int(input()))
house = sorted(house)

start = 1
end = house[-1] - house[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    value = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] >= value + mid:
            value = house[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)