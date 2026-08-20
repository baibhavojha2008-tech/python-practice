list=["Apple", "Banana", 5, 345.09, False, "Rohan"]

list.append("New Item")  # Adds "New Item" to the end of the list

print(list)  # Output: ['Apple', 'Banana', 5, 345.09, False, 'Rohan', 'New Item']

L1=[12, 34, 78, 90, 45]
L1.sort()  # Sorts the list in ascending order
print(L1)  # Output: [12, 34, 45, 78, 90]

L1.reverse()  # Reverses the order of the list
print(L1)  # Output: [90, 78, 45, 34, 12]

L1.insert(3, 100)  # Inserts 100 at index 3
print(L1)  # Output: [90, 78, 45, 100, 12]

L1.pop()  # Removes the last item from the list
print(L1)  # Output: [90, 78, 45, 100]

L1.pop(1)  # Removes the item at index 1
print(L1)  # Output: [90, 45, 100]

L1.remove(45)  # Removes the first occurrence of 45 from the list
print(L1)  # Output: [90, 100]   

#List is mutable, meaning its elements can be changed after creation.

