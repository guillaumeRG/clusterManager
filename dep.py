class dep:
    fichier=0
    is_install=0
    nodeIs_install=0
    started=0
    nodeStarted=0
    
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
        installLines=[]
        for line in lines :
            if line.split(';')[0]== 'started':
                installLines.append(line)
                
        
    #    print len(installLines)
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
        

    if __name__ == "__main__":
        print'toInstall : '
        toInstall("cfg/nfs-common")
        print'toStart : '
        toStart("cfg/nfs-common")
