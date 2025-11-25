import math
import practical_work2_task2

while True:

    x = input("Enter number 'X': ")

    if x.isdigit():

        x = int(x)

        y = input("Enter number 'Y': ")

        if y.isdigit():

            y = int(y)

            break

        else:

            print("It is not a number, please use only numbers")

    else:

        print("It is not a number, please use only numbers")

z = math.cos(x)  ** 2 + math.sin(y) ** 2

print(z)

while True:

    n = input("Enter number 'N': ")

    if n.isdigit():

        n = int(n)

        result = practical_work2_task2.count_sum_of_squares(n)
        
        print(f"Sum of squares for {n} is: {result}")
        break
    
    else:

        print("It is not a number, please use only numbers")