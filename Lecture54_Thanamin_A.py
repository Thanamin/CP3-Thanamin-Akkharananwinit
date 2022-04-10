def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

while login() == False:
    print("username or password not correct")
while showMenu() != 1 or 2:
    userSelected = menuSelect()
    if userSelected == 1:
        print((vatCalculator(int(input("Total Price =")))),"THB")
        break
    elif userSelected == 2:
        print(priceCalculator(),"THB")
        break
    else:
        print("please select 1 or 2")


