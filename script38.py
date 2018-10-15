
#!/usr/bin/python
# -*- coding: utf-8 -*


#Write a Python program to replace all occurrences of space, comma, or dot with a colon


import re

chaine = "Ceci est une chaine qui , contient, plusieurs. signes de ponctuations."

pattern = r"[,\.\s]+"

print(re.findall(pattern, chaine))

print(re.sub(pattern, ':', chaine))