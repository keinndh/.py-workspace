# EXERCISE 1
print("Exercise 1")

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

# Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    current_age = 18 - age
    print(f"You need {current_age} more year/s to learn to drive.")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

# Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = int(input("\nEnter my age: "))
your_age = int(input("Enter your age: "))
if your_age > my_age:
    current_age = your_age - my_age
    print(f"You are {current_age} year/s older than me.")
elif your_age < my_age:
    current_age = my_age - your_age
    print(f"I am {current_age} year/s older than you")
else:
    print(f"We are both {your_age} years old.")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

# Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
first_number = int(input("\nEnter first number: "))
second_number = int(input("Enter second number: "))
if first_number > second_number:
    print(f"a: {first_number} is greater than b: {second_number}.")
elif first_number < second_number:
    print(f"a: {first_number} is less than b: {second_number}.")
else:
    print(f"a: {first_number} is equal to b: {second_number}.")

# EXERCISE 2
print("\nExercise 2")

# 1. Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
score = int(input("\nEnter your score: "))
if 90 <= score <= 100:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
elif score >= 50:
    print('D')
else:
    print('F')

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("\nEnter the month: ").lower()
if month == 'september' or month == 'october' or month == 'november':
    print("The season is Autumn.")
elif month == 'december' or month == 'january' or month == 'february':
    print("The season is Winter.")
elif month == 'march' or month == 'april' or month == 'may':
    print("The season is Saturday.")
elif month == 'june' or month == 'july' or month == 'august':
    print("The season is Summer.")
else:
    print("Invalid month.")

# EXERCISE 3
print("\nExercise 3")

# 1. Here we have a person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
skills = person['skills']
if 'skills' in person:
    middle_skill = len(skills) // 2
    print(f"Middle skill: {skills[middle_skill]}")

# 2. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    if 'Python' in skills:
        print("Python is in skills key?: True")
    else:
        print("Python is in skills key?: False")

# 3. If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
    if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'JavaScript' in skills and 'React' in skills:
        print('He is a front end developer')
    else:
        print('Unknown title')

# 4. If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")


