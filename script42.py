
#!/usr/bin/python
# -*- coding: utf-8 -*

#Write a Python program to find all adverbs and their positions in a given sentence


import re 

chaine = "Clearly  and vehemently he has no excuse for such behavior"

pattern =r"\b[a-zA-Z]+\b"

liste = re.findall(pattern, chaine)

adverb_pattern = r"[a-zA-Z]+(ly)"

i = 0

while i<len(liste):
	if re.match(adverb_pattern,liste[i]):
		print(liste[i])
	i = i + 1