#!/usr/bin/python
# -*- coding: utf-8 -*

#Python Data Type: String - Exercises

# Write a Python function that takes a list of words and returns the length of the longest one

liste= ["hello", "world","bonjour tout le monde", "etc, etc ..."]

i = 0

char=[]

while i<len(liste):
	char.append(len(liste[i]))
	i= i + 1



# print(char.index(max(char)))

print('la chaine la plus longue est :' + liste[char.index(max(char))])	
	