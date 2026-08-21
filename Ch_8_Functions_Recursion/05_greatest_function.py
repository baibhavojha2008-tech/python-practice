def greatest ():
    a=int(input("enter first number:"))
    b=int(input("enter secon number:"))
    c=int(input("enter third number:"))

    if (a>b and a>c):
     print(f"The greatest number is {a}")
    elif(b>a and b>c):
     print(f"The greatest number is {b}")
    else:
     print(f"The greatest number is {c}")  

greatest()


