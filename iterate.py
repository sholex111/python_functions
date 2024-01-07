#name length


def name_length():
  """Takes input of a name and returns the length of the name."""

  name = input("Enter your name: ")
  name_length = len(name)
  print(name, "has", name_length, "letters.")


name_length()