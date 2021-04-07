# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:20:20 2021

@author: Desktop
"""

from kanren import run, eq, var
#asignar una variable de valor 
x=var()
y=var()
#asignacion de valores
from kanren import Relation, facts
parent = Relation()
grandparent=Relation()
tios = Relation()
primos=Relation()
hijos=Relation()

#relacion de padre

facts(parent, ("miguelina", "amilkar"),
             ("miguelina", "belen"),
              ("ernesto", "amilkar"),
              ("ernesto", "belen"),
              ("remi","shana"),
              ("remi","israel"),
              ("willy", "shana"),
              ("willly","israel"),
              ("barbara",  "miguelina"),
              ("barbara",  "remi"),
              ("clemente",  "miguelina"),
              ("clemente",  "remi"))
#relacion abuelos
facts(grandparent,("clemente","amilkar"),
                  ("clemente","belen"),
                  ("clemente","shana"),
                  ("clemente","israel"),
                  ("barbara","amilkar"),
                  ("barbara","belen"),
                  ("barbara","shana"),
                  ("barbara","israel")
                  )
facts(tios,("remi","amilkar"),
          ("remi","belen"),
          ("willy","amilkar"),
          ("willly","belen"),
          ("miguelina","shana"),
          ("miguelina","israel"),
          ("ernesto","shana"),
          ("ernesto","israel"))
#relacion primos
facts(primos,("belen","shana"),
              ("belen","israel"),
              ("amilkar","shana"),
              ("amilkar","israel"),
              ("shana","belen"),
              ("shana","amilkar"),
              ("israel","belen"),
              ("israel","amilkar"),)
#relacion hijos
facts(hijos,("belen","miguelina"),
              ("belen","ernesto"),
              ("amilkar","miguelina"),
              ("amilkar","ernesto"),
              ("shana","remi"),
              ("shana","willy"),
              ("israel","remi"),
              ("israel","willy"))
    
def grandparent1(x, z):
    y = var()
    return (parent(x, y), parent(y, z))

print(run(1, x, parent(x,"remi")))
print(run(1, x, parent(x, "shana")))
print(run(1, x, parent(x, "remi")))
print(run(1, x, grandparent(x, "israel")))
print(run(1, x, parent(x, "miguelina")))
print(run(1, x, tios(x, "belen")))
print(run(1, x, tios(x, "shana")))
print(run(1, x, primos(x, "belen")))
print(run(1, x, grandparent(x, "belen")))
print(run(1, x, hijos (x, "willy")))
print(run(1, x, hijos (x, "ernesto")))


