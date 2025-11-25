a = 5
b = 80

sum_squares = 0

count = 0

for number in range(a, b + 1):
    
    square = number ** 2

    sum_squares += square 

    count += 1 

average = sum_squares / count 

print("Average form squares all integers form 'a' to 'b': ", average)