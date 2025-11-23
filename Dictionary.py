# EXERCISE
print("Exercise")

# 1. Create an empty dictionary called dog
dog = {}
print(dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['color'] = 'white'
dog['breed'] = 'german shepherd'
dog['legs'] = 4
dog['age'] = 5
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'Bob'
student['last_name'] = 'Smith'
student['gender'] = 'male'
student['age'] = 25
student['martial status'] = 'single'
student['skills'] = ['coding', 'sports', 'singing']
student['country'] = 'Philippines'
student['city'] = 'Makati City'
student['address'] = 'barangay 101'
print(student)

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print('skills' in student)

# 6. Modify the skills values by adding one or two skills
student['skills'].append('ballet')
student['skills'].append('music')
print(student['skills'])

# 7. Get the dictionary keys as a list
student_keys = student.keys()
print(student_keys)

# 8. Get the dictionary values as a list
student_values = student.values()
print(student_values)

# 9. Change the dictionary to a list of tuples using items() method
print(student.items())

# 10. Delete one of the items in the dictionary
student.pop('skills')
print(student)

# 11. Delete one of the dictionaries
del dog
