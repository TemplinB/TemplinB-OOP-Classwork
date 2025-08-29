a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

if a > b and a > c:
    print("A is the greatest")
elif b > a and b > c:
    print("B is the greatest")
elif c > a and c > b:
    print("C is the greatest")
else:
    print("They are equal")

####################################

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
operator = input("Enter Operator + - * /:")

if operator == "+":
    print("The sum is:", num1 + num2)

elif operator == "-":
    print("The difference is:", num1 - num2)

elif operator == "*":
    print("The product is:", num1 * num2)

elif operator == "/":
    print("The product is:", num1 / num2)

else:
    print("Not usable operator")
