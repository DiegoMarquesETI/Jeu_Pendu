# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:29:55 2020

@author: xavie
"""

from random import randint


#fonction


#Fonction qui va trier les mots par ordre croissant, puis par ordre alphabétique
    

def Tri(Liste):
   return len(Liste), Liste.lower()


#Fonction qui ouvre le fichier et retourne un mot au hasard



def MotsFichier():
    Liste = []    
    Fichier = open("pendule.txt")
    for ligne in Fichier :
        Liste.append(ligne)
    Liste=sorted(Liste, key=Tri)    
    print(Liste)
    Indice = randint(0,len(Liste)-1)
    Fichier.close()
    Mot = Liste[Indice].upper()
    Mot = Mot[:-1]
    return Mot


#Fonction qui cache les lettres d'un mot par des underscores sauf si elles sont identiques à la 1ere lettre du mot mis en entrée de la fonction" 


def Underscore(Mot):
    L1 = Mot[0]
    MotModif=""
    for lettre in Mot :
        if lettre == L1:
            MotModif += L1
        else :
            MotModif += "_"
    return MotModif



#Fonction qui permet à l'utilisateur de saisir une lettre

def Saisie(LUtilise):
    
    Lettre = input("Saisir une lettre :")
    Lettre = Lettre.upper()
    while Lettre in LUtilise: #On véfifie que la lettre saisie soit bien une nouvelle lettre 
        print("Lettre deja choisie")
        Lettre = input("Saisir une lettre :")
        Lettre = Lettre.upper()
    while len(Lettre)!=1: #On véfifie si il n'y a pas eu d'erreur de saisie.  
        Lettre = input("Saisir une lettre :")
        Lettre = Lettre.upper()
    LUtilise.append(Lettre)
    return Lettre


#"Fonction qui modifie le compteur et indique le nombre de chance restant au joueur"
def Compteur(cpt,Resultat,MotModif):
    
    if Resultat == MotModif:
        cpt -= 1
        print('Nombre de chance : ' + str(cpt))
    else:
        print('Nombre de chance : ' + str(cpt))
    return cpt

#Fonction qui recupere le compteur et verifie si il y a encore des chances. Retourne vrai si encore chance et faux sinon"
def Perdu(cpt):
    if cpt==0:
        print("Perdu!")
        return False
    return True

#Fonction qui verifie la condition de victoire. Mot est le mot recherché et MotUnderscore le mot rempli par l'utilisateur
def Gagner(Mot,MotUnderscore):
    if Mot == MotUnderscore:
        print("Gagné!")
        return True
    return False


#Fontion qui réalise une modification du mot recherché. Prend en parametres le mot recherché, le mot avec underscore et le compteur et la liste des mots utilise et retourne le mot avec underscore
def Modif(Mot, MotUnderscore,cpt,LUtilise):
    Resultat =""  
    print("Les lettres interdites sont:",LUtilise)
    Lettre = Saisie(LUtilise)

    for i in range(len(Mot)) :
        if Lettre == Mot[i]:
            Resultat += Lettre
            
        else :
            Resultat +=MotUnderscore[i]

    cpt=Compteur(cpt,Resultat,MotUnderscore)
    return Resultat,cpt

