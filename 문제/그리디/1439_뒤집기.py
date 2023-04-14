nums = input()

first = nums[0]
count = 1
for num in nums:
    if num != first:
        count += 1
        first = num
        
print(count // 2)