def dp_change(money, coins):
    min_coins = {0:0}
    for m in range(1, money+1):
        min_coins[m] = 1000000000
        for i, coin in enumerate(coins):
            if m >= coin:
                if min_coins[m-coin] + 1 < min_coins[m]:
                    min_coins[m] = min_coins[m-coin] + 1
    return min_coins[money]


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        money = int(f.readline())
        coins = map(int,f.readline().split(','))
    result = dp_change(money, coins)
    with open('out.txt', 'w') as f:
        f.write(str(result))