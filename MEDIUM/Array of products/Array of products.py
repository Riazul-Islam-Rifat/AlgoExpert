def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    # Calculating the left products
    leftProducts = 1  # Left product for the first index is 1
    for item in range(len(array)):
        products[item] = leftProducts
        leftProducts *= array[item]  # Update leftProduct for next index

    # Find right product and multiply it with leftProduct to get the actual Array of Products\

    rightProducts = 1  # Right product for the right most index is 1.
    for item in range(len(array) - 1, -1, -1):
        products[item] = products[item] * rightProducts
        rightProducts *= array[item]

    return products


