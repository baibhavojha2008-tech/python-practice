s={1, "Baibhav", 3.14} # Creates a set with mixed data types

print(s, type(s))  # Output: {1, 'Baibhav', 3.14} <class 'set'>

s.add("Rohit")  # Adds a new element to the set
print(s)  # Output: {1, 'Baibhav', 3.14, 'Rohit'}

s.add(3.14)  # Trying to add a duplicate element
print(s)  # Output: {1, 'Baibhav', 3.14, 'Rohit'} - No change, as 3.14 is already present

s.remove("Baibhav")  # Removes an element from the set
print(s)  # Output: {1, 3.14, 'Rohit'}

