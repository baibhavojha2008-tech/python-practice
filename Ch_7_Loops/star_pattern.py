'''
for n=3
    *
   ***
  *****
'''

n=int(input("Enter how many lines do you want:"))

for i in range (1, n+1):
    print(" "* (n-i), end="") #For spaces 
    print("*"*(2*i-1),end="") #For odd number of stars
    print("") #This simply moves the cursor to the next line.

#end="" gives new line automatically

