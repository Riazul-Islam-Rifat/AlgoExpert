def getNthFib(n):
    # Write your code here.
    # The iterative solution is the best solution for nth fibonacchi number.
    last_two = [0, 1]
    counter = 3

    while counter <= n:
        nextFib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = nextFib
        counter += 1

    if n > 1:
        return last_two[1]
    else:
        return last_two[0]
