#!/usr/bin/python
# -*- coding: utf-8 -*


#Python Data Type: String - Exercises

#Write a Python function to get a string made of 4 copies of
#the last two characters of a specified string (length must be at least 2

chaine="Hello world"

if len(chaine) >=2:
	print((chaine[len(chaine) -2] + chaine[len(chaine) - 1]) * 4)
else:
	print("la chaine n'a pas plus de deux caracteres et par conséquent elle ne peut pas etre traitée  ") 