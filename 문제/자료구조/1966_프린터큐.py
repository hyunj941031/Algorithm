t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(docs)]
    count = 0
    while True:
        max_val = max(queue, key=lambda x: x[0])[0]
        if max_val == queue[0][0]:
            count += 1
            if queue[0][1] == m:
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
                
    print(count)