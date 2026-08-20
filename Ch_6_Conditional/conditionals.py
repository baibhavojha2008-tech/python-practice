age=int(input("Enter your age: "))

if (age <= 18):
    print("You are a minor.")

elif (age < 0):
    print("Invalid age.")
elif (age == 0):
    print("You are a newborn.")

else:
    print("You are not a minor.")

print("Thank you for using the age checker.")

