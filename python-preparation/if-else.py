a = input()

if a % 2 != 0:
    print("Weird")
elif a % 2 == 0 and 2<=a<=5:
    print("Not Weird")
elif a % 2 == 0 and 6<=a<=20:
    print("Weird")
elif a % 2 == 0 and a>20:
    print("Not Weird")
