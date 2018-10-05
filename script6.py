#!/usr/bin/python
# -*- coding: utf-8 -*

#Python Data Type: List - Exercises,

#Write a Python program to find the list of words that are longer than n from a given list of words.

liste = ["Hello", "world","slide","camel","qfqqsdqsd","Hello there", "hi everyone", "simple string and list", "str"]

n = 5
i=0
newlist=[]


while i<len(liste):
	if len(liste[i]) > n:
		newlist.append(liste[i])
	i = i + 1 

print(newlist)	