# EXERCISE 1
print("Exercise 1")

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# For Loop
for i in range(11):
    print(i)
print()
# While Loop
number = 0
while number < 11:
    print(number)
    number = number + 1
    if number == 11:
        break
print()

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# For Loop
f = 11
for j in range(11):
    f -= 1
    print(f)
print()

# While Loop
g = 11
while g <= 11:
    g -= 1
    print(g)
    if g == 0:
        break
print()

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for a in range(7):
    for b in range(a):
        print('#', end='')
    print('')
    a += 1
print()

# 4. Use nested loops to create the following:
for c in range(8):
    for d in range(8):
        print('#', end=' ')
    print('')
    c += 1
print()

# 5. Print the following pattern:
for e in range(11):
    print(f"{e} x {e} = {e*e}")
print()

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
language = ['Python', 'Numpy','Pandas','Django', 'Flask']
for h in language:
    print(f"{h}, ", end="")
print()

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for k in range(0, 101, 2):
    print(f"{k}, ", end="")
print()

# 8. se for loop to iterate from 0 to 100 and print only odd numbers
for l in range(101):
    if l % 2 == 1:
        print(f"{l}, ", end="")
print()

# EXERCISE 2
print("\nExercise 2")

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
the_sum = 0
for m in range(101):
    the_sum += m
print(f"{the_sum}")

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = 0
sum_odd = 0
for n in range(101):
    if n % 2 == 0:
        sum_even += n
print(f"The sum of all evens is {sum_even}. ", end='')
for o in range(101):
    if o % 2 == 1:
        sum_odd += o
print(f"And the sum of all odds is {sum_odd}")

# EXERCISE 3
print("\nExercise 3")

from country_data import countries, country

# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
for country in country():
    if country[-4:] == 'land':
        print(country)
print()

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for q in range(len(fruits)):
    q -= 1
    print(fruits[q])
print()

# 3. Go to the data folder and use the countries_data.py file.
# 3.1 What are the total number of languages in the data
unique_languages = set()
for data in countries():
    for language in data['languages']:
        unique_languages.add(language)
total_unique_languages = len(unique_languages)
print(total_unique_languages)

# 3.2 Find the ten most spoken languages from the data

# 3.3 Find the 10 most populated countries in the world

