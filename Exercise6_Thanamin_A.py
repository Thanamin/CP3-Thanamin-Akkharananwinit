print("Welcome Please Login")
user = input("User Name :")
password = input("Password :")
water = 10
banana = 15
mango = 23
if user == "admin" and password == "1234":
    print("Hello Admin TMA SHOP")
    print("--------------------")
    print("Item")
    print("1.) Water ------ 10 THB")
    print("2.) Banana ----- 15 THB")
    print("3.) Mango ------ 23 THB")
    waterAmount = int(input("Water amount ? :"))
    bananaAmount = int(input("Banana amount ? :"))
    mangoAmount = int(input("Mango amount ? :"))
    print("Total :",(waterAmount*water)+(bananaAmount*banana)+(mangoAmount*mango),"THB")
    print("Thank you")
else:
    print("User or Password not correct")