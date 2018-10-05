#!/usr/bin/python
# -*- coding: utf-8 -*


#Python Data Type: String - Exercises

#Write a Python program to count the occurrences of each word in a given sentence

# I used the counter collections module for this exercise

chaine = " Ceci est une chaine de caracteres avec plusieurs mots et plusieurs phrases et plusieurs autres choses"

liste = chaine.split()


from collections import Counter

print(Counter(liste))
