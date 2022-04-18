menuList = []
priceList = []
total = 0

def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
for number in range(len(menuList)):
    total = total + int(priceList[number])
print("ยอดรวม =",total,"THB")

