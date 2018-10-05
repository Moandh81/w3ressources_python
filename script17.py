#!/usr/bin/python
# -*- coding: utf-8 -*


#Python Data Type: String - Exercises

#Write a Python script that takes a list of words and returns the length of the longest one

chaine = "ceci est une chaine de caractères"

listemots = chaine.split()
listelen = []
i = 0

while i<len(listemots):
	listelen.append(len(listemots[i]))
	i= i +1



print("Le mot le plus long est :" + listemots[listelen.index(max(listelen))])


