#!/usr/bin/python
# -*- coding: utf-8 -*


#Write a Python program that matches a string that has an a followed by two to three 'b's


import re

chaine = input("introduisez la chaine de caracteres :")

pattern = r"ab{2,3}"

if re.match(pattern, chaine):
	print("la chaine matche bien")
else:
	print("la chaine ne matche pas")
