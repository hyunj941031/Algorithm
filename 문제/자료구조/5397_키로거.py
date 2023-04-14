for _ in range(int(input())):
    entered = input()
    left_stack = []
    right_stack = []
    for e in entered:
        if e == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif e == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif e == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(e)
        
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))