def vatCalulate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

print(vatCalulate(int(input("total price : "))))
