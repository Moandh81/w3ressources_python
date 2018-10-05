#!/usr/bin/python
# -*- coding: utf-8 -*


#Python Data Type: List - Exercises, 
#Exercice 4: Write a Python program to get the largest number from a list


liste = [1,3,5,6,98,98,56 , 45, 190]
i=0
max = 0

while i<len(liste):
	if liste[i]>max:
		max = liste[i]
	i = i + 1


print("le maximum de cette liste est :" + str(max) )	