def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = len(array) // 2
    front_arr, pivot_arr, back_arr = [], [], []
    for value in array:
        if value < array[pivot]:
            front_arr.append(value)
        elif value > array[pivot]:
            back_arr.append(value)
        else:
            pivot_arr.append(value)
            
    return quick_sort(front_arr) + pivot_arr + quick_sort(back_arr)

input_data = input()
array = []
for i in input_data:
    array.append(int(i))

result = quick_sort(array)

for i in reversed(result):
    print(i, end='')