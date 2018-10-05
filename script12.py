#!/usr/bin/python
# -*- coding: utf-8 -*

#Python Data Type: List - Exercises,

#  Write a Python program to check whether a list contains a sublist.


liste=[1,3,24,3,4,6, ["un tableau"],6,5,5,90,87]
i = 0

while i<len(liste):
	if isinstance(liste[i],list) == True:
		print("Le tableau contient un sous tableau")
	i = i + 1