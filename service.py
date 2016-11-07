from ClusterShell.NodeSet import NodeSet, RangeSet
from ClusterShell.Task import task_self
import sys

class service:
    def envoyer(self, args):
        node0 = NodeSet()
        nbNoeud = len(args)-3
        print'nbNoeud: %d'%nbNoeud

        for i in range(1,nbNoeud):
            node0.add(args[i])

                    
        print'sudo service '+args[nbNoeud+1]+' '+args[nbNoeud+2]
        task_self().run('sudo service '+args[nbNoeud+1]+' '+args[nbNoeud+2], nodes=node0)

        for output, nodes in task_self().iter_buffers():
            for node in nodes:
                print '%s: %s'%(node, output)

    
    






if __name__ == "__main__":

    services = service()
    services.envoyer(sys.argv)
    """
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
