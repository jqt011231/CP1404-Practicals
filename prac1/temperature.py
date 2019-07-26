def main():
    choice = selection()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print("Result: {:.2f} F".format(fahrenheit))
            choice = selection()
        elif choice == "F":
            fahrenheit = float(input ("Fahrenheit: "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print("Result: {:.2f} C".format(celsius))
            choice = selection()
        else:
            print("Invalid option")
            choice = selection()
    print("Thank you.")

def selection():
    MENU = """C - Convert Celsius to Fahrenheit
        F - Convert Fahrenheit to Celsius
        Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    return (choice)
main()