# Tuple of Tuples Processing:         
# Find the student with the highest score without using a loop.  
students = (("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 88))
topstudent = max(students,key=lambda x:x[1])
print(topstudent)


