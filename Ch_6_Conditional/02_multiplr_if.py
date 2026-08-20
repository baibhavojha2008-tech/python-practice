age= int(input("Enter your age: "))

#If statement 1

if (age%2 == 0):
    print("Your age is even")

#If statement 2

if (age <= 18):
    print("You are a minor.")

elif (age < 0):
    print("Invalid age.")
elif (age == 0):
    print("You are a newborn.")

else:
    print("You are not a minor.")

print("End of program.")