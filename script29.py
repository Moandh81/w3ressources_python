#!/usr/bin/python
# -*- coding: utf-8 -*



# Write a Python program that matches a word at the beginning of a string


import re 

chaine =input("Introduisez une chaine de caracteres :")

pattern = r"^([A-Z]*[a-z]+)."

if re.match(pattern, chaine):
	print("la chaine matche bien")
else:
	print("la chaine ne matche pas")
