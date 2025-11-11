# Sets. Set is used to store unique items, and it is possible to find
# the union, intersection, difference, symmetric difference, subset,
# super set and disjoint set among sets.

# Sets Operations: len(), checking(element in set_name), adding(set_name.add(element)), updating(set_name.update(set_name or [element/s])), removing(sets_name.remove(element) / set_name.discard(element) / sets_name.pop()), clearing(set_name.clear()), deleting(del set_name), converting_to_list(),
# union(set_name.union(set_name)), intersecting(set_name.intersection(set_name)), checking_subset(set_name_1.issubset(set_name_2) or set_name_2.issuperset(set_name_1)), difference(stet_name.difference(set_name)), (A\B)∪(B\A) = symmetric_differences(set_name_1.symmetric_difference(set_name_2))
# joining(set_name_1.isdisjoint(set_name_2))

# Given sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# EXERCISE 1
print("Exercise 1")

# 1 Find the length of the set it_companies
print(len(it_companies))

# 2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Reddit', 'Nvidia', 'Tesla']) # Inserted on random indices
print(it_companies)

# 4 Remove one of the companies from the set it_companies
it_companies.discard('Facebook')
print(it_companies)

# 5 What is the difference between remove and discard
print("""The difference between remove an discard is that remove() only remove
the element/s you want to remove and will return errors if object is not found,
while the discard() will not return any errors""")

# ============================================================================== #

# EXECISE 2
print("\nExercise 2")

# 1 Join A and B
union = A.union(B)
print(union)

# 2 Find A intersection B
intersect = A.intersection(B)
print(intersect)

# 3 Is A subset of B
subset = A.issubset(B)
print(subset)

# 4 Are A and B disjoint sets
joining = A.isdisjoint(B)
print(joining)

# 5 Join A with B and B with A
unionA_B = A.union(B)
unionB_A = B.union(A)
print(f"{unionA_B}\n{unionB_A}") # Similar Output

# 6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# 7 Delete the sets completely
del A, B # No Output

# =================================================== #

# EXERCISE 3
print("\nExercise 3")

# 1 Convert the ages to a set and compare the length of the list and the set. Which one is bigger?
set_age = set(age)
age_length = len(age)
set_age_length = len(set_age)
if age_length > set_age_length:
    print("List is greater than the set.")
else:
    print("Set is greater than list.")
