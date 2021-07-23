
n = int(input("The value of N :"))

if (n % 2 != 0):
    print("weird")

elif (n % 2 == 0 and (n) in range(2,5)):
    print("Not weird")

elif (n % 2 == 0 and (n) in range(6,21)):
    print("weird")

elif (n % 2 == 0 and n>20):
    print("Not weird")


