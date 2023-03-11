def validStartingCity(distances, fuel, mpg):
    cities = len(distances)
    milesRemaining = 0  # remaining fuel to cover distance
    startingIndex = 0  # Possible starting index
    milesRemainingAtStartingCity = 0  # Remaining miles (fuel to cover distance) at starting city

    for city in range(1, cities):
        distanceFromPrevCity = distances[city - 1]
        fuelFromPrevCity = fuel[city - 1]
        milesRemaining += fuelFromPrevCity * mpg - distanceFromPrevCity  # Miles remaining after traversing
        # to the current city from the previous city

        if milesRemaining < milesRemainingAtStartingCity:
            milesRemainingAtStartingCity = milesRemaining
            startingIndex = city

    return startingIndex
