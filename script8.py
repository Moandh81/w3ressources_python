#!/usr/bin/python
# -*- coding: utf-8 -*

#Python Data Type: List - Exercises,

#Write a Python program to print the numbers of a specified list after removing even numbers from it


liste=range(1,11)
i= 0
listepair=[]

while i<len(liste):
	if liste[i] % 2 == 0:
		listepair.append(liste[i])
	i = i + 1

print(listepair)