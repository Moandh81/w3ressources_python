#!/usr/bin/python
# -*- coding: utf-8 -*


#Python Data Type: List - Exercises, 
#Exercice 6:  Write a Python program to count the number of strings
#where the string length is 2 or more and the first and last character are same from a given list of strings.

liste = ['abc', 'xyz', 'aba', '1221']
i = 0
n=0

while i<len(liste):
	if (len(liste[i])>2) and (liste[i][0] == liste[i][len(liste[i])-1]):
		print(str(liste[i]))
	i = i + 1