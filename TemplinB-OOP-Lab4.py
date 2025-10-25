import pickle

class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = ""
    def add_values_to_Customer(self):
        self.cid = input("\nEnter Customer ID: ")
        self.cname = input("Enter Customer Name: ")
        self.acc_no = input("Enter Account Number: ")
        self.phone = input("Enter Phone Number: ")
        self.emailID = input("Enter Email: ")
        self.balance = int(input("Enter Balance: "))
    def debit_from(self, debit):
        self.balance = self.balance - debit
    def credit_to(self, credit):
        self.balance = self.balance + credit
    def display_Cust_info(self):
        print(str(self.cname) + "'s", "balance is at", "$" + str(self.balance))

        print("\n", str(self.cname) + "'s", "Credit Cards:")
        for x in self.credit_card:
            print(x.display_Card())

        print("\n", str(self.cname) + "'s", "Debit Cards:")
        print(self.debit_card.display_Card())

    def assign_Card(self, card):
        if card.type == "cc":
            self.credit_card.append(card)
        elif card.type == "dc":
            self.debit_card = card

class Card:
    def __init__(self):
        self.type = ""
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = 0.0
    def add_values_to_Card(self):
        self.type = input("\nEnter Card Type (cc or dc): ")
        self.card_no = input("Enter Card Number: ")
        self.cvv = input("Enter CVV: ")
        self.expiry_date = input("Enter Expiration Date: ")
    def display_Card(self):
        print("\nType:", self.type)
        print("Card No.:", self.card_no)
        print("Card CVV:", self.cvv)
        print("Card Expiration Date:", self.expiry_date)

while True:

    print("\n1. Create Customer Object")
    print("2. Create Card Object")
    print("3. Transfer Funds Between Customer Objects")
    print("4. Assign Card Objects to Customer Objects")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Commit")
    print("8. Exit")

    option = input("\nEnter Option: ")

    if option == "1":
        cu1 = Customer()
        cu2 = Customer()
        cu1.add_values_to_Customer()
        cu2.add_values_to_Customer()

    elif option == "2":
        ca1 = Card()
        ca2 = Card()
        ca3 = Card()
        ca4 = Card()
        ca5 = Card()
        ca6 = Card()
        ca1.add_values_to_Card()
        ca2.add_values_to_Card()
        ca3.add_values_to_Card()
        ca4.add_values_to_Card()
        ca5.add_values_to_Card()
        ca6.add_values_to_Card()

    elif option == "3":
        debit = int(input("Enter Transfer Amount: "))
        cu1.debit_from(debit)
        cu2.credit_to(debit)

    elif option == "4":
        cu1.assign_Card(ca1)
        cu1.assign_Card(ca2)
        cu1.assign_Card(ca3)
        cu1.assign_Card(ca4)
        cu2.assign_Card(ca5)
        cu2.assign_Card(ca6)

    elif option == "5":
        cu1.display_Cust_info()
        cu2.display_Cust_info()

    elif option == "6":
        ca1.display_Card()
        ca2.display_Card()
        ca3.display_Card()
        ca4.display_Card()
        ca5.display_Card()
        ca6.display_Card()

    elif option == "7":
        f1 = open("TemplinB-OOP-Lab4-Card.dat", "ab")
        pickle.dump(cu1, f1)
        pickle.dump(cu2, f1)
        pickle.dump(ca1, f1)
        pickle.dump(ca2, f1)
        pickle.dump(ca3, f1)
        pickle.dump(ca4, f1)
        pickle.dump(ca5, f1)
        pickle.dump(ca6, f1)
        f1.close()

    elif option == "8":
        break
