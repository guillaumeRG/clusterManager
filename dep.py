class dep:
    fichier=0
    is_install=0
    nodeIs_install=0
    started=0
    nodeStarted=0
    def toInstall(path):
        fichier = open(path,"r")
        installLine=fichier.read().split("\n")[0] #split de la ligne dans le fichier
        nbNode = len(installLine.split(";")[1].split(","))#lecture du nombre de node(s) dependant
        
        
        print nbNode

    if __name__ == "__main__":
        toInstall("cfg/nfs-common")
