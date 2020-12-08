# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:14:58 2020

@author: Diego
"""
from PENDULE import MotsFichier,Saisie,Gagner,Perdu,Tri,Underscore,Compteur,Modif
cpt=8

from tkinter import Tk,Label,Button,Entry,StringVar,Canvas,PhotoImage

#Création de la fenêtre de jeu
Mafenetre=Tk()
Mafenetre.title('Jeu du pendu')

image1=PhotoImage(master=Mafenetre, file='bonhomme1.gif')
image2=PhotoImage(master=Mafenetre, file='bonhomme2.gif')
image3=PhotoImage(master=Mafenetre, file='bonhomme3.gif')
image4=PhotoImage(master=Mafenetre, file='bonhomme4.gif')
image5=PhotoImage(master=Mafenetre, file='bonhomme5.gif')
image6=PhotoImage(master=Mafenetre, file='bonhomme6.gif')
image7=PhotoImage(master=Mafenetre, file='bonhomme7.gif')
image8=PhotoImage(master=Mafenetre, file='bonhomme8.gif')

#Création du bouton entry
Lettre=StringVar()
BoutonEntry=Entry(Mafenetre,textvariable=Lettre)


#Label du mot à trouver
Moot=StringVar()
MotAleatoire=MotsFichier()
Tiret=Underscore(MotAleatoire)
Moot=Tiret

LabelMotChercher=Label(Mafenetre,text=Moot,fg='black',bg='white')

# Label pour indiquer le nombre de coups encore restants
vie=StringVar()
vie.set("Nombre de coups restants: "+str(cpt))
LabelCoup=Label(Mafenetre,textvariable=vie,fg='black',bg='white')

#Création du bouton proposer
BoutonProposer=Button(Mafenetre,text='Proposer',command = Modif(MotAleatoire, Tiret, cpt,[MotAleatoire[0]]))

#Création bouton fermer
BoutonQuitter=Button(Mafenetre,text='Quitter',command=Mafenetre.destroy)

#Création du canvas
Largeur=300
Hauteur=300
Canevas=Canvas(Mafenetre, height= Hauteur, width=Largeur,bg='white')
item = Canevas.create_image(150,150,image=image1)



#Mise en page
LabelCoup.grid(row=2)
LabelMotChercher.grid(row=3)
BoutonProposer.grid(row=4)
BoutonEntry.grid(row=5)
BoutonQuitter.grid(row=6)
Canevas.grid(row=1,column=2,rowspan=5)
Mafenetre.mainloop()


