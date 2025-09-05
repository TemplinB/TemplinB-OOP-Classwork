while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    option = input("Enter Choice: ")

    if option == "1":
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        answer = n1 + n2
        print("The answer is", answer)

    elif option == "2":
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        answer = n1 - n2
        print("The answer is", answer)

    elif option == "3":
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        answer = n1 * n2
        print("The answer is", answer)

    elif option == "4":
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        if n2 == 0:
            print("Answer is Undefined")
        else:
            answer = n1 / n2
            print("The answer is", answer)

    elif option == "5":
        break

print("Thank you for using this application!")