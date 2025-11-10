gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Do you like Daen or Dusk? ")
print("1) Dawn")
print("2) Dusk")
ques = int(input('>> '))
if ques == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
  print(f"Gryffindor: {gryffindor}")
  print(f"Ravenclaw: {ravenclaw}")
elif ques == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
  print(f"Hufflepuff: {hufflepuff}")
  print(f"Slytherin: {slytherin}")

print("When I’m dead, I want people to remember me as ")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
ques = int(input('>> '))
if ques == 1:
  hufflepuff = hufflepuff + 2
  print(f"Hufflepuff: {hufflepuff}")
elif ques == 2:
  slytherin = slytherin + 2
  print(f"Slytherin: {slytherin}")
elif ques == 3:
  ravenclaw = ravenclaw + 2
  print(f"Ravenclaw: {ravenclaw}")
elif ques == 4:
  gryffindor = gryffindor + 2
  print(f"Gryffindor: {gryffindor}")

print("Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
ques = int(input('>> '))
if ques == 1:
  slytherin = slytherin + 4
  print(f"Slytherin: {slytherin}")
elif ques == 2:
  hufflepuff = hufflepuff + 4
  print(f"Hufflepuff: {hufflepuff}")
elif ques == 3:
  ravenclaw = ravenclaw + 4
  print(f"Ravenclaw: {ravenclaw}")
elif ques == 4:
  gryffindor = gryffindor + 4
  print(f"Gryffindor: {gryffindor}")
else:
  print("Wrong input.")

print("\nResult")
print(f"Gryffindor: {gryffindor}")
print(f"Ravenclaw: {ravenclaw}")
print(f"Hufflepuff: {hufflepuff}")
print(f"Slytherin: {slytherin}")
