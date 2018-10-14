#!/usr/bin/python
# -*- coding: utf-8 -*


# Write a Python program that matches a word containing 'z', not start or end of the word


import re

chaine = input("Introduire une chaine de caractères :")

pattern = r"^(?![zZ]).*[zZ]+.*(?![zZ])$"

if re.match(pattern, chaine):
	print("la chaine matche bien")
else:
	print("la chaine ne matche pas")

