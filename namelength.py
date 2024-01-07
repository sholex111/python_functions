#shotech learn Python function

def itr():
 """
 A simple Python function showing iteration.
 """

 # Iterate over a list of numbers
 numbers = [1, 2, 3, 4, 5]
 for number in numbers:
   print(f"Number: {number}")

 # Iterate over a range of numbers
 for i in range(1, 6):
   print(f"Number: {i}")

 # Iterate over a dictionary
 fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
 for fruit, color in fruits.items():
   print(f"Fruit: {fruit}, Color: {color}")


 for fruit, color in fruits.items():
   print(f"{fruit} is {color}")

# Call the function to see its output
itr()
