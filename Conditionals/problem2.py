age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").lower()

print("Your movie ticket price is: ")
if day == "wednesday":
    if age >= 18:
        print("$10")
    else:
        print("$6")
else:
    if age >= 18:
        print("$12")
    else:
        print("$8")
