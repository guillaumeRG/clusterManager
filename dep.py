class dep:
    fichier=0
    is_install=[]
    nodeIs_install=[]
    started=[]
    nodeStarted=[]
    
    def toInstall(path):
        fichier = open(path,"r")
        lines = fichier.read().split("\n")
        installLines=[]
        for line in lines :
            if line.split(';')[0]== 'is_install':
                installLines.append(line)
                
        
        #print len(installLines)
        #installLines=fichier.read().split("\n")[0] #split de la ligne dans le fichier
        for installLine in installLines:
            print'noeuds : '
            nodeIs_install = installLine.split(";")[1].split(",")
            for node in nodeIs_install:
                print node+' '
            print'\n'
            print 'services : '
            is_install = installLine.split(";")[2].split(",")
            for node in is_install:
                print node+' '
            print'\n'
    def toStart(path):
        fichier = open(path,"r")
        lines = fichier.read().split("\n")
        startedLines=[]
        for line in lines :
            if line.split(';')[0]== 'started':
                startedLines.append(line)
                
        
    #    print len(installLines)
        #installLines=fichier.read().split("\n")[0] #split de la ligne dans le fichier
        for startedLine in startedLines:
            print'noeuds : '
            nodeStarted = startedLine.split(";")[1].split(",")
            for node in nodeStarted:
                print node+' '
            print'\n'
            print 'services to start : '
            started = startedLine.split(";")[2].split(",")
            for node in started:
                print node+' '
            print'\n'
        

    if __name__ == "__main__":
        print'toInstall : '
        toInstall("cfg/nfs-common")
        print'toStart : '
        toStart("cfg/nfs-common")
