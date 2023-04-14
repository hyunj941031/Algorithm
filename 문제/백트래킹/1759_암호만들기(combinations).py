from itertools import combinations

l, c = map(int, input().split())
alphabet = input().split()

alphabet.sort()

vowels = ('a', 'e', 'i', 'o', 'u')

for password in combinations(alphabet, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
            
    if count >= 1 and count <= l - 2:
        print(''.join(password))