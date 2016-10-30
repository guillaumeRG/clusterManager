import Tkinter
from Tkinter import StringVar


class ihm(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent=parent
        
        self.initialize()

    def initialize(self):
        #layout manager
        self.grid()
        

        #champ de texte (entrer)
        self.value = StringVar() 
        self.value.set("Noeud")
        self.entry = Tkinter.Entry(self,fg='grey',textvariable=self.value)
        self.entry.grid(column=0,row=1,sticky='EW')
        
        
        self.button = Tkinter.Button(self,text=u"Ok")
        self.button.grid(column=1,row=1)

        self.label = Tkinter.Label(self,anchor="center",text = 'Nom du noeud :',fg="black",bg="white")
        self.label.grid(column=0,row=0,columnspan=2,sticky='EW')
        #redimensionnement auto
        self.grid_columnconfigure(0,weight=1)
        self.geometry("800x600+300+0")
        #800x600 <== taille de la fenetre le "x" c'est comme xor
        #+300 <== ou se positionne en x ou essai -300
        #+0 <=== ou se positionne en y ou essai-0

    
