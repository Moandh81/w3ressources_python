#!/usr/bin/python
# -*- coding: utf-8 -*



#Python Data Type: List - Exercises, 
#Exercice 1: Write a Python program to sum all the items in a list

liste = [1,4,45,3,5,9]

i=0
somme=0
while i<len(liste):
	somme = somme + liste[i]
	i = i + 1
print ("la somme des chiffres du tableau est :" + str(somme))