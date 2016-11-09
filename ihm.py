import Tkinter
from Tkinter import StringVar
from Tkinter import LabelFrame


class ihm(Tkinter.Tk):

    def fnct(self,event):
        if self.entrerNode.get() != "":
            print self.entrerNode.get()
            self.outputNode.insert('1.0',self.entrerNode.get()+'\n')
            self.valueNode.set("")

        if self.entrerService.get() !="":
            print self.entrerService.get()
            self.outputServices.insert('1.0',self.entrerService.get()+'\n')
            self.valueService.set("")
        
        
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent=parent
        self.bind("<Return>",self.fnct)
        
        self.initialize()
    
        
    def initialize(self):
        #layout manager
        self.grid() 

        #champ de texte (entrer)
        self.lframe = LabelFrame(self, text="Nom du noeud", padx=50, pady=20)
        self.lframe.grid(column=0,row=0,sticky='EW')

        self.lframeService = LabelFrame(self, text="Nom du service", padx=50, pady=20)
        self.lframeService.grid(column=1,row=0,sticky='EW')
        
        self.valueNode = StringVar() 
        #self.valueNode.set("Noeud")
        self.entrerNode = Tkinter.Entry(self.lframe,fg='grey',textvariable=self.valueNode)
        self.entrerNode.pack()

        self.valueService = StringVar() 
        #self.valueService.set("Noeud")
        self.entrerService = Tkinter.Entry(self.lframeService,fg='grey',textvariable=self.valueService)
        self.entrerService.pack()
        
        self.buttonNode = Tkinter.Button(self.lframe,text="Ok",command=self.fnct)
        self.buttonNode.pack()

        self.buttonService = Tkinter.Button(self.lframeService,text="Ok",command=self.fnct)
        self.buttonService.pack()

        self.outputServices = Tkinter.Text(self)
        self.outputServices.grid(column=1,row=2)
        
        self.outputNode = Tkinter.Text(self)
        self.outputNode.grid(column=0,row=2)

        #self.label = Tkinter.Label(self,anchor="center",text = 'Nom du noeud :',fg="black",bg="white")
        #self.label.grid(column=0,row=0,columnspan=2,sticky='EW')
        #redimensionnement auto
        self.grid_columnconfigure(0,weight=1)
        self.geometry("800x600+300+0")
        #800x600 <== taille de la fenetre le "x" c'est comme xor
        #+300 <== ou se positionne en x ou essai -300
        #+0 <=== ou se positionne en y ou essai-0

    
