import Tkinter
from Tkinter import StringVar
from Tkinter import LabelFrame


class ihm(Tkinter.Tk):

    def entrer():
        print 'click'
        self.value.set("bonjour")
        self.entrer.pack()
        
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent=parent
        
        self.initialize()
    
        
    def initialize(self):
        #layout manager
        self.grid() 

        #champ de texte (entrer)
        self.lframe = LabelFrame(self, text="Nom du noeud", padx=50, pady=20)
        self.lframe.pack(fill="both", expand="yes")
        self.lframe.grid(column=0,row=0,sticky='EW')
        
        self.value = StringVar() 
        #self.value.set("Noeud")
        self.entrer = Tkinter.Entry(self.lframe,fg='grey',textvariable=self.value).pack()
                
        self.button = Tkinter.Button(self,text="Ok",command=self.entrer)
        self.button.grid(column=1,row=0)

        #self.label = Tkinter.Label(self,anchor="center",text = 'Nom du noeud :',fg="black",bg="white")
        #self.label.grid(column=0,row=0,columnspan=2,sticky='EW')
        #redimensionnement auto
        self.grid_columnconfigure(0,weight=1)
        self.geometry("800x600+300+0")
        #800x600 <== taille de la fenetre le "x" c'est comme xor
        #+300 <== ou se positionne en x ou essai -300
        #+0 <=== ou se positionne en y ou essai-0

    
