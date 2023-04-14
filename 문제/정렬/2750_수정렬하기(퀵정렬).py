array = []
for _ in range(int(input())):
    array.append(int(input()))

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
            
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)

result = quick_sort(array)

for i in result:
    print(i)