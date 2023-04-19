def bestSeat(seats):
    seat = -1
    space = 0
    left = 0
    # Iterate each item once.
    # 0th and last index value will always be 1.
    # Find number of consecutive 0s.
    while left < len(seats):
        right = left+1
        while right < len(seats) and seats[right]==0:
            right+=1

        currentSpace = right - left -1  # Takes only number of zeroes.
        if currentSpace > space:
            space = currentSpace # Update with max space
            seat = (right+left)//2

        left = right

    return seat