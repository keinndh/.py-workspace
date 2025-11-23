# EXERCISE 1
print("Exercise 1")

# 1 Create an empty tuple
empty_tuple = ()
print(empty_tuple)

# 2 Create a tuple containing names of your sisters and your brothers
brothers = ('Bob', 'Ben')
sisters = ('Anna', 'Jane')
print(f"{brothers},\n{sisters}")

# 3 Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# 4 How many siblings do you have?
print(f"I have {len(siblings)} siblings.")

# 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Shane', 'Alex')
family_members = siblings + parents
print(family_members)

# EXERCISE 2
print("\nExercise 2")

# 1 Unpack siblings and parents from family_members
the_family_members = list(family_members)
unpacked_siblings = the_family_members[:len(the_family_members) - 2]
unpacked_parents = the_family_members[len(the_family_members) - 2:]
print(f"{unpacked_siblings},\n{unpacked_parents}")

# 2 Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('spinach', 'bittergourd', 'lettuce')
animals_products = ('meat', 'fur', 'milk')
food_stuff_tp = fruits + vegetables + animals_products
print(food_stuff_tp)

# 3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4 Slice out the middle item or items from the food_stuff_tp tuple or
# food_stuff_lt list.
print(food_stuff_lt[len(food_stuff_tp) // 2 - 1:len(food_stuff_tp) // 2 + 1])

# 5 Slice out the first three items and the last three items from food_staff_lt list
print(f"{food_stuff_lt[:3]},\n{food_stuff_lt[-3:]}")

# 6 Delete the food_staff_tp tuple completely
del food_stuff_tp # No Output

# 7 Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"{'Estonia' in nordic_countries}\n{'Iceland' in nordic_countries}")
