n, m = map(int, input().split())
array = list(map(int, input().split()))

result = 0
length = len(array)

count = 0
for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_value = array[i] + array[j] + array[k]
            if sum_value <= m:
                result = max(sum_value, result)
                
print(result)