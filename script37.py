#!/usr/bin/python
# -*- coding: utf-8 -*

# Write a Python program to find all words starting with 'a' or 'e' in a given string


import re

chaine = " The fox aumped ever Ahe Eazy dog"


pattern = r"\b[a-zA-Z0-9]+\b"

liste =re.findall(pattern, chaine)

i = 0

while i<len(liste):
	if (liste[i][0] in ["a","A"]):
		print("la chaine contient un mot commençant par la lettre A ")
	if (liste[i][0] in ["e","E"]):
		print("la chaine contient un mot commençant par la lettre E")
	else:
		print("la chaine ne contient aucun mot commençant par la lettre A ou E")

	i=i+1	






