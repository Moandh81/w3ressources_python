#!/usr/bin/python
# -*- coding: utf-8 -*

# Write a Python program where a string will start with a specific number


import re

chaine = input("Introduisez une chaine de caracteres")

pattern = r"^9.*"

if re.match(pattern, chaine):
 	print("la chaine commence par le chiffre 9")
else:
 	print("la chaine ne commence pas par le chiffre 9")

