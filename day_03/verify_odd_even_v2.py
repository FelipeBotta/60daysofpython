input = input("Insert a number:")

try:
  number = int(input)
  if number % 2 == 0:
    print("Even")
  else:
    print("Odd")
except ValueError:
  print("This input isn't a number")