def main():
    numItem = int(input("Number of item: "))
    while numItem <=0:
        print("The number is invalid")
        numItem = int(input("Number of item: "))
    price=[]
    for i in range(numItem):
        itemPrice = float(input("Price of the item: $"))
        price.append(itemPrice)
    if sum(price)>=100:
        totalPrice = sum(price)-sum(price)*0.1
        print("total price for",numItem,"is $",totalPrice)
    else:
        print("total price for",numItem,"is $",sum(price))

main()