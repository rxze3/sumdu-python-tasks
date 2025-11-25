while True:
    a = input("Enter 'A' number: ")

    if a.isdigit():
        a = int(a)

        b = input("Enter 'B' number: ")
        
        if b.isdigit():
            
            b = int(b)
            break

        else:
            print("It is not a number, please use only numbers")

    else:
        print("It is not a number, please use only numbers")

if a == b:
    x = a

    print("Your function is equals to: ", x)

else:
    if a > b:

        x = b / a + 61 

        print("Your function is equals to: ", x)

    else: 
        x = (b - a) / b

        print("Your function is equals to: ", x)