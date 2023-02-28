def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for item in range(n+1)]
    ways[0] = 1 # Base

    for denom in denoms:
        for amount in range(1,n+1): # amount is made by ways[i] ways
            if denom<=amount: # We can make an amount if demon(coin) is smaller or equal than the amount
                ways[amount]+= ways[amount-denom]
    return ways[n]
