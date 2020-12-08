# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:14:58 2020

@author: Diego
"""
from PENDULE import *
from core import cpt

from tkinter import Tk,Label,Button,Entry,StringVar,Canvas,PhotoImage

#Création de la fenêtre de jeu
Mafenetre=Tk()
Mafenetre.title('Jeu du pendu')


#Création du bouton proposer
BoutonProposer=Button(Mafenetre,text='Proposer', command=Mafenetre.destroy)
BoutonProposer.pack(padx=5,pady=5)

#Création du bouton entry
Lettre=StringVar()
BoutonEntry=Entry(Mafenetre,textvariable=Lettre)
BoutonEntry.pack(padx=5,pady=50)

#Label du mot à trouver
x=Underscore(MotsFichier())
LabelMotChercher=Label(Mafenetre,text=x,fg='black',bg='white')
LabelMotChercher.pack(padx=2,pady=10)

# Label pour indiquer le nombre de coups encore restants

vie=set(str(cpt))
LabelCoup=Label(Mafenetre,textvariable=vie,fg='black',bg='white')



#Création bouton fermer
BoutonQuitter=Button(Mafenetre,text='Quitter',command=Mafenetre.destroy)

#Création du canvas
width=600
height=450
Canevas=Canvas(Mafenetre,width=200, height=200,bg='white')
photo=PhotoImage(file="bonhomme"+str(cpt)+"."+"gif")
item=Canevas.create_image(100,100,image=photo)



#Mise en page
LabelCoup.grid(row=1,sticky='E')
LabelMotChercher.grid(row=2, sticky='S')
BoutonProposer.grid(row=3)
BoutonEntry.grid(row=4)
BoutonQuitter.grid(row=5, sticky='NW')
Canevas.grid(row=1,column=2,rowspan=5)
Mafenetre.mainloop()

