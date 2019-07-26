
def main():
    starsNumber = int(input("Number of stars= "))
    for i in range(0, starsNumber+1):
        for j in range(0, i):
            print("*", end=' ')
        print()
main()