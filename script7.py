#!/usr/bin/python
# -*- coding: utf-8 -*

#Python Data Type: List - Exercises,

#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 

#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']


liste= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

if len(liste)>=6:
	liste.remove(liste[0])
	liste.remove(liste[3])
	liste.remove(liste[3])

print(liste)
	