# input
like = input("what is this?")
print(like)

#zip the two lists
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 65]
names_and_heights = zip(names, heights)
print(list(names_and_heights))

#List comprehension
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade+10 for grade in grades]
print(scaled_grades)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

single_digits = range(0, 10)
for i in single_digits:
  print(i)

squares = []
for num in single_digits:
  squares.append(num**2)
print(squares)

cubes = [num**3 for num in single_digits]
print(cubes)