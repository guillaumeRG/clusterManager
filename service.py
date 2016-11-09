from ClusterShell.NodeSet import NodeSet, RangeSet
from ClusterShell.Task import task_self
import sys
#alpha
class service:
    
    def start(self, args):
        dependanceManager= dep()

        
        node0 = NodeSet()
        nbNoeud = len(args)-3
        print'nbNoeud: %d'%nbNoeud

        for i in range(1,nbNoeud):
            node0.add(args[i])

        #verification de la dependance
        dependanceManager.toInstall("cfg/"+args[nbNoeud+1])

        #recuperation des dependances
        startNode = dependanceManager.getNodeStarted()
        startServices = dependanceManager.getStarted()
        installNode = dependanceManager.getNodeIs_install()
        installService = dependanceManager.getIs_install()

        #pour chaque noeud dependant
        for node in startNode:
            
                
        print'sudo service '+args[nbNoeud+1]+' '+args[nbNoeud+2]
        task_self().run('sudo service '+args[nbNoeud+1]+' '+args[nbNoeud+2], nodes=node0)
    def status(self, args,afficher):
        node0 = NodeSet()
        nbNoeud = len(args)-3
        print'nbNoeud: %d'%nbNoeud

        for i in range(1,nbNoeud):
            node0.add(args[i])

        print'sudo service '+args[nbNoeud+1]+' '+args[nbNoeud+2]
        task_self().run('sudo service '+args[nbNoeud+1]+' '+args[nbNoeud+2], nodes=node0)
        if afficher==1:
            self.recevoir(afficher)
    def recevoir(self,statusCtrl):
        
        i=0
        for output, nodes in task_self().iter_buffers():
           for node in nodes:
               print '%s: %s'%(node, output)
               # a tester
               if statusCtrl == 1:
                   if output.split('Active: ')[1].split(' ')[0]=='active':
                       return 1
                   elif output.split('Active: ')[1].split(' ')[0]=='inactive':
                       return 0
                
           # "Active:" "active" "inactive"    
            

if __name__ == "__main__":
    tab=[]
    services = service()
    services.start(sys.argv,1)

    #sudo python service.py localhost dhcpcd status
    
    """print '%s: %s'%(tab[0][0], tab[0][1])
    for i in range(0,len(tab)):
         print '%s: %s'%(tab[i][0], tab[i][1])
    
    node0 = NodeSet()
    nbNoeud = len(sys.argv)-3
    print'nbNoeud: %d'%nbNoeud

    for i in range(1,nbNoeud):
        node0.add(sys.argv[i])

                
    print'sudo service '+sys.argv[nbNoeud+1]+' '+sys.argv[nbNoeud+2]
    task_self().run('sudo service '+sys.argv[nbNoeud+1]+' '+sys.argv[nbNoeud+2], nodes=node0)

    for output, nodes in task_self().iter_buffers():
        for node in nodes:
            print '%s: %s'%(node, output)"""
