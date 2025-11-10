# EXERCISES 1
print("EXERCISES 1")

# 1 Declare an empty list
empty_list = []
print(f"\n{empty_list}")

# 2 Declare a list with more than 5 items
list = [1, 2, 3, 4, 5]
print(list)

# 3 Find the length of your list
print(len(list))

# 4 Get the first item, the middle item and the last item of the list
print(list[0], list[2], list[4]) # Small data set

# 5 Declare a list called mixed_data_types,
# put your(name, age, height, marital status, address)
mixed_data_types = ['Mon', 19, 174, 'Single', 'Philippines']
print(mixed_data_types)

# 6 Declare a list variable named it_companies and
# assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle
# and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7 Print the list using print()
print(it_companies)

# 8 Print the number of companies in the list
print(len(it_companies))

# 9 Print the first, middle and last company
print(f"{it_companies[0], it_companies[len(it_companies) // 2], it_companies[len(it_companies) - 1]}")

# 10 Print the list after modifying one of the companies
it_companies.insert(3, "Samsung")
print(it_companies)

# 11 Add an IT company to it_companies
it_companies.append("Nvidia")
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
it_companies.insert((len(it_companies) // 2), "Huawei")
print(it_companies)

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())

# 14 Join the it_companies with a string '#;  '
toJoin = '#; '
join = toJoin.join(it_companies)
print(join)

# 15 Check if a certain company exists in the it_companies list.
print('Samsung' in it_companies)

# 16 Sort the list using sort() method.
sort = sorted(it_companies) # New List
print(sort)

# 17 Reverse the list in descending order using reverse() method
print(sort.reverse())

# 18 Slice out the first 3 companies from the list
print(sort[:3])

# 19 Slice out the last 3 companies from the list
print(sort[-3:])

# 20 Slice out the middle IT company or companies from the list.
print(sort[len(it_companies) // 2 - 1:len(it_companies) // 2 + 1])

# 21 Remove the first IT company from the list
sort.remove(sort[0])
print(sort)

# 22 Remove the middle IT company or companies from the list
sort.remove(sort[len(sort) // 2])
print(sort)

# 23 Remove the last IT company from the list
sort.remove(sort[len(sort) - 1])
print(sort)

# 24 Remove all IT companies from the list
sort.clear()
print(sort)

# 25 Destroy the IT companies list
del sort # No Output

# 26 Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_languages = front_end + back_end
print(join_languages)

# 27 After joining the lists in question 26.
# Copy the joined list and assign it to a variable full_stack,
# then insert Python and SQL after Redux.
full_stack = join_languages
redux = "Redux"
index_fulL_stack = full_stack.index(redux) + 1
full_stack.insert(index_fulL_stack, 'Python')
full_stack.insert(index_fulL_stack + 1, 'SQL')
print(f"{full_stack}\n")

# =============================================== #

# EXERCISE 2
print("\nEXERCISES 2")

# 1 The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1.1 Sort the list and find the min and max age
ages.sort()
maximum = max(ages)
minimum = min(ages)
print(f"\n{ages},\nMax: {maximum}, Min: {minimum}")

# 1.2 Add the min age and the max age again to the list
ages.append(maximum)
ages.append(minimum)
print(f"Inserted {maximum} and {minimum}: {ages}")

# 1.3 Find the median age (one middle item or two middle items divided by two)
median_index = len(ages) // 2
if median_index % 2 == 0:
    if (ages[median_index - 1]) == ages[median_index]:
        print(f"Median: {ages[median_index]}")
    else:
        print(f"Median: {ages[median_index - 1], ages[median_index]}")
elif median_index % 2 == 1:
    print(f"Median: {ages[median_index]}")
else:
    print("No median.")

# 1.4 Find the average age (sum of all items divided by their number )
print(f"Average: {sum(ages) / len(ages)}")

# 1.5 Find the range of the ages (max minus min)
print(f"Range: {maximum - minimum}")

# 1.6 Compare the value of (min - average) and (max - average), use abs() method
print(f"Compare: Max - {abs(minimum - (sum(ages) / len(ages)))} and Min - {abs(maximum - (sum(ages) / len(ages)))}")

# 2 Find the middle country(ies)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(f"Middle Country: {countries[len(countries) // 2]}")

# 3 Divide the countries list into two equal lists
# if it is even if not one more country for the first half.
first_half = 0
second_half = 0
countries_half = len(countries) // 2
if countries_half % 2 == 0:
    first_half = countries[0:countries_half]
    second_half = countries[countries_half:len(countries)]
elif countries_half % 2 == 1:
    first_half = countries[0:(countries_half + 1)]
    second_half = countries[(countries_half + 1):len(countries)]
print(f"First Half: {first_half}"
        f"\nSecond Half: {second_half}")

# 4 Unpack the first three countries and the rest as scandic countries.
powerhouse_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = powerhouse_countries
print(f"['{ch}', '{ru}', '{us}']")
print(scandic)
