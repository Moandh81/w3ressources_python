
#!/usr/bin/python
# -*- coding: utf-8 -*

#Write a Python program to find all five characters long word in a string

import re

chaine = "Salut, comment ca va ?. Bien, et toi ?"

liste = chaine.split()

pattern =r"\b[a-zA-Z0-9]+\b"

print(liste)

listemots= re.findall(pattern, chaine)

print(listemots)

i = 0

while i<len(listemots):
	if (len(listemots[i])>=5):
		print(listemots[i])
	i = i + 1