while True:
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Division")
    print("5. Remainder")
    print("6. Floor Division")
    print("7. Power")
    print("8. Factorial")

    c = int(input("Enter your choice : "))

    if c == 1:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Addition : ", a + b)

    elif c == 2:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Subtraction : ", a - b)

    elif c == 3:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Multiply : ", a * b)

    elif c == 4:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        if b == 0:
            print("Cannot divide by zero, ERROR!!")
        else:
            print("Division : ", a / b)

    elif c == 5:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Remainder : ", a % b)

    elif c == 6:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        if b == 0:
            print("Cannot divide by zero, ERROR!!")
        else:
            print("Floor Division : ", a // b)

    elif c == 7:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Power : ", a ** b)

    elif c == 8:
        a = int(input("Enter no. : "))
        f=1
        for i in range(1,a+1):
            f=f*i
        print(f)
    elif c==0:
        break
    else:
        print("Invalid Choice!")