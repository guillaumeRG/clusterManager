from ClusterShell.NodeSet import NodeSet, RangeSet
from ClusterShell.Task import task_self
import sys

class service:
    
    def envoyer(self, args,afficher):
        node0 = NodeSet()
        nbNoeud = len(args)-3
        print'nbNoeud: %d'%nbNoeud

        for i in range(1,nbNoeud):
            node0.add(args[i])

        print'sudo service '+args[nbNoeud+1]+' '+args[nbNoeud+2]
        task_self().run('sudo service '+args[nbNoeud+1]+' '+args[nbNoeud+2], nodes=node0)
        if afficher==1:
            self.recevoir()

    def recevoir(self):
        reponse=[]
        
        i=0
        for output, nodes in task_self().iter_buffers():
           for node in nodes:
                print '%s: %s'%(node, output)

                
        

if __name__ == "__main__":
    tab=[]
    services = service()
    services.envoyer(sys.argv,1)

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
