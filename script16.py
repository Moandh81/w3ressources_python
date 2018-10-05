#!/usr/bin/python
# -*- coding: utf-8 -*


#Python Data Type: String - Exercises

#Write a Python function to reverses a string

chaine="hell"

inverse=""
i = len(chaine)

while i>0:
	inverse = inverse + chaine[i-1]
	i=i-1


print(inverse)

