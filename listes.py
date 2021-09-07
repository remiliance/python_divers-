import pprint
from functools import reduce


def mettre_au_carre(x):
    return x ** 2  # x ** 2 = x puissance 2, pour les cerveaux lents :-'


def appliquer_fonction(fonc, valeur):
    return fonc(valeur)  # On utilise la fonction callback fonc avec comme paramètre valeur.

print(appliquer_fonction(mettre_au_carre, 3)) # Affiche 9, c'est à dire mettre_au_carre(3)

li = [3, 1, 4, 2, 5]
print (li)
print(li[0:3:1])
print(li[0:3])

#print(appliquer_fonction(mettre_au_carre, li))

def carre(x): return x ** 2

def pair(x): return not bool(x % 2)

l3=list(map(pair, [1, 2, 3, 4, 5]))  # Affiche [False, True, False, True, False], c'est à dire si le nombre est pair.
print(l3)
print (list(map(carre, [1, 2, 3, 4, 5]))) # Affiche [1, 4, 9, 16, 25], c'est à dire le carré de chaque élément
print (list(filter(pair,(map(carre, [1, 2, 3, 4, 5]))))) # Affiche [1, 4, 9, 16, 25], c'est à dire le carré de chaque élément

def produit(x, y): return x * y
"""
l2=list(reduce(produit, [1, 2, 3], 1)) # Affiche [1, 4, 9, 16, 25], c'est à dire le carré de chaque élément
print(l2)
"""

def petit_carre(x): return x ** 2 < 16


def pair(x): return not bool(x % 2)


print
filter(petit_carre,
       [1, 2, 3, 4, 5])  # Affiche [1, 2, 3], c'est à dire les nombres dont les carrés sont inférieurs à 16.

print
filter(pair, [1, 2, 3, 4, 5])  # Affiche [2, 4], c'est à dire les nombres pairs de la liste.

# Python 3
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)


def addition(x, y): return x + y





def appcarre(element, liste): return liste + [element ** 2]


print
reduce(addition, [1, 2, 3], 0)  # Équivaut à ((0 + 1) + 2) + 3
print
reduce(produit, [1, 2, 3], 1)  # Équivaut à ((1 * 1) * 2) * 3
print
reduce(appcarre, [1, 2, 3], [])  # Équivaut à map(carre, [1, 2, 3]) ;)
