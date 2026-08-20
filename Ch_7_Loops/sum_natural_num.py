num= int(input("Enter how many natural numbers to sum: "))
sum=0

for i in range(1,num+1):
    sum+=i

print(f"The sum of the first {num} natural numbers is: {sum}")