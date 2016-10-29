import Tkinter 

class ihm(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent=parent
        
        self.initialize()

    def initialize(self):
        #layout manager
        self.grid()
        

        #champ de texte (entrer)
        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')

        button = Tkinter.Button(self,text=u"Click me !")
        button.grid(column=1,row=0)

        label = Tkinter.Label(self,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        #redimensionnement auto
        self.grid_columnconfigure(0,weight=1)

    
