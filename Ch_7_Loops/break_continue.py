for i in range(100):
    if i == 50:
        break
    print(i)
print("The loop is broken at 50")

for i in range(100):
    if i == 50:
        continue  #Skips the current iteration and continues with the next iteration
    #Skips 50 and continues with the next iteration
    print(i)
print("The loop is skipped at 50")
