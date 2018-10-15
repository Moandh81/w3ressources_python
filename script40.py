
#!/usr/bin/python
# -*- coding: utf-8 -*

#Write a Python program to find all three, four, five characters long words in a string

chaine = "Salut, comment ca va ?. Bien, et toi ?"


import re

pattern = r"\b[a-zA-Z0-9]+\b"

liste = re.findall(pattern, chaine)

print(liste)

i = 0

while i<len(liste):
		if (len(liste[i])>=3) and (len(liste[i])<=5):
				print(liste[i])
		i = i + 1	