from tkinter import *
import numpy as np
import random

## ========= Fonctions ========

def draw():
    dico_couleur={2:"#A9BCF5",4:"#5882FA",8:"#0040FF",16:"#0431B4",32:"#04B486",64:"#31B404",128:"#2EFE2E",256:"#9AFE2E",512:"#FFFF00",1024:"#FFBF00",2048:"#DF0101"}
    canevas.delete(ALL)
    for i in range(4):
        for j in range(4):
            if table[i,j]==0:
                canevas.create_rectangle(j*150,i*150,j*150+150,i*150+150,fill='white')
            else :
                canevas.create_rectangle(j*150,i*150,j*150+150,i*150+150,fill= dico_couleur.get(table[i,j]))
                canevas.create_text(j*150+75,i*150+75,text=str(table[i,j]),font=('Arial','50','bold'),fill='white')
                
def addnew():
    global table
    i,j=random.randrange(0,4),random.randrange(0,4)
    while table[i,j]!=0:
        i,j=random.randrange(0,4),random.randrange(0,4)
    r=random.randrange(0,20)
    if r==0:
        table[i,j]=4
    else:
        table[i,j]=2

def restart(self):
    global table
    table = np.zeros((4,4),int)
    addnew()
    addnew()
    draw()

def fermer(self):
   fenetre.destroy()
        
def up(self):
    global table
    copie=table.copy()
    for j in range(4):
        n=0
        while table[0,j]==0 and n<3:
            table[0,j],table[1,j],table[2,j],table[3,j]=table[1,j],table[2,j],table[3,j],0
            n=n+1
        n=0
        while table[1,j]==0 and n<2:
            table[1,j],table[2,j],table[3,j]=table[2,j],table[3,j],0
            n=n+1
        if table[2,j]==0:
           table[2,j],table[3,j]=table[3,j],0
        if table[0,j]==table[1,j]:
                table[0,j],table[1,j],table[2,j],table[3,j]=table[0,j]+table[1,j],table[2,j],table[3,j],0
        if table[1,j]==table[2,j]:
                table[1,j],table[2,j],table[3,j]=table[1,j]+table[2,j],table[3,j],0
        if table[2,j]==table[3,j]:
            table[2,j],table[3,j]=table[2,j]+table[3,j],0
    if table.tolist() != copie.tolist() :
        addnew()
        draw()

def down(self):
    global table
    copie=table.copy()
    for j in range(4):
        n=0
        while table[3,j]==0 and n<3:
            table[3,j],table[2,j],table[1,j],table[0,j]=table[2,j],table[1,j],table[0,j],0
            n=n+1
        n=0
        while table[2,j]==0 and n<2:
            table[2,j],table[1,j],table[0,j]=table[1,j],table[0,j],0
            n=n+1
        if table[1,j]==0:
           table[1,j],table[0,j]=table[0,j],0
        if table[3,j]==table[2,j]:
                table[3,j],table[2,j],table[1,j],table[0,j]=table[3,j]+table[2,j],table[1,j],table[0,j],0
        if table[2,j]==table[1,j]:
                table[2,j],table[1,j],table[0,j]=table[2,j]+table[1,j],table[0,j],0
        if table[1,j]==table[0,j]:
            table[1,j],table[0,j]=table[1,j]+table[0,j],0
    if table.tolist() != copie.tolist():
        addnew()
        draw()

def left(self):
    global table
    copie=table.copy()
    for i in range(4):
        n=0
        while table[i,0]==0 and n<3:
            table[i,0],table[i,1],table[i,2],table[i,3]=table[i,1],table[i,2],table[i,3],0
            n=n+1
        n=0
        while table[i,1]==0 and n<2:
            table[i,1],table[i,2],table[i,3]=table[i,2],table[i,3],0
            n=n+1
        if table[i,2]==0:
           table[i,2],table[i,3]=table[i,3],0
        if table[i,0]==table[i,1]:
                table[i,0],table[i,1],table[i,2],table[i,3]=table[i,0]+table[i,1],table[i,2],table[i,3],0
        if table[i,1]==table[i,2]:
                table[i,1],table[i,2],table[i,3]=table[i,1]+table[i,2],table[i,3],0
        if table[i,2]==table[i,3]:
            table[i,2],table[i,3]=table[i,2]+table[i,3],0
    if table.tolist() != copie.tolist():
        addnew()
        draw()

def right(self):
    global table
    copie=table.copy()
    for i in range(4):
        n=0
        while table[i,3]==0 and n<3:
            table[i,3],table[i,2],table[i,1],table[i,0]=table[i,2],table[i,1],table[i,0],0
            n=n+1
        n=0
        while table[i,2]==0 and n<2:
            table[i,2],table[i,1],table[i,0]=table[i,1],table[i,0],0
            n=n+1
        if table[i,1]==0:
           table[i,1],table[i,0]=table[i,0],0
        if table[i,3]==table[i,2]:
                table[i,3],table[i,2],table[i,1],table[i,0]=table[i,3]+table[i,2],table[i,1],table[i,0],0
        if table[i,2]==table[i,1]:
                table[i,2],table[i,1],table[i,0]=table[i,2]+table[i,1],table[i,0],0
        if table[i,1]==table[i,0]:
            table[i,1],table[i,0]=table[i,1]+table[i,0],0
    if table.tolist() != copie.tolist():
        addnew()
        draw()
  

## ========= Programme principal ========
        
table=np.array([[],])

table = np.zeros((4,4),int)
addnew()
addnew()

fenetre = Tk()
fenetre.title('2048')

Bouton1 = Button(fenetre, text = 'Exit (Esc)', command = fenetre.destroy)
Bouton1.pack()
fenetre.bind("<Escape>",fermer)

Bouton2 = Button(fenetre, text = 'Restrat (F2)', command = restart )
Bouton2.pack()
fenetre.bind("<F2>",restart)

canevas = Canvas(fenetre,width=600, height=600)
canevas.pack()
                
fenetre.bind("<Up>",up) 
fenetre.bind("<Down>",down) 
fenetre.bind("<Left>",left) 
fenetre.bind("<Right>",right)

draw()

fenetre.mainloop()
                    

