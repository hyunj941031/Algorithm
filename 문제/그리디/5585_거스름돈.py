price = int(input())
coins = [500, 100, 50, 10, 5, 1]
pay = 1000

count = 0
change = pay-price
for coin in coins:
    count += change // coin
    change %= coin

print(count)