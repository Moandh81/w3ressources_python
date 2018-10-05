#!/usr/bin/python
# -*- coding: utf-8 -*

#Python Data Type: List - Exercises,

#Write a Python program to append a list to the second list

liste1 = ["hello", "there", "Hi", "everyone"]
liste2 =  ["bonjour", "tout", "le", "monde"]

i = 0

while i<len(liste1):
	liste2.append(liste1[i])
	i= i + 1

print(liste2)