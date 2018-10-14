#!/usr/bin/python
# -*- coding: utf-8 -*


#Write a Python program that matches a word at end of string, with optional punctuation


import re

chaine = input("Introduire une chaine de caracteres :")

pattern = r".([a-z]+|[A-Z]+[.,?!]?$)"

if re.match(pattern, chaine):
	print("la chaine matche bien")
else:
	print("la chaine ne mtche pas")

