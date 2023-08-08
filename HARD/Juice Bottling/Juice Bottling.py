def juiceBottling(prices):
    # Stores the profit
    maxProfit = [0] * len(prices)
    # Store the dividing point for each quantity
    # We store the first index of the dividing points
    # Ex- Answer is [1,2] then we store 1 as a dividing point for that quantity
    # We do so because we need the answer in ascending order
    dividingPoints = [0] * len(prices)

    for qty in range(len(prices)):
        for dividingPoint in range(qty + 1):
            # Find the profit
            profit = prices[dividingPoint] + maxProfit[qty - dividingPoint]

            if profit > maxProfit[qty]:  # When current profit for tha quantity is greater than the previous profit
                maxProfit[qty] = profit  # Update the maxProfit
                # Store the dividingPoint for which we get the maxProfit
                dividingPoints[qty] = dividingPoint

                # Now find the solution using the dividingPoints
    solution = []
    # We always find the profit for the highest quantity
    # So first dividing point is in that position
    currentDividingPoint = len(prices) - 1
    while currentDividingPoint > 0:  # As in 0th position we don't have any profit we don't add it in our answer
        solution.append(dividingPoints[currentDividingPoint])
        currentDividingPoint -= dividingPoints[currentDividingPoint]

    return solution
