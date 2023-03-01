# Zadanie 6. (wydawanie monet)

# 3 7 10    10
#
#  1 2 5 8 10      13
#   10 2 1
#   5 8
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13
#  0 1 1 2 2 3 3 4 4 5 5  6  6  7

def min_coins(coins, T):
    coins.sort()
    C = [0 for _ in range(T+1)]
    for coin in coins:
        for i in range(coin, T+1):
            coin_count = 0
            amount = i
            coin_count += amount // coin
            amount %= coin
            if amount > 0:
                if C[amount] > 0:
                    coin_count += C[amount]
                else:
                    continue
            if C[i] == 0 or C[i] > coin_count:
                C[i] = coin_count
        # print(C)
    return C[T]
# end


c = [1, 3, 5, 13, 20, 7, 10]
k = 34

print(min_coins(c, k))
