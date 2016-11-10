import Tkinter
from Tkinter import StringVar
from Tkinter import LabelFrame
import service

class ihm(Tkinter.Tk):
    
    services = []
    nodes = []
    serviceManager=service.service()
    def reset(self):
        global nodes
        global services
        self.nodes=[]
        self.services=[]
        self.outputServices = Tkinter.Text(self)
        self.outputServices.grid(column=1,row=1)
        self.outputNode = Tkinter.Text(self)
        self.outputNode.grid(column=0,row=1)
    def start(self):
        print'start'
        global nodes
        global services
        global serviceManager
        args = []
        j=0
        for i in range(1,(len(self.nodes)+len(self.services))):
            if i < len(self.nodes):
                args.append(self.nodes[i-1])
            else:
                 args.append(self.services[j])
                 j=j+1
        args.append("start")
        if  self.nodes[0] != "":
            self.serviceManager.start(args,0)
            
    def status(self):
        print'status'
        global nodes
        global services
        global serviceManager
        args = []
        j=0
        for i in range(1,(len(self.nodes)+len(self.services))):
            if i < len(self.nodes):
                args.append(self.nodes[i-1])
            else:
                 args.append(self.services[j])
                 j=j+1
        args.append("status")
        if  self.nodes[0] != "":
            self.serviceManager.status(args,1)
    def stop(self):
        print 'stop'
        print'status'
        global nodes
        global services
        global serviceManager
        args = []
        j=0
        for i in range(1,(len(self.nodes)+len(self.services))):
            if i < len(self.nodes):
                args.append(self.nodes[i-1])
            else:
                 args.append(self.services[j])
                 j=j+1
        args.append("stop")
        if  self.nodes[0] != "":
            self.serviceManager.stop(args)
    def fnct(self,event):
        if self.entrerNode.get() != "":
            print self.entrerNode.get()
            self.outputNode.insert('1.0',self.entrerNode.get()+'\n')
            global nodes
            self.nodes.append('test')
            self.valueNode.set("")

        if self.entrerService.get() !="":
            print self.entrerService.get()
            self.outputServices.insert('1.0',self.entrerService.get()+'\n')
            global services
            self.services.append(self.entrerService.get())
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
        self.outputServices.grid(column=1,row=1)
        
        self.outputNode = Tkinter.Text(self)
        self.outputNode.grid(column=0,row=1)

        self.start=Tkinter.Button(self,text="Start",command=self.start)
        self.start.grid(column=0,row=2)

        self.start=Tkinter.Button(self,text="Reset",command=self.reset)
        self.start.grid(column=2,row=0)

        self.stop=Tkinter.Button(self,text="Stop",command=self.stop)
        self.stop.grid(column=1,row=2)

        self.status=Tkinter.Button(self,text="Status",command=self.status)
        self.status.grid(column=2,row=2)
        #self.label = Tkinter.Label(self,anchor="center",text = 'Nom du noeud :',fg="black",bg="white")
        #self.label.grid(column=0,row=0,columnspan=2,sticky='EW')
        #redimensionnement auto
        self.grid_columnconfigure(0,weight=1)
        self.geometry("800x600+300+0")
        #800x600 <== taille de la fenetre le "x" c'est comme xor
        #+300 <== ou se positionne en x ou essai -300
        #+0 <=== ou se positionne en y ou essai-0

    
