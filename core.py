# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:50:19 2020

@author: Diego
"""

from PENDULE import MotsFichier
from PENDULE import Underscore
from PENDULE import Perdu
from PENDULE import Gagner
from PENDULE import Modif


cpt=8
Rejouer="1"


while Rejouer=="1":
    cpt=8
    LUtilise=[]
    Mot = MotsFichier()
    LUtilise.append(Mot[0])
    MotUnderscore = Underscore(Mot)
    print(MotUnderscore)   
    while (Perdu(cpt)==True and Gagner(Mot, MotUnderscore)==False):
        
        MotUnderscore,cpt=Modif(Mot,MotUnderscore,cpt,LUtilise)
        print(MotUnderscore)
    
    Rejouer=input("Voulez vous rejouer ? 1 oui 0 non")
