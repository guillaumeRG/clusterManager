import Tkinter
from Tkinter import StringVar
from Tkinter import LabelFrame
import service
import dep
class ihm(Tkinter.Tk):
    
    services = []
    nodes = []
    serviceManager=service.service()
    configManager = dep.dep()
    link=''
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
        print'----------------start----------------'  
        global nodes
        global services
        global serviceManager
        args = ['service.py']

        for i in range(1,(len(self.nodes)+1)):
            args.append(self.nodes[i-1])
            
        args.append('service')
  
        for i in range(0,(len(self.services))):
            
            args[len(self.nodes)+1]=self.services[i]
            if  self.nodes[0] != "":
                if self.services[0] != "":
                    self.serviceManager.start(args)
        print''            
            
    def status(self):
        print'----------------status----------------'
        global nodes
        global services
        global serviceManager
        args = ['service.py']
        args.append('service')
        args.append('service')
        for i in range(1,(len(self.nodes)+1)):
            args[1]=self.nodes[i-1]
            
            for i in range(0,(len(self.services))):
            
                args[2]=self.services[i]                
        
                if  self.nodes[0] != "":
                    if self.services[0] != "":
                        ret=self.serviceManager.status(args,1)
                        if ret ==0:
                            print'Service : '+args[2]+' sur : '+args[1]+ ' status : non-demarre'
                        elif ret ==1:
                            print'Service : '+args[2]+' sur : '+args[1]+ ' status : demarre'
       
        print''
        
            
    def stop(self):
        print'----------------stop----------------'
        global nodes
        global services
        global serviceManager
        args = ['service.py']

        for i in range(1,(len(self.nodes)+1)):
            args.append(self.nodes[i-1])
            
        args.append('service')
 
        for i in range(0,(len(self.services))):
            
            args[len(self.nodes)+1]=self.services[i]
            if  self.nodes[0] != "":
                if self.services[0] != "":
                    self.serviceManager.stop(args)
        print''
    def fnct(self,event):
        if self.entrerNode.get() != "":
            #print self.entrerNode.get()
            self.outputNode.insert('1.0',self.entrerNode.get()+'\n')
            global nodes
            self.nodes.append(self.entrerNode.get())
            self.valueNode.set("")

        if self.entrerService.get() !="":
            #print self.entrerService.get()
            self.outputServices.insert('1.0',self.entrerService.get()+'\n')
            global services
            self.services.append(self.entrerService.get())
            self.valueService.set("")
    def btn(self):
        if self.entrerNode.get() != "":
            #print self.entrerNode.get()
            self.outputNode.insert('1.0',self.entrerNode.get()+'\n')
            global nodes
            self.nodes.append(self.entrerNode.get())
            self.valueNode.set("")

        if self.entrerService.get() !="":
            #print self.entrerService.get()
            self.outputServices.insert('1.0',self.entrerService.get()+'\n')
            global services
            self.services.append(self.entrerService.get())
            self.valueService.set("")
    def startConfig(self):
        global configManager        
        self.configManager.targetNode('cfg/'+self.entrerConfig.get())
        self.configManager.targetService('cfg/'+self.entrerConfig.get())
        self.configManager.link('cfg/'+self.entrerConfig.get())
        global nodes
        self.nodes = self.configManager.getTargetNodes()

        global services
        self.services = self.configManager.getTargetServices()

        global link
        self.link = self.configManager.getLinkedTo()
        
        self.linkedStart()
        
    def startConfigProcedure(self):
        global configManager
        global link
        
        self.configManager.targetNode('cfg/'+self.link[0])
        self.configManager.targetService('cfg/'+self.link[0])
        self.configManager.link('cfg/'+self.link[0])
        global nodes
        self.nodes = self.configManager.getTargetNodes()

        global services
        self.services = self.configManager.getTargetServices()
        self.link[0] = ''
        
        self.link = self.configManager.getLinkedTo()
        
        self.linkedStart()
        
    def linkedStart(self):
        print'----------------start----------------'  
        global nodes
        global services
        global serviceManager
        args = ['service.py']

        for i in range(1,(len(self.nodes)+1)):
            args.append(self.nodes[i-1])
            
        args.append('service')
  
        for i in range(0,(len(self.services))):
            
            args[len(self.nodes)+1]=self.services[i]
            if  self.nodes[0] != "":
                if self.services[0] != "":
                    self.serviceManager.start(args)
        print''    
        global nodes
        global services
        self.nodes=[]
        self.services=[]
        global link
        
        if self.link[0] != '':
        
            self.startConfigProcedure()
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
        
        self.buttonNode = Tkinter.Button(self.lframe,text="Ok",command=self.btn)
        self.buttonNode.pack()

        self.buttonService = Tkinter.Button(self.lframeService,text="Ok",command=self.btn)
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

        self.valueConfig = StringVar()
        self.entrerConfig = Tkinter.Entry(self,fg='grey',textvariable=self.valueConfig)        
        self.entrerConfig.grid(column=0,row=3)

        self.config=Tkinter.Button(self,text="Start config",command=self.startConfig)
        self.config.grid(column=1,row=3)
        #self.label = Tkinter.Label(self,anchor="center",text = 'Nom du noeud :',fg="black",bg="white")
        #self.label.grid(column=0,row=0,columnspan=2,sticky='EW')
        #redimensionnement auto
        self.grid_columnconfigure(0,weight=1)
        self.geometry("800x600+300+0")
        #800x600 <== taille de la fenetre le "x" c'est comme xor
        #+300 <== ou se positionne en x ou essai -300
        #+0 <=== ou se positionne en y ou essai-0

    
