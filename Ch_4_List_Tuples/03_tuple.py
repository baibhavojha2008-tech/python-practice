a=(1,14,False,"Rohan")
print(a)
#The tuple is immutable, meaning its elements cannot be changed after creation.

c=a.count(14)  # Counts the number of occurrences of 14 in the tuple
print(c)  # Output: 1

i=a.index("Rohan")  # Returns the index of the first occurrence of "Rohan" in the tuple
print(i)  # Output: 3

k=a[0:3]  # Slices the tuple to get elements from index 0 to 2
print(k)  # Output: (1, 14, False)  

print(len(a))  # Output: 4, returns the number of elements in the tuple
