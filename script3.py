#!/usr/bin/python
# -*- coding: utf-8 -*


#Exercice 3 : Ecrire un programme qui calcule le factoriel d'un nombre entier

nombre = 10
liste=range(1,nombre+1)
produit=1
i=0

while i<len(liste):
	produit=produit*liste[i]
	i=i+1


print("le factoriel de " + str(nombre) + "est  : " + str(produit))



