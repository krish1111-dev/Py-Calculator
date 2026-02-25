def Additon(a, b):
    return a + b


def Subtraction(a, b):
    return a - b


def Multiply(a, b):
    return a * b


def Division(a, b):
    return a / b


print("- Enter the Operation -")
print("1. Addition ")
print("2. Subraction ")
print("3. Multiply ")
print("4. Division ")
print("5. Exit")


while True:
    choise = input("Enter the Operation You Want - ")

    if choise == "5":
            print("Exiting... ")
            break
    
    if choise not in ["1", "2", "3", "4", "5"]:
        print("Enter the Valid Operation")
        continue     


    try:
         Num1 = float(input("Enther the First Number: "))
         Num2 = float(input("Enther the Second Number: "))
    except ValueError:
        print("Enther the Valid number")
        continue
    

    if choise == "1":
        print("Result: ", Additon(Num1, Num2))

    elif choise == "2":
        print("Result: ", Subtraction(Num1, Num2))

    elif choise == "3":
        print("Result: ", Multiply(Num1, Num2))

    elif choise == "4":
        print("Result: ", Division(Num1, Num2))

    else:
        print("Enther the Valid Number")
