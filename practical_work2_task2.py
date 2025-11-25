def count_sum_of_squares(number):

    sum_of_squares = 0

    for i in range(1, number + 1):
        sum_of_squares += i ** 2
    
    return sum_of_squares
    