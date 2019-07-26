
def main():
    sales = float(input("Enter sales: $"))
    if sales < 0:
        print ("Please input positive numbers or you are fired")
    else:
        if sales < 1000:
            bonus = sales*0.1
            print("Your bonus: $", bonus )
            sales = float(input("Enter sales: $"))
        else:
            bonus = sales*0.15
            print("Your bonus: $", bonus)
main()