s1= {1,9,101}
s2= {2,3,101}

print(s1.union(s2))  # Output: {1, 2, 3, 9, 101} - Union of s1 and s2
print(s1.intersection(s2))  # Output: {101} - Intersection of s1 and s2
print(s1.difference(s2))  # Output: {1, 9} - Difference of s1 and s2
print(s2.difference(s1))  # Output: {2, 3} - Difference of s2 and s1
