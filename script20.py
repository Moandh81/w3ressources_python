#!/usr/bin/python
# -*- coding: utf-8 -*


# Write a Python program to count and display the vowels of a given text.

chaine = "Ceci est une chaine de caracteres"

voyelles = ["a", "e", "é", "è", "i", "u", "o", "y"]

i = 0
nbrevoy=0

while i<len(chaine):
	if chaine[i] in voyelles:
		nbrevoy = nbrevoy + 1
		print(chaine[i])
	i = i + 1

print(nbrevoy)