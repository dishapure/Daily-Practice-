# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:11:02 2023

@author: disha
"""

foo = "Mary had 21 little sheep"
print(foo)
print(str(foo.split()[0]).split()[0]+" is "+str(foo.split()[2]).split()[0]+" years old")

name = "disha"

print(name.split()[0])
#print(name.split()[1])


strng = '\''.join(("mary","had","21","sheep"))
print(strng)
print(strng[0:1])
print(not strng[0:1].lower())