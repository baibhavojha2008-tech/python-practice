'''

***
* *   for n=3
***   
'''

n=int(input("Enter the lines of pattern="))

for i in range (1,n+1):   
    if(i==1 or i==n):
        print("*"* n)

    else:    
        print("*", end="") #Left side star
        print(" "* (n-2), end="") #Space in middle
        print("*", end="") #Right side star
        print("") #New line
