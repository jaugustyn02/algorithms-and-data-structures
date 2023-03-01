def prom_problem(A, L):
    def custom_key(i):
        nonlocal A
        return A[i]

    indices = [i for i in range(len(A))]
    indices.sort()
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