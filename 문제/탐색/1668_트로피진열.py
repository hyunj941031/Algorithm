n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
    
left = array[0]
left_count = 1
for i in range(1, len(array)):
    if left < array[i]:
        left = array[i]
        left_count += 1
        
right = array[-1]
right_count = 1
for i in range(len(array)-2, -1, -1):
    if right < array[i]:
        right = array[i]
        right_count += 1
        
print(left_count)
print(right_count)