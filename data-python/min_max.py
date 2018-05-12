#!/usr/bin/env python
# -*- coding: utf-8 -*-

# enonce
# Notions abordées
#   - Boucle
#   - Conditions

#  Énoncé
# Garde forestier dans les merveilleuses plaines du Wyoming on vous demande de recenser chaque arbre par le taille et ainsi trouver le plus grand et le plus petit arbre

# MIN
# Input : [7, 9, 10, 1, 2, 18]
# Output : 1
# MAX
# Input : [7, 9, 10, 1, 2, 18]
# Output : 18

# code

val = [7, 9, 10, 1, 2, 18]
max_1 = 0
min_1 = val[0]

for i in val:
    if i > max_1:
        max_1 = i
    if i < min_1:
        min_1 = i

print ("la valeur maximale est {0}".format(max_1))
print ("la valeur minimale est {0}".format(min_1))


# 2ème possibilité avec fonction :

val = [7, 9, 10, 1, 2, 18]

def max1():
    max_1 = 0
    for i in val:
        if i > max_1:
            max_1 = i
    return max_1

def min1():
    min_1 = val[0]
    for i in val:
        if i < min_1:
            min_1 = i
    return min_1

print ("la valeur maximale est {0}".format(max1()))
print ("la valeur minimale est {0}".format(min1()))


# encore plus simple car la focntion existe déjà dans Python

print ("la valeur maximale est {0}".format(max(val)))
print ("la valeur minimale est {0}".format(min(val)))