#!/usr/bin/python
# -*- coding: utf-8 -*

# Write a Python program  to check for a number at the end of a string

import re

chaine = input("Introduisez une chaine de caractères :")

pattern =r".*[0-9]+"

if re.match(pattern, chaine):
	print("la chaine se termine par un chiffre")
else:
	print("la chaine ne se termine pas par un chiffre")

