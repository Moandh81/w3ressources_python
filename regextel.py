#!/usr/bin/python
# -*- coding: utf-8 -*


# test of regular expressions
# script qui permet de vérifier un numéro de téléphone français
# Le numéro doit commencer par zéro
# le format des chiffres peut etre le suivant :

# 0X XX XX XX XX

# 0X-XX-XX-XX-XX

# 0X.XX.XX.XX.XX

# 0XXXXXXXXX


import time

debut = time.time()

import re
numero = input("introduisez le numéro de téléphone français valide :")

pattern = r"^0[0-9]([-. ][0-9]{2}){4}$"

if re.match(pattern, numero):
	print("Ceci est un numéro de téléphone valide")
else:
	print("Ceci n'est pas un numéro de téléphone valide")


fin = time.time()

duree = fin - debut

print(str(duree))