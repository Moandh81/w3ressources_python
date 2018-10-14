#!/usr/bin/python
# -*- coding: utf-8 -*


#Write a Python program that matches a word containing 'z'

import re

chaine = input("Introduisez une chaine de caracteres")

pattern = r".*[zZ].*"

if re.match(pattern, chaine):
	print("la chaine contient la lettre z")
else:
	print("la chaine ne contient pas la lettre z")



