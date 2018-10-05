#!/usr/bin/python
# -*- coding: utf-8 -*


#Write a Python function to create the HTML string with tags around the word(s).
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def add_tags(balise, chaine):
	print("<"+ balise + "> " + chaine  + " </"+balise+">")


add_tags("i", "python")