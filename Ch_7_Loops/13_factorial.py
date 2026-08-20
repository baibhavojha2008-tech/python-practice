num= int(input("Enter which number to find factorial of: "))
factorial=1
i=1
while i<= num:
    factorial*=i
    i+=1

print(f"The factorial of {num} is: {factorial}")
