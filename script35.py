#!/usr/bin/python
# -*- coding: utf-8 -*


#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. 


import re

chaine = input("Introduisez une chaine de caracteres")

pattern = r"^(?![0-9])*[0-9]{1,3}(?![0-9])*"


if re.match(pattern, chaine):
	print("La chaine contient des chiffres de longueur max 3")
else:
	print("la chaine ne contient pas de chiffres de longueur max 3")