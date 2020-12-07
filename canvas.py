# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:14:58 2020

@author: Diego
"""
from PENDULE import *


from tkinter import Tk,Label,Button,Entry,StringVar
Mafenetre=Tk()
Mafenetre.title('Jeu du pendu')
BoutonProposer=Button(Mafenetre,text='Proposer', command=Mafenetre.destroy)
BoutonProposer.pack(padx=5,pady=5)


Lettre=StringVar()
BoutonEntry=Entry(Mafenetre,textvariable=Lettre)
BoutonEntry.pack(padx=5,pady=50)

x = AffichageMot(MotsFichier(),LUtilise)
LabelMotChercher=Label(Mafenetre,text=x,fg='black',bg='white')
LabelMotChercher.pack(padx=2,pady=10)

cpt=IntVar()
cpt.set(str(cpt))
LabelCoup=Label(Mafenetre,textvariable=Coup,fg='black',bg='white')
LabelCoup.pack(padx=3,pady=20)


Largeur=600
Hauteur=450
Canevas=Canvas(Mafenetre,width=Largeur, height=Hauteur,bg='white')
Canevas.pack(padx=5,pady=5)
photo=PhotoImage(file='pendu.gif')
item=Canevas.create_image(300,200,image=photo)
Mafenetre.mainloop()