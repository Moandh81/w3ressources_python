#!/usr/bin/python
# -*- coding: utf-8 -*


#Write a Python program that matches a string that has an a followed by zero or one 'b'


import re


chaine = input("introduisez une chaine de caracteres :")

pattern = r"ab?"

if re.match(pattern, chaine):
	print("la chaine de caracteres mache")
else:
	print("la chaine de caractères ne matche pas")