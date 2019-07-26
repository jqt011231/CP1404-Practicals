
def main():
    score=float(input("Enter score:"))
    if score <0 or score>100:
        print("It is invalid score")
    else:
        if score <=100 and score>=90:
            print("Excellent!")
        elif score <=50:
            print ("Passable")
        else:
            print("Bad")
main()


