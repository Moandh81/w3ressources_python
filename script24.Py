#!/usr/bin/python
# -*- coding: utf-8 -*


#Write a Python program that matches a string that has an a followed by three 'b'


import re

chaine = input("introduisez la chaine de caracteres :")

pattern = r"ab{3}"

if re.match(pattern, chaine):
	print("la chaine de acarecteres matche bien")
else:
	print("la chaine de caracteres ne matche pas")

