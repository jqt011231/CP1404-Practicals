
numberInput = [int(input("Enter a number: ")) for i in range(2)]

for number in range(numberInput[0], numberInput[1]):
    if number % 2 == 0:
        print("even number: ", number)
for number in range(numberInput[0], numberInput[1]):
    if number % 2 == 1:
        print("odd number: ", number)
