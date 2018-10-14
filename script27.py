#!/usr/bin/python
# -*- coding: utf-8 -*


#Write a Python program to find sequences of one upper case letter followed by lower case letters

import re

chaine = input("introduisez une chaine de caractères :")

pattern = r"[A-Z]+[a-z]+"

if re.match(pattern, chaine):
	print("la chaine matche bien")
else:
	print("la chaine ne matche pas")