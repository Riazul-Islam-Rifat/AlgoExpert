def nonConstructibleChange(coins):
    coins.sort()

    CuurentChange = 0

    for item in coins:
        if item>CuurentChange+1:
            return CuurentChange+1

        else:
            CuurentChange+=item

    return CuurentChange+1