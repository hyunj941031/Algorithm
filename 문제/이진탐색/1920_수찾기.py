n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A.sort()

for b in B:
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if b == A[mid]:
            print(1)
            break
        elif b < A[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    if start > end:
        print(0)
            