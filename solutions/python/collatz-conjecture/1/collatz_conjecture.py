def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    numberOfsteps = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        numberOfsteps += 1
    return numberOfsteps