#!/usr/bin/python
# -*- coding: utf-8 -*



# Write a Python program to find sequences of lowercase letters joined with a underscore


import re

chaine = input("Introduisez une chaine de caracteres :")

pattern = r"[a-z]+_"


if re.match(pattern, chaine):
	print("la chaine matche bien")
else:
	print("la chaine ne matche pas")