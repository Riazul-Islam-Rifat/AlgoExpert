def minNumberOfCoinsForChange(n, denoms):
    numsOfCoins = [float('inf') for item in range(n + 1)]
    numsOfCoins[0] = 0

    for denom in denoms:
        for amount in range(1, len(numsOfCoins)):
            if denom <= amount:
                numsOfCoins[amount] = min(numsOfCoins[amount], 1 + numsOfCoins[amount - denom])

    return numsOfCoins[n] if numsOfCoins[n] != float('inf') else -1


