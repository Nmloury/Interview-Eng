def check_sum(cache, coins, total):
    best_coins_count = float('inf')
    for coin in coins:
        temp_diff = total - coin
        if temp_diff < 0:
            pass
        else:
            total_count = 1 + cache[temp_diff]
            if total_count < best_coins_count:
                best_coins_count = total_count
    cache[total] = best_coins_count


def min_coins(coins, coin_sum):
    cache = {0: 0}
    for i in range(1, coin_sum + 1):
        check_sum(cache, coins, i)
    return cache[coin_sum]

#######
# Tests
#######


min_coins([1, 3, 5], 3)
min_coins([1, 3, 5], 5)
min_coins([1, 3, 5], 11)
min_coins([1, 3, 5], 12)
min_coins([2, 3, 5], 1)
