
#!/usr/bin/python
# -*- coding: utf-8 -*

#Write a Python program to remove multiple spaces in a string

import re 

chaine = "Ceci        est une chaine    contenant plusieurs espaces         "


pattern = r"\s{2,}"

print(re.sub(pattern, ' ', chaine))