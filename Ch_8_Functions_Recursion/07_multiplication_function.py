def mul(n,m):
    for i in range(1,m+1):
        print(f"{n}*{i}={n*i}")

n=int(input("Enter the number you want multiply table:"))
m=int(input("Enter the number till which you want the table:"))
mul(n,m)

