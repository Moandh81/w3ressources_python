#!/usr/bin/python
# -*- coding: utf-8 -*


#Python Data Type: List - Exercises, 
#Exercice 2 : Write a Python program to multiplies all the items in a list


liste = [1,3,5,6,98,98,56]
i=0
produit=1
while i<len(liste):
	produit = (produit * liste[i])
	i = i + 1

print("le produit de la liste est :" + str(produit))  