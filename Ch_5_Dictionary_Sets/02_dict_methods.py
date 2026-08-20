marks= {

"Baibhav": 90, #Baibhav is a key and 90 is the value associated with that key
"Rohit": 80, #Rohit is a key and 80 is the value associated with that key
"Ankit": 70 #Ankit is a key and 70 is the value associated with that key
}

print(marks.items())  # Output: dict_items([('Baibhav', 90), ('Rohit', 80), ('Ankit', 70)]), returns a view object of the dictionary's items
print(marks.keys())  # Output: dict_keys(['Baibhav', 'Rohit', 'Ankit']), returns a view object of the dictionary's keys 
print(marks.values())  # Output: dict_values([90, 80, 70]), returns a view object of the dictionary's values        

marks.update({"Rohit": 85, "Baseema": 95})  # Updates the value associated with the key "Rohit" to 85 and adds a new key-value pair
print(marks)  # Output: {'Baibhav': 90, 'Rohit': 85, 'Ankit': 70, 'Baseema': 95}

print(marks.get("Ankit"))  # Output: 70, returns the value associated with the key "Ankit"
print(marks.get("Rahul", "Not Found"))  # Output: Not Found, returns "Not Found" since the key "Rahul" does not exist in the dictionary

print(marks.get("Baibhav2", "Not Found"))  # Output: Not Found, returns "Not Found" since the key "Baibhav2" does not exist in the dictionary
print(marks["Baibhav2"])  # Output: KeyError: 'Baibhav2', raises a KeyError since the key "Baibhav2" does not exist in the dictionary