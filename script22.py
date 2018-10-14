#!/usr/bin/python
# -*- coding: utf-8 -*



# Write a Python program that
# matches a string that has an a followed by 1 or more b's

import re

chaine = input("Introduisez une chaine de caracteres :")

pattern = r"ab+"

if re.match(pattern, chaine):
	print("la chaine de caractères matche bien")
else:
	print("la chaine de caractres ne matche pas")