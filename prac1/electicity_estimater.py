
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
def main():
    tarrif = float(input("Which tarrif (11 or 31)= "))
    while tarrif != 11 and tarrif!= 31:
        print("Please input 11 or 31")
        tarrif = float(input("Which tarrif (11 or 31)= "))
    dailyUsage = float(input("Enter daily usage per kWh= "))
    days= float(input("Enter days of billing period= "))
    if tarrif == 11:
        billingTotal= TARIFF_11*dailyUsage*days
    else:
        billingTotal = TARIFF_31 * dailyUsage * days
    print ("Estimated bill= $ {0:.2f}".format(billingTotal))
main()
