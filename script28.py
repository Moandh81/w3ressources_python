#!/usr/bin/python
# -*- coding: utf-8 -*




# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. 


import re

chaine = input("Introduisez une chaine de caraceteres :")

pattern = r"a.*b$"

if re.match(pattern, chaine):
	print("La chaine matche bien")
else:
	print("la chaine ne matche pas")