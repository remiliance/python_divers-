# Python program to
# demonstrate sets

# Same as {"a", "b", "c"}
myset = set(["a", "b", "c"])
print(myset)

# Adding element to the set
myset.add("d")
myset.add("a")
myset.add("o")
print(myset)

# Python program to demonstrate differences
# between normal and frozen set

# Same as {"a", "b","c"}
normal_set = set(["a", "b", "c"])

print("Normal Set")
print(normal_set)

# A frozen set
frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(frozen_set)


ma_liste = ["chien", "chat"]
print(ma_liste)

ma_liste.append("tt")
print(ma_liste)


# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# frozen_set.add("h")

result = {}
result[1]= "valeur1"
result[1]= "valeur2"
print(result)

# A Python program to
# demonstrate adding elements
# in a set

# Creating a Set
people = {"Jay", "Idrish", "Archi"}

#people = set(["a", "b", "c"])

print("People:", end=" ")
print(people)

# This will add Daxit
# in the set
people.add("Daxit")
print(people)
# Adding elements to the
# set using iterator
for i in range(1, 6):
    people.add(i)

print("\nSet after adding element:", end=" ")
print(people)
