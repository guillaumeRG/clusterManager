class dep:
    is_install=[]
    nodeIs_install=[]
    started=[]
    nodeStarted=[]
    targetNodes = []
    targetServices = []
    linkedTo = ''
    def targetNode(self, path):
        fichier = open(path,"r")
        lines = fichier.read().split("\n")
        targetLines=[]
        for line in lines :
            if line.split(';')[0]== 'target':
                targetLines.append(line)
               
                
        
        #print len(installLines)
        #installLines=fichier.read().split("\n")[0] #split de la ligne dans le fichier
        for targetLine in targetLines:
            global targetNodes
            targetNodes = targetLine.split(";")[1].split(",")
    def targetService(self, path):
        fichier = open(path,"r")
        lines = fichier.read().split("\n")
        targetLines=[]
        for line in lines :
            if line.split(';')[0]== 'services':
                targetLines.append(line)
                
        
       
        for targetLine in targetLines:
            global targetServices
            targetServices = targetLine.split(";")[1].split(",")

    def link(self,path):
        fichier = open(path,"r")
        lines = fichier.read().split("\n")
        targetLines=[]
        for line in lines :
            if line.split(';')[0]== 'link':
                targetLines.append(line)
       
        for targetLine in targetLines:
            global linkedTo
            linkedTo = ''
            linkedTo = targetLine.split(";")[1].split(",")
    def toInstall(self,path):
        fichier = open(path,"r")
        lines = fichier.read().split("\n")
        installLines=[]
        for line in lines :
            if line.split(';')[0]== 'is_install':
                installLines.append(line)
                
        
        #print len(installLines)
        #installLines=fichier.read().split("\n")[0] #split de la ligne dans le fichier
        for installLine in installLines:
            global nodeIs_install
            nodeIs_install = installLine.split(";")[1].split(",")

            global is_install
            is_install = installLine.split(";")[2].split(",")

    def toStart(self,path):
        fichier = open(path,"r")
        lines = fichier.read().split("\n")
        startedLines=[]
        for line in lines :
            if line.split(';')[0]== 'started':
                startedLines.append(line)
                
        
    #    print len(installLines)
        #installLines=fichier.read().split("\n")[0] #split de la ligne dans le fichier
        for startedLine in startedLines:
            global nodeStarted
            nodeStarted = startedLine.split(";")[1].split(",")
            global started 
            started = startedLine.split(";")[2].split(",")

    def getStarted(self):
        global started
        return started
    def getNodeStarted(self):
        global nodeStarted
        return nodeStarted
    def getIs_install(self):
        global is_install
        return is_install
    def getNodeIs_install(self):
        global nodeIs_install
        return nodeIs_install
    def getTargetNodes(self):
        global targetNodes
        return targetNodes
    def getTargetServices(self):
        global targetServices
        return targetServices
    def getLinkedTo(self):
        global linkedTo
        return linkedTo
        

    if __name__ == "__main__":
        """print'toInstall : '
        toInstall("cfg/nfs-common")
        print'toStart : '
        toStart("cfg/nfs-common")
        print getStarted()[0]"""
        
        
        targetService("cfg/config1")
        
        print 'services : '+getTargetServices()[0]
        targetNode("cfg/config1")
        
        print 'nodes : '+getTargetNodes()[0]
