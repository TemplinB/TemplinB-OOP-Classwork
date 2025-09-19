myStudents = {}

while True:
    print("1. Add a Student")
    print("2. Delete a Student")
    print("3. Modify a Student")
    print("4. Display all Students")
    print("5. Exit the Program")

    option = input("Choose and Option: ")

    if option == "1":
        nname = input("Give Student Name: ")
        l1p = int(input("Give Lab 1 Points: "))
        l2p = int(input("Give Lab 2 Points: "))
        l3p = int(input("Give Lab 3 Points: "))
        l4p = int(input("Give Lab 4 Points: "))
        l5p = int(input("Give Lab 5 Points: "))

        lab_total = l1p + l2p + l3p + l4p + l5p
        lab_perc = (lab_total / 50) * 100
        lab_avg = (lab_total) / 5

        myStudents.update({nname: {
            "lab1": l1p,
            "lab2": l2p,
            "lab3": l3p,
            "lab4": l4p,
            "lab5": l5p,
            "total": lab_total,
            "perc": lab_perc,
            "avg": lab_avg}})

    elif option == "2":
        name_del = input("Which Student to Delete: ")
        del myStudents[name_del]

    elif option == "3":
        nname = input("Give Student Name: ")
        l1p = int(input("Give Lab 1 Points: "))
        l2p = int(input("Give Lab 2 Points: "))
        l3p = int(input("Give Lab 3 Points: "))
        l4p = int(input("Give Lab 4 Points: "))
        l5p = int(input("Give Lab 5 Points: "))

        lab_total = l1p + l2p + l3p + l4p + l5p
        lab_perc = (lab_total / 50) * 100
        lab_avg = (lab_total) / 5

        myStudents.update({nname: {
            "lab1": l1p,
            "lab2": l2p,
            "lab3": l3p,
            "lab4": l4p,
            "lab5": l5p,
            "total": lab_total,
            "perc": lab_perc,
            "avg": lab_avg}})

    elif option == "4":
        for student_record in myStudents.items():
            print(student_record)
            print("---------------------------------------------------------------------------------------")

    elif option == "5":
        break