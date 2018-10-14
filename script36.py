#!/usr/bin/python
# -*- coding: utf-8 -*


# Write a Python program to search some literals strings in a string
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'

import re

chaine = input("Introduisez une chaine de caractères")

pattern = r".*(fox).*"

if re.match(pattern, chaine):
	print("La chaine contient le mot fox")
else:
	print("la chaine ne contient pas le mot fox")